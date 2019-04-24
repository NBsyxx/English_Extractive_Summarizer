from gensim.models import word2vec

model = word2vec.Word2Vec.load("word2vec2withcran")


print("与'about'最相近的单词:")
result = model.most_similar('area')
for each in result:
    print(each[0], each[1])