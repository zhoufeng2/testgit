#! /usr/bin/env python
#encoding=utf-8

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

KEY_WORD = "Not to match"

EXCEL_FIELD = {"XML_ID":0,"StringID":1,"XML_content":2}

OUT_EXCEL = "_stringID_out.xls"

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
    def setSheetbyID(self, index):
        return self.xlBook.sheet_by_index(index)

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

def diffExcel(fileName, area, fileDir):
    stringIDOutBook = EasyExcel(fileName)
    diffExcel = NewExcel()
    for sheetName in stringIDOutBook.getSheets():
    
        listToWrite = ["XML_ID","StringID",LANGUAGES_MATCH[sheetName.name],"XML_content"]
        diffExcel.addSheet(sheetName.name)
        diffExcel.writeSheet(0, listToWrite)
        outSheet = stringIDOutBook.setSheet(sheetName.name)

        index = 1
        notMatchIndex = 0
        for NotMatch in outSheet.col_values(1):
            
            if NotMatch == KEY_WORD:
                XML_id = outSheet.cell_value(notMatchIndex, EXCEL_FIELD["XML_ID"])
                XML_content = outSheet.cell_value(notMatchIndex, EXCEL_FIELD["XML_content"])

                # the first sheet is basic
                outSheet = stringIDOutBook.setSheetbyID(0)
                try:
                    idIndex = outSheet.col_values(0).index(XML_id)
                    StringID = outSheet.cell_value(idIndex, EXCEL_FIELD["StringID"])
                    StringID_content = outSheet.cell_value(idIndex, STRING_ID_OUT[LANGUAGES_MATCH[sheetName.name]])
                except Exception:
                    StringID = KEY_WORD
                    StringID_content = KEY_WORD

                outSheet = stringIDOutBook.setSheet(sheetName.name)
                if -1 == XML_content.find("n=spell"):
                    listToWrite = [XML_id,StringID,StringID_content,XML_content]
                    diffExcel.writeSheet(index, listToWrite)
                    index += 1
            notMatchIndex += 1
    diffExcel.saveExcel(fileDir + "/" + area + "_diff.xls")
    print("*** " +  area + " *** is ok")
    
if __name__ == "__main__":
    print("Analyze start!")

    specFile = input("input the Excel-file:")
    specFile = ''.join(specFile.split())
    fileDir = specFile +"Excel"

    if os.path.exists(fileDir):
        for area in AREA_ITEM:
            fileName = fileDir + "/" + area + OUT_EXCEL
            if os.path.exists(fileName):
                diffExcel(fileName, area, fileDir)
            #else:
                #print("***No " + area + " excel***")
    else:
        print("***No " + fileDir + " directory***")
          
        
        

   




