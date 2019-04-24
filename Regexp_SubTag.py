import re
import datetime


for i in range(0, 13):
    print(datetime.datetime.now(), 'opening the wiki_{}'.format(i),)
    filename = 'Wiki_source/wiki_{}.txt'.format(str(i))
    file_input = open(filename, 'r', errors= 'ignore')
    file_output = open('Training_corpus/corpus_wiki_{0}.txt'.format(str(i)), 'a', errors='ignore')
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
                file_output.write(line)
        if count % 100000 == 0:
            print(datetime.datetime.now(), 'finished', count, 'lines')
    file_input.close()
    file_output.close()
    print(datetime.datetime.now(), 'the{} has been done'.format(i),)
