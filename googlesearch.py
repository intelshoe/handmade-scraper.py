# This script will search google using our web dorks file and search term file
# import needed files
import requests
import urllib.request

#function to perform search
def search(query):
  url = "http://www.google.com/search?q="+query
