from gensim.models import word2vec
import logging


def train(filename, model_name):
    model = word2vec.Word2Vec.load(model_name)
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence(filename, max_sentence_length=100000)
    model.train(sentences, total_examples=len(list(sentences)), epochs=15)
    model.save(model_name)

train('continue.txt','word2vec_wiki_corpus.model')

