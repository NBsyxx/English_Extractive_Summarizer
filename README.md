# English_Extractive_Summarizer
An extractive summarizer for English, based on word2Vec and text rank



#---------Instructions-------------

git clone 

make sure the trained model is in folder.

------test word2vec:---

1.install gensim package by typing (Linux)

>>pip3 install gensim 

2. type 

>>python3 word2vec_text.py

and hit enter

------- SUMMARIZER-----
Automatic summarize:
1. name source text as 'input.txt', make sure it's in folder 
2. type

>>python3 textRank.py

and hit enter

* for percentage output, uncomment line 160 in textRank.py



#---------Development Ideas--------

This summarizer aims to extract several most important sentences in a piece of formally written English Material,
it ranks the sentences in text and gives the most important ones.
the extraction is based on calculated score of each sentence in the context. The score is calculated based on textrank,
which reveals the connectivity among sentences. The connection between sentences is evaluated using the cosine
similarities. Each sentence receives votes (connections with othersentences) and get a calculated score round by round, 
when the score of each sentence is no longer changing, we will output the ranked sentences. 




