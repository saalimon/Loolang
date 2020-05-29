# !/usr/bin/python
# coding=utf-8
import re
from pythainlp.tokenize import syllable_tokenize

class Spoonerism:
    def __init__(self,inputText):
        self.inputText = inputText
        self.syl = syllable_tokenize(inputText)
        if "<s/>" in self.syl :
            self.syl.remove("<s/>")
        self.specialCase = '(อย)|(หง)|(หญ)|(หน)|(หม)|(หย)|(หร)|(หล)|(หว)|(กร)|(คร)|(ปร)|(พร)|(ตร)|(กล)|(คล)|(ปล)|(พล)|(กว)|(คว)|[\u0E00-\u0E2E]'
    def checkSwap(self,syl):
        if len(syl) == 2:
            syl[0],syl[1] = syl[1],syl[0]
        elif len(syl) == 3:
            syl[0],syl[2] = syl[2],syl[0]
        return syl
    def word2alpha(self,word):
        result = re.search(self.specialCase, word)
        # print(word,result)
        return result.group(), result.start()
    def spoonerism2syl(self,syl):
        syl = self.checkSwap(syl)
        if len(syl) == 2:
            posSwap1 = 0
            posSwap2 = 1
        elif len(syl) == 3:
            posSwap1 = 0
            posSwap2 = 2
        alpha1,pos1 = self.word2alpha(syl[posSwap1])
        alpha2,pos2 = self.word2alpha(syl[posSwap2])
        s1 = list(syl[posSwap1])
        s2 = list(syl[posSwap2])
        if len(alpha1) == 1 :
            s1[pos1] = alpha2
            s2[pos2] = alpha1
            syl[posSwap1] = "".join(s1)
            syl[posSwap2] =  "".join(s2)
        else :
            s1[pos1] = 'ห'
            s1[pos1+1] = alpha2
            s2[pos2] = alpha1
            syl[posSwap1] = "".join(s1)
            syl[posSwap2] =  "".join(s2)
        # print(s1,s2)
        # print(syl)
        return syl
    def check_condition(self,syl):
        #list of สระอุ และ สระอู
        vowel_cond = [chr(3640),chr(3641)]
        alpha_cond, pos_cond = self.word2alpha(syl)
        syl_list_cond = list(syl)
        if alpha_cond == 'ร' or alpha_cond == 'ล':
            looParam = 'ซู'
        elif ('ุ' in syl_list_cond) or ('ู' in syl_list_cond):
            looParam = 'ลี'
        elif (alpha_cond == 'ร' or alpha_cond == 'ล') and (('ุ' in syl_list_cond) or ('ู' in syl_list_cond)):
            looParam = 'ซี'
        else:
            looParam = "ลู"  
        return looParam
    def Spoon(self):
        full = ""
        if len(self.syl) == 1:
            full = self.inputText 
        elif len(self.syl) == 2:
            full = full + "".join(self.spoonerism2syl(self.syl))
        elif len(self.syl) == 3:
            full = full + "".join(self.spoonerism2syl(self.syl))
        else:
            raise ValueError('cannot used more than 3 syllable')
        #   return "ไม่สามารถใช้กับคำที่มากกว่า 1 พยางค์ได้"
          # print("ไม่สามารถใช้กับคำที่มากกว่า 1 พยางค์ได้")
        # print("-->",full)
        return full
    def Loolang(self):
        full = ""
        for inSyl in self.syl:
            inSyl = [self.check_condition(inSyl),inSyl]
            if len(inSyl) == 2:
                full = full + "".join(self.spoonerism2syl(inSyl))
            else:
                raise ValueError('cannot used more than 2 syllable')
        return full

            
        

