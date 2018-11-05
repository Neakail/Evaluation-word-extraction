# -*- coding:utf-8 -*-

class text_preprocessing(object):

    def __init__(self):
        pass

    @classmethod
    def readline(cls):
        with open('comment_obj.txt', 'r') as f:
            content = {}
            for line in f.readlines():
                each = line.split('|')
                content[each[0]] = each[1].replace('\r\n','')
        return content

    @classmethod
    def readline2(cls):
        with open('comment_obj.txt', 'r') as f:
            content = []
            for line in f.readlines():
                each = line.split('|')
                content.append((each[0],each[1].replace('\r\n', '')))
        return content

    @classmethod
    def readline3(cls):
        with open('shanghaixiecheng.txt', 'r') as f:
            content = []
            for line in f.readlines():
                each = line.split('@@@')
                if each[1] != '':
                    each_objection = each[1].split('###')
                    for i in each_objection:
                        content.append((each[0],i.replace('\r\n', '')))
        return content


if __name__ == '__main__':

    text_preprocessing.readline2()