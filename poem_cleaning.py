### cleaning up poems

# importing library
import pandas as pd

# importing raw poem data
df = pd.read_csv('data/poem_raw.csv').iloc[:, 1:]

# dropping date
df = df.drop('date', axis = 1)
df = df.dropna()

# cleaning titles
df['title'] = df['title'].str.replace('[\S\s]*name\"\:\"', '').str.replace('\",\"text\":', '')
df['title'] = df['title'].str.replace('\\\\u003C', '<').str.replace('\\\\u003E', '>')
df['title'] = df['title'].str.replace('</*[a-zA-Z]*>', '')

# cleaning authors
df['author'] = df['author'].str.replace('[\S\s]*name\"\:\"', '').str.replace('\"', '')

# cleaning text
df['text'] = df['text'].str.replace('\"text\":\"', '').str.replace('\xa0', '')
df['text'] = df['text'].str.replace('\"$', '').str.replace('\&#39;', '\'')
df['text'] = df['text'].str.replace('^\s*', '').str.replace('\s{2,}', ' ')

# cleaning genres
df['genre'] = df['genre'].str.replace(' ', '').str.replace(',', ' ')

# exporting to csv
df.to_csv('data/poem_clean.csv')