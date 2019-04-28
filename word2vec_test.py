from gensim.models import word2vec
import gensim.downloader as api


def print_closest_words(word):
    print("\nWords close to " + word)
    result = model.most_similar(word)
    for each in result:
        print(each[0], each[1])



model = word2vec.Word2Vec.load("realTrained.model")
print_closest_words('Balenciaga')
print_closest_words('Versace')
print('\n')

result = model.most_similar(positive=['Food','Chinese'])
for i in result:
    print(i[0],i[1])
print('\n')
result = model.most_similar(positive=['expensive','clothing'])
for i in result:
    print(i[0],i[1])