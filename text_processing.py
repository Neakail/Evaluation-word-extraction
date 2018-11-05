# -*- coding:utf-8 -*-




class text_processing(object):

    def __init__(self):
        pass

    @classmethod
    def find_att(cls,lines,opinionobject):
        # 变态_0 老师_2 ATT --> 找"变态"
        attword = []
        for line in lines:
            each = line.split(' ')
            former = each[0]
            later = each[1]
            relation = each[2]
            if opinionobject in later and relation == 'ATT':
                opinionword = former.split('_')[0]
                radword = text_processing.find_rad(lines,opinionword)
                vobword = text_processing.find_vob(lines,opinionword)
                advword = text_processing.find_adv(lines,opinionword)
                if advword:
                    opinionword = advword + opinionword
                if vobword:
                    opinionword += vobword
                if radword:
                    opinionword += radword
                if len(opinionword) > 3:
                    attword.append(opinionword)
        return attword


    @classmethod
    def find_rad(cls,lines,attobject):
        # 的_1 变态_0 RAD --> 找"的"
        for line in lines:
            each = line.split(' ')
            former = each[0]
            later = each[1]
            relation = each[2]
            if attobject in later and relation == 'RAD':
                radword = former.split('_')[0]
                return radword

    @classmethod
    def find_vob(cls,lines,attobject):
        # 人性_5 没_4 VOB --> 找"人性"
        for line in lines:
            each = line.split(' ')
            former = each[0]
            later = each[1]
            relation = each[2]
            if attobject in later and relation == 'VOB':
                vobword = former.split('_')[0]
                # attword = text_processing.find_att(lines,vobword)
                # if attword:
                #     vobword = attword + vobword
                return vobword

    @classmethod
    def find_vob_reserve(cls,lines,attobject):
        # 人性_5 没_4 VOB --> 找"没"
        for line in lines:
            each = line.split(' ')
            former = each[0]
            later = each[1]
            relation = each[2]
            if attobject in former and relation == 'VOB':
                vobword = later.split('_')[0]
                # attword = text_processing.find_att(lines,vobword)
                # if attword:
                #     vobword = attword + vobword
                return vobword


    @classmethod
    def find_sbv(cls,lines,opinionobject):
        # 畜生_7 不如_8 SBV --> 找"不如"
        opinionword = []
        for line in lines:
            each = line.split(' ')
            former = each[0]
            later = each[1]
            relation = each[2]
            if opinionobject in former and relation == 'SBV':
                sbvword = later.split('_')[0]
                vobword = text_processing.find_vob(lines, sbvword)
                cooword = text_processing.find_coo(lines,sbvword)
                if vobword:
                    sbvword += vobword

                    # 是否缩进
                    opinionword.append(sbvword)


                for i in cooword:
                    sbv_reserve = text_processing.find_sbv_reserve(lines,i)
                    if sbv_reserve:
                        i = sbv_reserve + i

                        # 是否缩进
                        opinionword.append(i)
        return opinionword

    @classmethod
    def find_sbv_reserve(cls,lines,opinionobject):
        # 畜生_7 不如_8 SBV --> 找"畜生"
        for line in lines:
            each = line.split(' ')
            former = each[0]
            later = each[1]
            relation = each[2]
            if opinionobject in later and relation == 'SBV':
                sbv_reserve_word = former.split('_')[0]
                return sbv_reserve_word


    @classmethod
    def find_coo(cls,lines,opinionobject):
        # 不如_8 没_4 COO -->找"不如"/"没"
        coowords = []
        for line in lines:
            each = line.split(' ')
            former = each[0]
            later = each[1]
            relation = each[2]
            if opinionobject in later and relation == 'COO':
                cooword = former.split('_')[0]
                coowords.append(cooword)
            if opinionobject in former and relation =='COO':
                cooword = later.split('_')[0]
                coowords.append(cooword)
        return coowords

    @classmethod
    def find_adv(cls,lines,opinionobject):
        # 不_7 厚道_8 ADV -->找"不"
        for line in lines:
            each = line.split(' ')
            former = each[0]
            later = each[1]
            relation = each[2]
            if opinionobject in later and relation == 'ADV':
                advword = former.split('_')[0]
                return advword
