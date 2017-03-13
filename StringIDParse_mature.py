#! /usr/bin/env python
#encoding=utf-8
 
import os

#3.x 与 2.x变化比较大
#2.x
#import sys
#reload（sys）
#sys.setdefaultencoding('utf8')

import imp
import sys  
imp.reload(sys)  

import codecs
import xml.etree.ElementTree as ET
import re
import xlrd
import xlwt
from bs4 import BeautifulSoup


# string table index
APP_TYPE = 3
APP_NAME = 4
STRING_ID = 6
ORIGINAL_STR = 10
STATUS = 11
UK_ENGLISH_FULL = 15
THAI_FULL = 20
BAHASA_INDONESIA_FULL = 25
MALAY_FULL = 30
PORTUGUESE_FULL = 35
SPANISH_FULL = 40
VIETNAMESE_FULL = 45
ARABIC_FULL = 50
MANDARIN_FULL = 55


# cmd excel index
CMD_TYPE = 0
CMD_UK_ENGLISH_STR = 1
CMD_MANDARIN_STR = 2
CMD_ARGENTINA_SPANISH_STR = 3
CMD_BRAZIL_PORTUGUESE_STR = 4
CMD_THAI_STR = 5

uk_english = 0
thai = 1
bahasa_indonesia = 2
malay = 3
portuguese = 4
spanish = 5
vietnamese = 6
arabic = 7
mandarin = 8

LANGUAGES_TYPE = [
    "en",
    "th",
    "pt",
    "es",
    "zh-cn"]

XML_LABLE = ["prompt","hint","unit","source","phonetype"]

SPECIAL_CONTENT = "Not to match"

#newSheetItem = ["XML_id","String ID","XML_content",""]

DATAFLIE = ["data avx","data id","data in","data my","data pk","data th","data sg","data vn"]


#对应out表en中的列
STRING_ID_OUT = {"en":3,"th":4,"pt":5,"es":6,"zh-cn":7}

LANGUAGES_MATCH = {"en":"UK English-Full",
    "th":"Thai-Full",
    "pt":"Portuguese_Full",
    "es":"Spanish_full",
    "zh-cn":"Mandarin_Full"}

AREA_ITEM = [
    "Angola",
    "Argentina",
    "Bahrain",
    "Botswana",
    "Brazil",
    "Brunei",
    "Cook Island",
    "Default",
    "Fiji",
    "India",
    "Indonesia",
    "Jordan",
    "Kenya",
    "Kuwait",
    "Lebanon",
    "Lesotho",
    "Malaysia",
    "Mozambique",
    "Nambia",
    "Namibia",
    "New Caledonia",
    "Oman",
    "P.N.Guinea",
    "Philippines",
    "Qatar",
    "Saudi Arabi",
    "Singapore",
    "Solomon Island",
    "South Africa",
    "Swaziland",
    "Tahiti",
    "Thailand",
    "Tonga",
    "U.A.E",
    "Vanuatu",
    "Vietnam",
    "W.Samoa",
    "Zambia",
    "Zimbabwe",
    "pakistan"]

class LanguageGather:
    def __init__(self,
            xml_id,
            string_id,
            xml_content):
        
        self.liststring = []

        self.xml_id = xml_id
        self.liststring.append(xml_id)
        
        self.string_id = string_id
        self.liststring.append(string_id)

        self.xml_content = xml_content
        self.liststring.append(xml_content)
        
    
    def printinfo(self):
        
        print(self.xml_id)
        print(self.string_id)
        print(self.xml_content) 
        print("*" * 12)
        pass

    def getString(self):
        return self.liststring



class EasyExcel:
    '''
    Some convenience methods for Excel documents accessed
    through COM.
    '''
    def __init__(self, matchFileName, matchSheetName):
        if matchFileName:
            self.filename = matchFileName
            
            try:
                self.xlBook = xlrd.open_workbook(matchFileName)
            except Exception as e:
                print(e)
                print ('Open file error')
            self.cursheet = self.xlBook.sheet_by_name(matchSheetName)
        else:
            pass

    def getCurrentSheet(self):
        return self.cursheet
    
    def setSheet(self,matchSheetName):
        self.cursheet = self.xlBook.sheet_by_name(matchSheetName)
        
    def searchStringID(self,contentStr,lanuageStr,xml_id,xmlOrignalContent,exsitSheet):
        
        #第一行字段，忽略
        index = 2
        elementEmpty = LanguageGather("","","")
        flage = True  # only save the content once
        tempElementList = []
        tempStringID = ""
        
        while index < self.cursheet.nrows:
            string_id = str(self.cursheet.cell_value(index,STRING_ID))
            app_name = str(self.cursheet.cell_value(index,APP_NAME))
            uk_english_full = str(self.cursheet.cell_value(index,UK_ENGLISH_FULL))
            uk_english_full = uk_english_full.strip()
            thai_full = str(self.cursheet.cell_value(index,THAI_FULL))
            thai_full = thai_full.strip()
            portuguese_full = str(self.cursheet.cell_value(index,PORTUGUESE_FULL))
            portuguese_full = portuguese_full.strip()
            spanish_full = str(self.cursheet.cell_value(index,SPANISH_FULL))
            spanish_full = spanish_full.strip()
            mandarin_full = str(self.cursheet.cell_value(index,MANDARIN_FULL))
            mandarin_full = mandarin_full.strip()
            
            #orignal_str = str(self.cursheet.cell_value(index,ORIGINAL_STR))
            if "en" == lanuageStr:
                orignalStr = uk_english_full
            elif "th" == lanuageStr:
                orignalStr = thai_full
            elif "pt" == lanuageStr:
                orignalStr = portuguese_full
            elif "es" == lanuageStr:
                orignalStr = spanish_full
            elif "zh-cn" == lanuageStr:
                orignalStr = mandarin_full
            else:
                break

            if len(orignalStr) == len(contentStr) and -1 != orignalStr.find(contentStr):
                #print(uk_english_full)
                #print(contentStr)
                
                status = self.cursheet.cell_value(index,STATUS)
                if -1 == status.find("Delete"):                # and "VR" == app_name:
                    
                    #element = LanguageGather(xml_id,string_id,xml_orignal_content,contentStr)
                    if "" != string_id and -1 == tempStringID.find(string_id):
                        tempStringID = tempStringID + "/"  + string_id

                    #表示找到匹配成功后，就将相关内容append保存，之后设置为flage为flase
                    if flage:
                        tempElementList.append(xml_id)
                        tempElementList.append(xmlOrignalContent)
                        flage = False
            index += 1

        if False == flage:
            tempStringID = tempStringID.strip()
            tempStringID = tempStringID.strip("/")
            element = LanguageGather(tempElementList[0],tempStringID,tempElementList[1])
            lisStr  = element.getString()
            return lisStr

        element = LanguageGather(xml_id,SPECIAL_CONTENT,xmlOrignalContent)
        lisStr  = element.getString()

        return lisStr
    
    def searchCmdType(self,contentStr,lanuageStr,xml_id,xmlOrignalContent,exsitSheet):
        
        #第一行是字段，忽略
        index = 2

        elementEmpty = LanguageGather("","","")
        flage = True
        tempElementList = []
        tempStringID = ""
        
        index = 2
        while index < self.cursheet.nrows:
            cmdType = str(self.cursheet.cell_value(index,CMD_TYPE))
            uk_english_str = str(self.cursheet.cell_value(index,CMD_UK_ENGLISH_STR))
            uk_english_str = uk_english_str.strip()
            thai_str = str(self.cursheet.cell_value(index,CMD_THAI_STR))
            thai_str = thai_str.strip()
            portuguese_str = str(self.cursheet.cell_value(index,CMD_BRAZIL_PORTUGUESE_STR))
            portuguese_str = portuguese_str.strip()
            spanish_str = str(self.cursheet.cell_value(index,CMD_ARGENTINA_SPANISH_STR))
            spanish_str = spanish_str.strip()
            mandarin_str = str(self.cursheet.cell_value(index,CMD_MANDARIN_STR))
            mandarin_str = mandarin_str.strip()
            
            if "en" == lanuageStr:
                orignalStr = uk_english_str
            elif "th" == lanuageStr:
                orignalStr = thai_str
            elif "pt" == lanuageStr:
                orignalStr = portuguese_str
            elif "es" == lanuageStr:
                orignalStr = spanish_str
            elif "zh-cn" == lanuageStr:
                orignalStr = mandarin_str
            else:
                break
                
            if len(orignalStr) == len(contentStr) and -1 != orignalStr.find(contentStr):
         
                if "" != cmdType and -1 == tempStringID.find(cmdType):
                    tempStringID = tempStringID + "/"  + cmdType
                if flage:
                    tempElementList.append(xml_id)
                    tempElementList.append(xmlOrignalContent)
                    flage = False
                
            index += 1
        if False == flage:
            tempStringID = tempStringID.strip()
            tempStringID = tempStringID.strip("/")
            element = LanguageGather(tempElementList[0],tempStringID,tempElementList[1])
            lisStr = element.getString()
            return lisStr
        
        element = LanguageGather(xml_id,SPECIAL_CONTENT,xmlOrignalContent)
        lisStr  = element.getString()
        return lisStr

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
            #if 0 == row:
            #    self.sheet.Cells(row,colnum).Interior.ColorIndex = 3
    def hasSheet(self):
        if 0 != self.count:
            return True
        else:
            return False
    def getSheet(self,sheetIndex):
        self.sheet = self.workbook.get_sheet(sheetIndex)
        
    def saveExcel(self,fileName):
        self.workbook.save(fileName)

def matchStringID(newSheetItem,specFile,countryName):
    exsitSheet = []
    
    #deal with the different languages
    for sheetName in LANGUAGES_TYPE:
        xmlFile = specFile + "/" + "config" + "/" + countryName + "/" + sheetName + "/" + "config_sds_prompts.xml"
        
        #if it exists, then do 
        if os.path.exists(xmlFile):
            exsitSheet.append(sheetName)
        
            analyzeExcel.addSheet(sheetName)

            newSheetItem.append("order")
            newSheetItem.append("visability")
            newSheetItem.append("content_spell")
            analyzeExcel.writeSheet(0, newSheetItem)
            cmopare_sds_prompt_to_excel(xmlFile, sheetName, exsitSheet)
            newSheetItem.pop()
            newSheetItem.pop()
            newSheetItem.pop()
            print("###" + sheetName + "###")
    return exsitSheet

def searchString(pattern, lineStr):
    match = pattern.search(str(lineStr))
    if match:
        return match.group(1)
    return ""
                    
def cmopare_sds_prompt_to_excel(xmlFile,lanuageStr,exsitSheet):
    
    index = 1
    sdsFile = codecs.open(xmlFile,'rb',"utf-8")

    #get the line
    soup = BeautifulSoup(sdsFile,"html.parser")
    #sdsLine = sdsFile.readlines()

    #以content关键字作为find目标
    numInsertIndex = 1
    LinesContent = soup.find_all(content = True)

    patC = re.compile(r'chong2');
    for lineStr in LinesContent:

        xmlContent = lineStr["content"]
        xmlContent = str(xmlContent)
        
        xmlContent = xmlContent.strip()
        xmlOrignalContent = xmlContent

        xmlID = lineStr["id"]
        xmlID = str(xmlID)

        if "0" == xmlID:
            numInsertIndex += 1 
        
        #order、visability和content_spell字段内容获取
        pattern = re.compile(r'order="(\w+)"')
        xmlOrder = searchString(pattern, lineStr)

        pattern = re.compile(r'visability="(\w+)"')
        xmlVisability = searchString(pattern, lineStr)

        pattern = re.compile(r'content_spell="(.+)"\s')
        xmlContentSpell = searchString(pattern, lineStr)

        #识别type
        pattern = re.compile(r'<(\w+)')
        nodeType = searchString(pattern, lineStr)
        if nodeType == XML_LABLE[1]:
            xmlID = nodeType + str(numInsertIndex-1) + "_" + xmlID
        else:
            xmlID = nodeType + "_" + xmlID
            
        xmlContent = patC.sub('重', xmlContent)
        TempLineStr = str(lineStr)
       
        if nodeType == XML_LABLE[0]:
            listStr = stringIDExcel.searchStringID(xmlContent,lanuageStr,xmlID,xmlOrignalContent,exsitSheet)
        else:
            listStr = comCmdListExcel.searchCmdType(xmlContent,lanuageStr,xmlID,xmlOrignalContent,exsitSheet)
            
        listStr.append(xmlOrder)
        listStr.append(xmlVisability)
        listStr.append(xmlContentSpell)
        if "" != listStr[0]:
            analyzeExcel.writeSheet(index,listStr)
            index += 1

    sdsFile.close()


if __name__ == "__main__":
    print("Analyze start!")
    print("please input one of the [data avx | data id | data in | data my | data pk | data th | data sg | data vn], which you will deal with!!")
    #current_dir = cur_file_dir()
    #print (current_dir)
    
    countryList = AREA_ITEM
    
    specFile = input("input the root-file:")
    newFile = ''.join(specFile.split()) + "Excel"

    if os.path.exists(newFile):
        pass
    else:
        os.makedirs(newFile)

    '''
    countryList = []
    while True:
        input_country = input("input the country file in your current path or input 'end' to end:\n")
        if input_country == "end":
            break
        else:
            countryList.append(input_country)
    '''
    # open the excel and match the string
    stringIDFileName = "16cyTMAP_StringID.xlsx"
    stringIDSheetName = 'Text'
    stringIDExcel = EasyExcel(stringIDFileName,stringIDSheetName)
    comCmdFileName = "16cyTMAP_func_8_02_VoiceRecog_CommandList.xlsx"
    comCmdSheetName = "8.02.3 Common Command List"
    comCmdListExcel = EasyExcel(comCmdFileName,comCmdSheetName)

    for countryName in countryList:
        print("*******" + countryName + "*********")
        newSheetItem = ["XML_id","String ID","XML_content"]
        analyzeExcel = NewExcel()
        exsitSheet = matchStringID(newSheetItem,specFile,countryName)

        fileName = newFile + '/' + countryName + "_" +  "stringID_out.xls"
        if os.path.exists(fileName):
            os.remove(fileName)
            
        if 0 != len(exsitSheet):
            analyzeExcel.saveExcel(fileName)
        else:
            print("No this *config*.xls")

