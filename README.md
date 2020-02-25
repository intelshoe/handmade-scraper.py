# handmade-scraper.py
Python scraper to find handmade products and list them on a website. Users also have the option of purchasing products through us, and we recieve a small percentage of payment before we purchase directly from manufacturer and send directly to the client (also known as drop-shipping). Profits will be split equally between the original development team.

Organized into 3 main parts:
- Controller - tells models and views to execute and reports errors to log file
- Views - organizes the information into a wordpress format and sends to wordpress as posts
- Models - performs actualy web searches and sorts page data, keeping only relevant data
