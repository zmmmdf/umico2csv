import requests
from bs4 import BeautifulSoup
from csv import writer
import sys

class Scraper:
    def __init__(self):
        pass

    def scrape(self, output_file='umico.csv', start=1):
        page_url = 'https://umico.az/search?page=1'
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        pagination_items = soup.find_all(class_='MPProductPagination-PageItem')
        if pagination_items:
            last_page_number = int(pagination_items[-2].text)
        else:
            last_page_number = 1

        print(f"Starting the scraping process from page {start} to page {last_page_number}")

        unique_entries = set()

        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            csv_writer = writer(file)
            csv_writer.writerow(['Image URL', 'Name', 'Price', 'Seller', 'Link'])

            for page in range(start, last_page_number + 1):
                page_url = f'https://umico.az/search?page={page}'
                response = requests.get(page_url)
                page_soup = BeautifulSoup(response.text, 'html.parser')

                items = page_soup.find_all(class_='MPProductItem')

                for item in items:
                    try:
                        img_url = item.select_one('.MPProductItem-Logo img')['src']
                        name = item.select_one('.MPTitle').text.strip()
                        price = item.select_one('span.flex.flex-col.justify-end.text-base.leading-6.font-bold span').text.strip()
                        if price.count('.') > 1:
                            price = item.select('span.flex.flex-col.justify-end.text-base.leading-6.font-bold span span')[0].text.strip()
                        if not (name and price): continue
                        seller = item.select_one('.MPProductItem-Seller div span:last-child').text.strip()
                        link = "https://umico.az" + item.select_one('a[href]')['href'].split('-')[0]
                        entry = (img_url, name, price, seller, link)

                        if entry not in unique_entries:
                            unique_entries.add(entry)
                            csv_writer.writerow(entry)
                    except Exception as e:
                        print(f"\nError processing item entry on page {page}: {e}")
                        pass

                # Print the progress without a newline
                sys.stdout.write(f"\rScraping page {page} of {last_page_number}")
                sys.stdout.flush()

            print("\nScraping complete.")
