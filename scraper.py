#This is the main program starting point
#break program into multiple files
import .search
import .parse

#user inputs search engine preference
#big ones: google, bing, yahoo, duckduckgo
#or ecommerce site search: etsy, amazon, craigslist, facebook markets, small forums, private sites
#and even sub-sites of the big search engines related to shopping

#user may choose several engines, which will randomize searches through them

#user chooses "Dorks" for optimizing search
#options could be default, random, or custom
#custom allows dorks for beginning, middle, and end of search string

#user chooses keyword list
#default or custom

#user chooses amount of keywords to use at one time
#1 term only, 2 terms, 3 terms, 4 terms, or random

#user inputs additional terms, such as dates, up to 4 - optional
#user has option to add to regular term list or use in every search

#finally user inputs amount of potentials to find in total
#default = 50

#run search using options from above

#run search results through parser, also using options from above

#return csv file location
