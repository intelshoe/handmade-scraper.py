# This script will search google using our web dorks file and search term file
# import needed files
import requests
from bs4 import BeautifulSoup

#function to perform search
def search(query):
   URL = "https://www.google.com/search?q=StackOverflow"
   headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 
            (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
   resp = requests.get(URL, headers=headers).text 
   soup = BeautifulSoup(resp, 'html.parser')
   #exampled of what is possible to find
   for link in soup.findAll('a', href=True): 
       if 'facebook.com' in link.get('href'):
           print link.get('href')
            
 #define search function
 
#if user chose google then
    #if user chose terms to use with every search, then
            
    #elif user wants to add terms to keyword list, then
#else
print("Invalid search options")            
