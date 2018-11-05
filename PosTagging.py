# -*- coding:utf-8 -*-
import jieba.posseg

content = []
for each in content:
    print each
    seg = jieba.posseg.cut(each)

    for i in seg:
        print i.word, i.flag


        # everyline = "说实话一岁半到三岁的小孩是最难搞的。"
        # content = ltp_api.use_api(everyline,pattern='pos')
        # print content
        # candicate_words = []
        #
        # each = content.split(' ')
        # for i in each:
        #     if 'a' in i:
        #         candicate_words.append(i.split('_')[0])
        #     if 'an' in i:
        #         candicate_words.append(i.split('_')[0])
        #     if 'i' in i:
        #         candicate_words.append(i.split('_')[0])
        #     id 'v' in i:
        #         candicate_words.append(i.split('_')[0])