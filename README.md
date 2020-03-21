# handmade-scraper.py
Python scraper to find handmade products and list them on a website. 

Organized into 3 main parts (based on MVC):
- scraper.py - runs from command line, tells search and post to execute, reports errors to log file, and sends good posts to site
- parse.py - parses for potential good content and organizes the information into a wordpress postable format
- search.py - performs actualy web searches
