import re
import datetime


for i in range(0, 10):
    print(datetime.datetime.now(), 'opening the wiki_{}'.format(i),)
    filename = 'wiki_{}'.format(str(i))
    file_output = open('corpus_wiki_{0}'.format(str(i)), 'a', encoding="utf8")
    file_input = open(filename, 'r',encoding="utf8")
    count = 0
    while True:
        count += 1
        line = file_input.readline()
        if line == '':
            break
        else:
            line = re.sub(r"<[a-zA-ZÀ-ÿ()/:,.\s\'\"=?0-9\-]+>", '', line)
            file_output.write(line)
        if count % 100000 == 0:
            print(datetime.datetime.now(), 'finished', count, 'lines')
    file_input.close()
    file_output.close()
    print(datetime.datetime.now(), 'the{} has been done'.format(i),)
