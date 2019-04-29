from gensim.models import word2vec
import logging


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence('Training_corpus/corpus_wiki_0.txt', max_sentence_length=100000)
model = word2vec.Word2Vec(sentences, size=200, window=10, min_count=10, sg=1, hs=1, iter=15, workers=8)
model.save('RealTrained.model')





