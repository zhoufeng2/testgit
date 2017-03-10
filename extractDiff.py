#! /usr/bin/env python
#encoding=utf-8


# diff excel：字段XML_id、StringID、XML_content、对应的语言的Content
#  1.从compare表中的Diffent_all_languages第二列开始,抽出--前面的语言language，判断--后面如果是StringID，则继续查询，并扫面每行
# if StringID == Not to match:
#     1.从Diffent_all_languages抽出XML_id，StringID, 对应语言的content
#     2.从out表对应的语言表中抽出XML_content，从en表中抽出对应的语言content
#     3.保存在Different中的对应的语言中

import sys
# version2.7+
if "3" != sys.version[0:1]:
  reload(sys)
  sys.setdefaultencoding('utf-8')

import os
import xlrd
import xlwt
import re

LANGUAGES_MATCH = {"en":"UK English-Full",
    "th":"Thai-Full",
    "pt":"Portuguese_Full",
    "es":"Spanish_full",
    "zh-cn":"Mandarin_Full"}

STRING_ID_OUT = {"UK English-Full":3,"Thai-Full":4,"Portuguese_Full":5,"Spanish_full":6,"Mandarin_Full":7}

class EasyExcel:
    """docstring for EasyExcel"""
    def __init__(self, fileName):
        if fileName:
            self.filename = fileName
            try:
                self.xlBook = xlrd.open_workbook(fileName)
            except Exception as e:
                print(e)
                print('Open file error,may be no this file')
            else:
                pass

    def setSheet(self, sheetName):
        return self.xlBook.sheet_by_name(sheetName)

    def getSheets(self):
        return self.xlBook.sheets()

class NewExcel:
    def __init__(self):
        self.workbook = xlwt.Workbook()
        self.count = 0

    def addSheet(self,sheetName):
        self.sheet = self.workbook.add_sheet(sheetName)
        self.count += 1

    def writeSheet(self,row,itemlist):
        for colnum in range(len(itemlist)):
            self.sheet.write(row,colnum,itemlist[colnum])
	        
    def hasSheet(self):
        if 0 != self.count:
            return True
        else:
            return False
    def getSheet(self,sheetIndex):
        self.sheet = self.workbook.get_sheet(sheetIndex)
	    
    def saveExcel(self,fileName):
        self.workbook.save(fileName)


def matchString(parttern, str):
    match = parttern.search(str)
    if match:
        return match.group(1)
    return ""


if __name__ == "__main__":
    print("Analyze start!")
    
    compareFileName = "Angola_stringID_compare.xls"
    outFileName = "Angola_stringID_out.xls"

    compareBook = EasyExcel(compareFileName)
    cmpSheet = compareBook.setSheet("Diffent_all_languages")

    stringIDOutBook = EasyExcel(outFileName)

    diffExcel = NewExcel()

    for languageStringID in cmpSheet.row_values(0):
        print(languageStringID)
        if -1 != languageStringID.find("--"):
            parttern = re.compile(r'(\w+)--')
            language = matchString(parttern, languageStringID)
            listToWrite = ["XML_ID","String_ID","Language_content","XML_content"]
            diffExcel.addSheet(language)
            print(language)
            diffExcel.writeSheet(0, listToWrite)
            index = 1
            for XML_id in cmpSheet.col_values(0):
                StringID = cmpSheet.cell_value(index, 1)
                outSheet = stringIDOutBook.setSheet('en')
                outRowIndex = 1
                idIndex = outSheet.col_values(0).index(XML_id)
                
                XML_content = outSheet.cell_value(idIndex, 2)
                outSheet = stringIDOutBook.setSheet(language)

                idIndex = outSheet.col_values(0).index(XML_id)
                StringID_content = outSheet.cell_value(idIndex, STRING_ID_OUT[LANGUAGES_MATCH[language]])
                        
                listToWrite = [XML_id,StringID,StringID_content,XML_content]
                diffExcel.writeSheet(index, listToWrite)
                index += 1

    diffExcel.saveExcel("diff.xls")

   




