umico.az Scraper
================

This is a Python web scraper built to extract car information from umico.az, one of the most popular online purchase websites in Azerbaijan. 

Features
--------

-   Extracts item details including name, price, img_url, url, and seller.
-   Data is saved in CSV format.
-   Requests and Beautiful Soup libraries are used for web scraping.
-   Code may need to be updated due to possible changes in website HTML tags.

Installation
------------

1.  Clone this repository.
2.  Install the required dependencies by running `pip install -r requirements.txt` in your terminal.

Installation
----------

You can install umico2csv via pip:

```bash
pip install umico2csv
```

Usage
----------
```py
from umico2csv import Scraper

scraper = Scraper()

scraper.scrape(output_file='umico.csv', start=1)


```

Disclaimer
----------

This application is intended for educational purposes only and should not be used for commercial purposes. The author is not responsible for any legal issues that may arise from the misuse of this tool.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.
