# handmade-scraper.py
Python scraper to find handmade products and list them on a website.

Organized into 3 main parts:
- Controller - tells models to execute and reports errors to log file
- Views - organizes the information into a wordpress format and sends to wordpress as posts
- Models - performs actualy web searches and sorts page data, keeping only relevant data
