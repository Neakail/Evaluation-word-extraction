# -*- coding:utf-8 -*-
import urllib2
import time
import text_preprocessing
import text_processing
import sys

import chardet
reload(sys)
sys.setdefaultencoding('UTF-8')
class ltp_api(object):

    @classmethod
    def use_api(self,text, format='plain', pattern = 'dp'):
        url_get_base = "http://api.ltp-cloud.com/analysis/?"
        api_key = "x1v5M5s4A8SRaKXuEvds1CanbnCTSaenAlHX6HTX"
        # 结果格式，有xml、json、conll、plain（不可改成大写）
        # 指定分析模式，有ws、pos、ner、dp、sdp、srl和all
        result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s"
                                 % (url_get_base, api_key, text, format, pattern))
        content = result.read().strip()
        return content

if __name__ == '__main__':
    print "LTP分词效果"
    print "-----------------------------------"
    print "上海妇联，这事儿就跟你一点关系都没有吗？"
    print "-----------------------------------"
    print "分词结果为："
    print "-----------------------------------"
    print ltp_api.use_api(text='上海妇联，这事儿就跟你一点关系都没有吗？',pattern='ws')


    # content = text_preprocessing.text_preprocessing.readline()
    #
    # for everyline in content:
    #     candicate_words = []
    #     #everyline = "变态的老师，没人性，畜生不如！"
    #
    #     # 看这老师年轻貌美身材好咋就这么心狠呢？像这种狠毒的女人拉去当慰安妇我是不是反对的
    #     # 这都四天了，妇联的稿子还没准备好？脸皮咋这么厚呢
    #     everyline = "可伶的孩子们，严惩责任方"
    #     print everyline
    #     dp_result = ltp_api.use_api(everyline).replace('\n\n','\n')
    #     print dp_result
    #     lines = dp_result.split('\n')
    #     opinionobject = content[everyline]
    #     words_att = text_processing.text_processing.find_att(lines,opinionobject)
    #     words_sbv = text_processing.text_processing.find_sbv(lines,opinionobject)
    #     words_coo = text_processing.text_processing.find_coo(lines,opinionobject)
    #     for i in words_att:
    #         candicate_words.append(i)
    #     for i in words_sbv:
    #         candicate_words.append(i)
    #     for i in words_coo:
    #         candicate_words.append(i)
    #     if len(candicate_words) == 0:
    #         print content[everyline] + "没有评价词"
    #
    #     else:
    #         print content[everyline] + "的评价词有:"
    #         for i in candicate_words:
    #             print i
    #     raw_input()


