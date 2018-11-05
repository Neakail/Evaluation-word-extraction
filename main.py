# -*- coding:utf-8 -*-
import text_processing
import text_preprocessing
from ltp_local import *

if __name__ == '__main__':
    f = open('tmp2.txt', 'w')
    content = text_preprocessing.text_preprocessing.readline3()
    for i in content:
        candicate_words = []
        sentence = i[0]
        print sentence
        print "-----------------------------------"
        print "依存句法分析结果为："
        print "-----------------------------------"
        opinionobject = i[1]
        wordlist = jieba_segmentor(sentence, opinionobject)
        wordlists = []
        for i in wordlist:
            # print wordlist
            wordlists.append(i.encode('utf-8'))

        lines = []
        pos = posttagger(wordlists)
        arcs = parse(wordlists, pos)
        index_a = 0
        for arc in arcs:
            index_b = arc.head - 1
            relation = arc.relation
            if index_b >= 0:
                each_sentence = wordlists[index_a] + '_' + str(index_a) + ' ' + wordlists[index_b] + '_' + str(
                    index_b) + ' ' + relation
                print each_sentence
                lines.append(each_sentence)
            else:
                each_sentence = wordlists[index_a] + '_' + str(index_a) + ' ' + str(index_b) + ' ' + relation
                print each_sentence
                lines.append(each_sentence)
            index_a += 1

        words_att = text_processing.text_processing.find_att(lines, opinionobject)
        words_sbv = text_processing.text_processing.find_sbv(lines, opinionobject)
        words_coo = text_processing.text_processing.find_coo(lines, opinionobject)
        words_vob = text_processing.text_processing.find_vob(lines, opinionobject)
        for i in words_att:
            candicate_words.append(i)
        for i in words_sbv:
            candicate_words.append(i)
        for i in words_coo:
            candicate_words.append(i)
        if len(candicate_words) == 0:
            print opinionobject + "没有评价词"
            print "-----------------------------------"

        else:
            print "-----------------------------------"
            print opinionobject + "的评价词有:"
            print "-----------------------------------"
            for i in candicate_words:
                print i
            print "-----------------------------------"
            f.write(sentence + "|" + opinionobject + "|" + '*'.join(candicate_words))
            f.write('\n')
    f.close()