import asyncio
import aiohttp
import csv
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        pass

    async def scrape_page(self, session, page_url):
        async with session.get(page_url) as response:
            html = await response.text()
            page_soup = BeautifulSoup(html, 'html.parser')

            items = page_soup.find_all(class_='MPProductItem')
            entries = []

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
                    entries.append(entry)
                except Exception as e:
                    print(f"\nError processing item entry on page {page_url}: {e}")
                    pass

            print(f"\rScraping page {page_url}...", end='', flush=True)
            return entries

    async def scrape(self, output_file='umico.csv', start=1):
        page_url = 'https://umico.az/search?page=1'
        async with aiohttp.ClientSession() as session:
            response = await session.get(page_url)
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')

            pagination_items = soup.find_all(class_='MPProductPagination-PageItem')
            if pagination_items:
                last_page_number = int(pagination_items[-2].text)
            else:
                last_page_number = 1

            print(f"Starting the scraping process from page {start} to page {last_page_number}")

            unique_entries = []

            with open(output_file, 'a', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(('Image URL', 'Name', 'Price', 'Seller', 'Link'))
            tasks = []
            
            for page in range(start, last_page_number + 1):
                page_url = f'https://umico.az/search?page={page}'
                tasks.append(self.scrape_page(session, page_url))

                if page % 100 == 0 or page == last_page_number:
                    entries = await asyncio.gather(*tasks)
                    for entry_list in entries:
                        unique_entries.extend(entry_list)

                    with open(output_file, 'a', newline='', encoding='utf-8') as file:
                        csv_writer = csv.writer(file)
                        for entry in unique_entries:
                            csv_writer.writerow(entry)

                    tasks.clear()
