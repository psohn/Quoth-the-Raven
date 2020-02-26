### using urls for poems for PoetryFoundation to scrape poems

# importing libraries
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

# importing scraped urls
url_list = pd.read_csv('poem_url.csv')['url']

# url number used to debug
url_number = 1

# empty arrays of fields we want to scrape
title_list = np.array([])
author_list = np.array([])
date_list = np.array([])
genre_list = np.array([])
text_list = np.array([])

# scraping poetry foundation for poems
for url in url_list:
    
    try:
        # creating the soup
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # regex pattern search for fields
        title = re.findall("\"description\":.*\"text\":", soup.text)
        author = re.findall("\"author\":{[^}]*", soup.text)
        date = re.findall("\"datePublished\":\"[0-9]*\"", soup.text)
        genre = soup.find("meta", property="article:tag")["content"]
        text = re.findall("\"text\":[^}]*", soup.text)

        # debugging
        print(url_number)
        url_number += 1
        
        # appending fields to array (if empty, appending empty)
        if len(title) != 0:
            title_list = np.append(title_list, title)
        else:
            title_list = np.append(title_list, None)
        
        if len(author) != 0:
            author_list = np.append(author_list, author)
        else:
            author_list = np.append(author_list, None)
        
        if len(date) != 0:
            date_list = np.append(date_list, date)
        else: 
            date_list = np.append(date_list, None)
        
        if len(genre) != 0:
            genre_list = np.append(genre_list, genre)
        else:
            genre_list = np.append(genre_list, None)
        
        if len(text) != 0:
            text_list = np.append(text_list, text)
        else:
            text_list = np.append(text_list, None)
            
    except:
        pass

# creating dataframe for data
df = pd.DataFrame()

df['title'] = title_list
df['author'] = author_list
df['date'] = date_list
df['genre'] = genre_list
df['text'] = text_list

# exporting to csv
df.to_csv('poem_raw.csv')