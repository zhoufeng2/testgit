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
            xml_content,
            orignalstr):
        
        self.liststring = []

        self.xml_id = xml_id
        self.liststring.append(xml_id)
        
        self.string_id = string_id
        self.liststring.append(string_id)

        self.xml_content = xml_content
        self.liststring.append(xml_content)
        
        self.orignalstr = orignalstr
        self.liststring.append(orignalstr)
    
    def printinfo(self):
        
        print(self.xml_id)
        print(self.string_id)
        print(self.xml_content) 
        print(self.orignalstr)   
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
        elementEmpty = LanguageGather("","","","")
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
                        tempElementList.append(contentStr)
                        tempElementList.append(thai_full)
                        tempElementList.append(portuguese_full)
                        tempElementList.append(spanish_full)
                        tempElementList.append(mandarin_full)
                        flage = False
                #return element

                #else:
                #   print("Deleted")
                #    return elementEmpty
                
            index += 1

        if False == flage:
            tempStringID = tempStringID.strip()
            tempStringID = tempStringID.strip("/")
            element = LanguageGather(tempElementList[0],tempStringID,tempElementList[1],tempElementList[2])
            lisStr  = element.getString()
            if 1 == len(exsitSheet):
                lisStr.append(tempElementList[3])
                lisStr.append(tempElementList[4])
                lisStr.append(tempElementList[5])
                lisStr.append(tempElementList[6])
            return lisStr
        
       # print(contentStr)
        element = LanguageGather(xml_id,"SPECIAL_CONTENT",xmlOrignalContent,"SPECIAL_CONTENT")
        lisStr  = element.getString()
        if 1 == len(exsitSheet):
            lisStr.append(4*"")
       # print(5*"*")
        
        return lisStr
    
    def searchCmdType(self,contentStr,lanuageStr,xml_id,xmlOrignalContent,exsitSheet):
        
        #第一行是字段，忽略
        index = 2

        elementEmpty = LanguageGather("","","","")
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
                    tempElementList.append(contentStr)
                    tempElementList.append(thai_str)
                    tempElementList.append(portuguese_str)
                    tempElementList.append(spanish_str)
                    tempElementList.append(mandarin_str)
                    flage = False
                
            index += 1
        if False == flage:
            tempStringID = tempStringID.strip()
            tempStringID = tempStringID.strip("/")
            element = LanguageGather(tempElementList[0],tempStringID,tempElementList[1],tempElementList[2])
            lisStr = element.getString()
            if 1 == len(exsitSheet):
                lisStr.append(tempElementList[3])
                lisStr.append(tempElementList[4])
                lisStr.append(tempElementList[5])
                lisStr.append(tempElementList[6])
            return lisStr
        
        element = LanguageGather(xml_id,"SPECIAL_CONTENT",xmlOrignalContent,"SPECIAL_CONTENT")
        lisStr  = element.getString()
        if 1 == len(exsitSheet):
            lisStr.append(4*"")
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
            newSheetItem.pop()
            newSheetItem.append(LANGUAGES_MATCH[sheetName])
            analyzeExcel.addSheet(sheetName)

            #if it is english 
            if 1 == len(exsitSheet):
                tempItem = newSheetItem[:]
                newSheetItem.append("Thai-Full")
                newSheetItem.append("Portuguese_Full")
                newSheetItem.append("Spanish_full")
                newSheetItem.append("Mandarin_Full")
                newSheetItem.append("order")
                newSheetItem.append("visability")
                newSheetItem.append("content_spell")
                analyzeExcel.writeSheet(0, newSheetItem)
                newSheetItem = tempItem[:]
                cmopare_sds_prompt_to_excel(xmlFile, sheetName, exsitSheet)
            else:
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

def compareStringID(exsitSheet):

    diffStringID = "Diffent_all_languages"
    uniformStringID = "Uniform_all_languages"
    sheetList = [diffStringID,uniformStringID]
    
    compareexcel.addSheet(diffStringID)
    compareexcel.addSheet(uniformStringID)
            
    cursheet = xlBook.sheet_by_name(exsitSheet[0])

    rowNum_diff = 1
    rowNum_uniform = 1
    rowMax = cursheet.nrows
    tempName = exsitSheet[0]
    idNum = 0

    #find the max row in sheet
    for sheetName in exsitSheet:
        cursheet = xlBook.sheet_by_name(sheetName)
        if cursheet.nrows > rowMax:
            rowMax = cursheet.nrows
            tempName = sheetName

    #find the same XML_id and the same StringID and save 
    for index in range(rowMax):
        xml_id_list = []
        currentsheet = xlBook.sheet_by_name(tempName)
        current_xml_id = currentsheet.cell_value(index, 0)
        if 0 == index:
            for sheetName in exsitSheet:
                xml_id_list.append(sheetName + "--String ID")
            
            xml_id_list.insert(0, "XML_id")
            compareexcel.writeSheet(0, xml_id_list)
            
            for sheetName in exsitSheet:
                xml_id_list.append(sheetName)
        
            compareexcel.getSheet(sheetList.index(diffStringID))
            compareexcel.writeSheet(0, xml_id_list)
        else:
            for sheetName in exsitSheet:
                #  check the _out.xls
                cursheet = xlBook.sheet_by_name(sheetName)

                #  
                for rowIter in range(cursheet.nrows):
                    if current_xml_id == cursheet.cell_value(rowIter, 0):
                        xml_id_list.append(cursheet.cell_value(rowIter, 1))
                        break
                if rowIter == (cursheet.nrows -1) and current_xml_id != cursheet.cell_value(rowIter, 0):
                    xml_id_list.append("No this XML_id")

                    
            num = xml_id_list.count(xml_id_list[0])
            indexEn = [idx for idx, strNoMatch in enumerate(xml_id_list) if strNoMatch == "SPECIAL_CONTENT"]
                     
            xml_id_list.insert(0,current_xml_id)
            if 0 != len(indexEn)  or num != len(exsitSheet):
                compareexcel.getSheet(sheetList.index(diffStringID))
                cursheet = xlBook.sheet_by_index(0)
                for indexDiff in range(len(LANGUAGES_TYPE)):
                    if indexDiff in indexEn:
                        xml_id_list.append(cursheet.cell_value(index,STRING_ID_OUT[exsitSheet[indexDiff]]))
                    else:
                        xml_id_list.append("")
                compareexcel.writeSheet(rowNum_diff,xml_id_list)
                rowNum_diff += 1
            else:
                compareexcel.getSheet(sheetList.index(uniformStringID))
                compareexcel.writeSheet(rowNum_uniform,xml_id_list)
                rowNum_uniform += 1


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
        newSheetItem = ["XML_id","String ID","XML_content",""]
        analyzeExcel = NewExcel()
        exsitSheet = matchStringID(newSheetItem,specFile,countryName)

        fileName = newFile + '/' + countryName + "_" +  "stringID_out.xls"
        if os.path.exists(fileName):
            os.remove(fileName)
            
        if 0 != len(exsitSheet):
            analyzeExcel.saveExcel(fileName)
            
            # xlBook = xlrd.open_workbook(fileName)
            # compareexcel = NewExcel()
            # compareStringID(exsitSheet)
            # fileName = newFile + '/' + countryName + "_" +  "stringID_compare.xls"
            # if os.path.exists(fileName):
            #     os.remove(fileName)
            # compareexcel.saveExcel(fileName)   
        else:
            print("No this *config*.xls")

