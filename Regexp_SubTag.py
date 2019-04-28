import re
import datetime
global stop_word_list
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



for i in range(1, 13):
    print(datetime.datetime.now(), 'opening the wiki_{}'.format(i),)
    filename = 'Wiki_source/wiki_{}.txt'.format(str(i))
    file_input = open(filename, 'r', encoding='utf-8',errors='ignore')
    file_output = open('Training_corpus/corpus_wiki_{0}'.format(str(i)), 'a',encoding='utf-8', errors='replace')
    count = 0
    while True:
        count += 1
        line = file_input.readline()
        if line == '':
            break
        else:
            #line = re.sub(r"<[a-zA-ZÀ-ÿ()/:,.\s\'\"=?0-9\-]+>", '\n', line)
            list = re.findall(r"\<[a-zA-ZÃ¶€â³©、&()/:,.\s\'\"=?0-9\-“”’‘。，；：¡]+\>", line)
            if list.__len__() >= 1:
                continue
            elif line == '\n':
                continue
            else:
                line = re.sub(r"[;:.\'\", ?]\s", ' ', line)
                line = ' '.join([word for word in line.split() if word not in stop_word_list])
                file_output.write(line)

        if count % 50000 == 0:
            print('     ', line)
            print(datetime.datetime.now(), 'finished', count, 'lines')
    file_input.close()
    file_output.close()
    print(datetime.datetime.now(), 'the {} has been done'.format(i), count)
