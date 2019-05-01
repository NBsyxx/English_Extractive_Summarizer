# English_Extractive_Summarizer
An extractive summarizer for English, based on word2Vec and text rank

--Development Ideas--

1. overview
This summarizer aims to extract several most important sentences in a piece of formally written English Material,
it ranks the sentences in text and gives the most important ones.
the extraction is based on calculated score of each sentence in the context. The score is calculated based on textrank,
which reveals the connectivity among sentences. The connection between sentences is evaluated using the cosine
similarities. Each sentence receives votes (connections with othersentences) and get a calculated score round by round, 
when the score of each sentence is no longer changing, we will output the ranked sentences. 
    
    2. word embedding
    Since the training corpus is large therefore I am choose methods that generate word vectors with small and fixed 
    dimension. The word embedding is carried out by using word2vec module from gensim, which shrinks or expands the dimension of 
    different wrods, to a fixed dimension. My traininig corpus is Wikipedia which is extracted from downloaded database
    
    3.text rank score
    This step takes the text as input and splits the text into seperate sentences. It constracts a graph where every 
    sentence has edges to any other sentences. 
    
    still trying to find a way to evaluate. 
