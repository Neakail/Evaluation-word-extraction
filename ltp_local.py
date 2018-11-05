# -*- coding:utf-8 -*-

from pyltp import Postagger
from pyltp import Parser
import jieba

def jieba_segmentor(sentence,opinionobject):
    jieba.add_word(opinionobject)
    # jieba.add_word('没人性')
    word_list = jieba.cut(sentence=sentence)
    return word_list


#依存语义分析
def parse(words, postags):
    parser = Parser()  # 初始化实例
    parser.load('/home/linnankai/ltp_data_v3.4.0/parser.model')  # 加载模型
    arcs = parser.parse(words, postags)  # 句法分析
    # print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
    parser.release()  # 释放模型
    return arcs

def posttagger(words):
    tags = []
    postagger = Postagger()  # 初始化实例
    postagger.load('/home/linnankai/ltp_data_v3.4.0/pos.model')  # 加载模型
    postags = postagger.postag(words)  # 词性标注
    for word,tag in zip(words,postags):
        tags.append(tag)
    postagger.release()  # 释放模型
    return tags

def addword(word):
    jieba.add_word(word)


