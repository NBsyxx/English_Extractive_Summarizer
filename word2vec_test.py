from gensim.models import word2vec
import gensim.downloader as api


def print_closest_words(word):
    print("\nWords close to " + word)
    result = model.most_similar(word)
    for each in result:
        print(each[0], each[1])



model = word2vec.Word2Vec.load("realTrained.model")
print_closest_words('overwatch')
print_closest_words('Tracer')
print('\n')

result = model.most_similar(positive=['light','electricity'])
for i in result:
    print(i[0],i[1])
print('\n')
result = model.most_similar(positive=['fire','work','man'])
for i in result:
    print(i[0],i[1])