from gensim.models import word2vec
import math
import numpy as np
from nltk.tokenize import word_tokenize
import time


time_start = time.time()
global stop_word_list
global model


stop_word_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
                  "you", "your", "yours", "yourself", "yourselves", "he", "him",
                  "his", "himself", "she", "her", "hers", "herself", "it", "its",
                  "itself", "they", "them", "their", "theirs", "themselves", "what",
                  "which", "who", "whom", "this", "that", "these", "those", "am", "is",
                  "are", "was", "were", "be", "been", "being", "have", "has", "had",
                  "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but",
                  "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
                  "with", "about", "against", "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
                  "over", "under", "again", "further", "then", "once", "here", "there", "when",
                  "where", "why", "how", "all", "any", "both", "each", "few", "more", "most",
                  "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                  "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Load the pre-trained model as global
model = word2vec.Word2Vec.load("realTrained.model")


def cut_sentences(sentence):
    puns = frozenset('.')
    tmp = []
    for ch in sentence:
        tmp.append(ch)
        if puns.__contains__(ch):
            yield ''.join(tmp)
            tmp = []
    yield ''.join(tmp)


def two_sentences_similarity(sents_1, sents_2):
    counter = 0
    for sent in sents_1:
        if sent in sents_2:
            counter += 1
    return counter / (math.log(len(sents_1) + len(sents_2)))


def cosine_similarity(vec1, vec2):
    tx = np.array(vec1)
    ty = np.array(vec2)
    cos1 = np.sum(tx * ty)
    cos21 = np.sqrt(sum(tx ** 2))
    cos22 = np.sqrt(sum(ty ** 2))
    cosine_value = cos1 / float(cos21 * cos22)
    return cosine_value


def clear_oov(sents):
    temp = []
    for word in sents[1:]:
        if word in model.wv.vocab:
            temp.append(word)
    return temp


def compute_similarity_by_avg(sents_1, sents_2):
    if len(sents_1) == 0 or len(sents_2) == 0:
        return 0.0
    sents_1 = clear_oov(sents_1)
    sents_2 = clear_oov(sents_2)
    vec1 = model[sents_1[0]]
    for word1 in sents_1[1:]:
        vec1 = vec1 + model[word1]
    vec2 = model[sents_2[0]]
    for word2 in sents_2[1:]:
        vec2 = vec2 + model[word2]
    similarity = cosine_similarity(vec1 / len(sents_1), vec2 / len(sents_2))
    return similarity


def calculate_score(weight_graph, scores, i):
    length = len(weight_graph)
    d = 0.85
    added_score = 0.0
    for j in range(length):
        denominator = 0.0
        fraction = weight_graph[j][i] * scores[j]
        for k in range(length):
            denominator += weight_graph[j][k]
            if denominator == 0:
                denominator = 1
        added_score += fraction / denominator
    weighted_score = (1 - d) + d * added_score
    return weighted_score


def weight_sentences_rank(weight_graph):
    scores = [0.5 for _ in range(len(weight_graph))]
    old_scores = [0.0 for _ in range(len(weight_graph))]
    while different(scores, old_scores):
        for i in range(len(weight_graph)):
            old_scores[i] = scores[i]
        for i in range(len(weight_graph)):
            scores[i] = calculate_score(weight_graph, scores, i)
    return scores


def different(score_1,score_2):
    difference = []
    for i in range(0, score_1.__len__()):
        difference.append(score_1[i]-score_2[i])
    sum_of_square = 0
    for j in difference:
        sum_of_square += j * j
    print('Difference:', sum_of_square)
    if sum_of_square < 0.00001:
        return False
    else:
        return True


def create_graph(sents):
    texts = len(sents)
    graph = {}
    for i in range(0,texts):
        temp = {}
        for j in range(0,texts):
            temp[j] = compute_similarity_by_avg(sents[i], sents[j])
        graph[i] = temp
    return graph


def filter_stop_words(sents):
    filtered_list = []
    for sent in sents:
        if sent not in stop_word_list:
            filtered_list.append(sent)
    return filtered_list


def summarize(text, n):
    tokens = cut_sentences(text)
    sentences = []
    sents = []
    for sent in tokens:
        temp = [word for word in word_tokenize(sent) if word]
        if temp.__len__()>= 6:
            sents.append(temp)
            sentences.append(sent)
    sents = filter_stop_words(sents)
    graph = create_graph(sents)
    scores = weight_sentences_rank(graph)
    print('----------Scores Calculated------------')
    print(scores)

    # if you want to output percentage of code, modify here!!
    #n = int(len(sentences)*0.2)
    sent_selected = nlargest(n, scores)
    sent_index = []
    for i in range(n):
        sent_index.append(sent_selected[i][1])
    sent_index.sort()
    print('---Sentences Returned--- with', sent_selected.__len__()/sents.__len__(),'---of the sentence kept')
    return [sentences[i] for i in sent_index]


def count_sentence_with_score(compare_score,scores):
    count = 0
    for score in scores:
        if score > compare_score:
            count += 1
    return count


def nlargest(n, iterable):
    rank_list = []
    count = 0
    for i in iterable:
        rank_list.append((i, count))
        count += 1
    rank_list.sort(key = lambda a : a[0],reverse=True)
    return rank_list[0:n]


if __name__ == '__main__':
    time_start = time.time()
    file = open("input.txt", "r",errors='ignore')
    original_text = file.read()
    text = original_text.replace('\n', '')
    file.close()
    print('-----------The Original Text is:----------------------')
    print(original_text)
    print('------------------------------------------------------')

    num_of_sents = int(input('Number Sentences for Generated Summary?\n'))
    summarize_text = summarize(text, num_of_sents)
    print('-----------Running-------------------------------------')

    for i in summarize_text:
        print(i)
    time_end = time.time()
    print('It takes '+str(time_end-time_start)+'s to extract Summary')
