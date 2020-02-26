### scraping urls off PoetryFoundation for poems

# importing libraries
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

# base url for poetry foundation
url = "https://www.poetryfoundation.org/sitemaps?type=poem&page="

# page number to add onto url (starting at 1 for page 1)
page_number = 1

# a list of length 1 so that it does not satisfy the while loop immediately
poem_url = [1]

# empty list of urls
url_list = np.array([])

# scraping poetry foundation for urls
while len(poem_url) != 0:
    
    # creating the soup
    response = requests.get(url + str(page_number)) # requesting a page
    soup = BeautifulSoup(response.content, "html.parser") # BeautifulSouping
    text = soup.text # turning the soup into readable data
    
    # pulling urls off the page
    poem_url = np.array(re.findall('https://www.poetryfoundation.org/poems/\d+', text)) # regex to find poem specific urls
    
    # checking to see if the scraper is working
    print(poem_url) 
    print(page_number)
    page_number += 1 # to keep the loop moving with an increase in the page number
    
    # append to the page's urls to the overall list
    url_list = np.append(url_list, poem_url)

# turn list into dataframe for exporting to csv    
df = pd.DataFrame({'url' : url_list})

# export dataframe to csv
df.to_csv('poem_url.csv')