### importing libraries ###

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


### importing dataframes ###

df = pd.read_csv('data/poem.csv', index_col = 0)
text = pd.read_csv('data/text.csv', index_col = 0)
genre = pd.read_csv('data/genre.csv', index_col = 0)
author = pd.read_csv('data/author.csv', index_col = 0)


### build function ###

# a function to append metrics into pandas dataframe
def features(metrics):
    '''
    function to append metrics
    
    input:
    metrics -> list of features
    
    output: 
    appended pandas dataframe
    '''
    
    feature = metrics[0]
    
    if len(metrics) > 1:
        for metric in metrics[1:]:
            feature = feature.join(metric)
        
    return feature
    

# a function to fit metrics into KNN model
def build_model(metrics):
    '''
    function to build a model
    
    input: 
    metrics -> list of features
    
    output: 
    KNN model
    '''
    
    feature = features(metrics)
    
    model = KNeighborsClassifier().fit(feature, df.index)
    
    return model

# a function to return index of neighbours
def neighbours(metrics, n_neighbours, poem_index):
    '''
    function to return nearest neighbours
    
    input: 
    metrics -> list of features
    n_neighbours -> int number of recommendations
    poem_index -> index of poem
    
    output:
    index of neighbours
    '''
    
    feature = features(metrics)
    
    model = build_model(metrics)
    
    poem = feature.iloc[poem_index:poem_index+1, :]
    
    neighbours = model.kneighbors(X = poem, n_neighbors = n_neighbours + 1)
    
    return neighbours[1][0][1:]

# a function return poem recommendations
def recommend(metrics = [text, genre, author * 2], n_neighbours, poem_index):
    '''
    function to return recommendations
    
    input: 
    metrics -> list of features
    n_neighbours -> int number of recommendations
    poem_index -> index of poem
    
    output:
    recommendations
    '''
    
    title = df.iloc[poem_index, 0]
    author = df.iloc[poem_index, 1]
    text = df.iloc[poem_index, 3]
    
    print(f'Your poem is \"{title}\" by {author}: \n{text} \n')
    
    indices = neighbours(metrics, n_neighbours, poem_index)
    
    for index in indices:
        title = df.iloc[index, 0]
        author = df.iloc[index, 1]
        text = df.iloc[index, 3]
        
        print(f'A recommended poem is \"{title}\" by {author}: \n{text} \n')