#This is the main program starting point
#break program into multiple files
import .search
import .parse

#user inputs search engine preference
#right now only supporting google and etsy searches

#user chooses "Dorks" for optimizing search
#options could be default, random, or custom
#custom allows dorks for beginning, middle, and end of search string

#user chooses keyword list
#default or custom

#user chooses amount of search terms to use at one time
#1 term only, 2 terms, 3 terms, 4 terms, or random

#user inputs additional terms, such as dates, up to 4 - optional
#user has option to add to regular term list or use in every search

#finally user inputs amount of potentials to find in total
#default = 50

#run search using options from above
#return any errors found

#run search results through parser, also using options from above
#return any errors

#return csv file location
