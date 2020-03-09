# Quoth the Raven
Poetry recommender system using poetry scraped from PoetryFoundation (PF). 

Using poetry scraped from PF, we used several metrics to make a recommendation system. We used the text, author, and genres (as assigned by PF). We took the text and applied Tf-idf vectorization, took the author and applied one hot encoding, and took the genres and applied one hot encoding. With authors, we found that recommendations should give authors a bigger weight and with a default K-nearest neighbours (KNN) algorithm applied to make recommendations, poems by the same author were not showing in recommendations as genres and text had a bigger weight in the Euclidean distance metric (which we chose). Thus, we doubled the weight of the authors so that poems by the same author would be recommended automatically. With genres, we found that there were too many different genres assigned and a lot of them overlapped (such as grief and grieving) so we manually aggregated them since clustering wouldn't catch these unless the genres were co-occurring. Finally, we found a model using all three metrics (text, author, genre) that gave good recommendations. It is of note that the quality of the recommendations were subjective as there is no ground truth label to compare them to.

# Contributors
Philip Sohn

# Source
All data was scraped from PoetryFoundation: https://www.poetryfoundation.org/
