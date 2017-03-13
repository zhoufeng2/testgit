#! /usr/bin/env python
#encoding=utf-8

# version2..7+
import sys

if "2" == sys.version[0:1]:
  reload(sys)
  sys.setdefaultencoding('utf-8')

import os
import xlrd
import re
import codecs

LANGUAGES_TYPE = ["en","th","pt","es","zh-cn"]

ATTRIBUTES_TYPE = ["id","paramcount","order","visability","content","content_spell"]

NODES_TYPE = ["prompt","hint","unit","source","phonetype"]

FATHER_NODE = ["prompts","hintscategory","category","units","sources","phonetypes","config_sds_prompts"]

INPUT_EXCEL = "_stringID_out.xls"

OUT_CONFIG_NAME = "config_sds_prompts"

EXCEL_FIELD = {"XML_id":0,"StringID":1,"content":2,"order":3,"visability":4,"content_spell":5}

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

  def getSheets(self):
    return self.xlBook.sheets()


class ExcelToXML:
  """docstring for ExcelToXML"""
  def __init__(self, inputFileName, outFlieDir):
    self.inputFileName = inputFileName
    self.outFlieDir = outFlieDir
    
  def setNodeAttribute(self, attrContentList, nodeType, node):
    # re: parttern
    patS = re.compile(r'%s')
    patID = re.compile(r'_(.+)')

    #  find the number of %s
    listMatch = patS.findall(attrContentList[1])
    if "" == len(listMatch):
      paraNum = 0
    else:
      paraNum = len(listMatch)

    #  set the id 
    node.setAttribute(ATTRIBUTES_TYPE[0], matchString(patID, attrContentList[0]))

    #  set the attribute, when it is at prompt
    if nodeType == NODES_TYPE[0]:
      #  set the paramcount
      node.setAttribute(ATTRIBUTES_TYPE[1], str(paraNum))
      if "" != attrContentList[2]:
        #  set the order
        node.setAttribute(ATTRIBUTES_TYPE[2], attrContentList[2])
      #  set the content
      node.setAttribute(ATTRIBUTES_TYPE[4], attrContentList[1])
    else:
      #  set the visability    
      if "" != attrContentList[3]:
        node.setAttribute(ATTRIBUTES_TYPE[3], attrContentList[3])
      #  set the content
      node.setAttribute(ATTRIBUTES_TYPE[4], attrContentList[1])
      #  set the content_spell
      if "" != attrContentList[4]:
        node.setAttribute(ATTRIBUTES_TYPE[5], attrContentList[4])

  def createXML(self):
    import xml.dom.minidom
    #read the excel and locate the sheet
    excelForPrompts = EasyExcel(self.inputFileName)
    for sheetName in excelForPrompts.getSheets():
      sheet = excelForPrompts.setSheet(sheetName.name)

      #creat document
      doc = xml.dom.minidom.Document() 
      #creat the root
      root = doc.createElement(FATHER_NODE[6]) 
      #add this root to the document
      doc.appendChild(root)

      #create the father element
      nodePrompts = doc.createElement(FATHER_NODE[0])
      root.appendChild(nodePrompts);

      nodeHints = doc.createElement(FATHER_NODE[1])
      root.appendChild(nodeHints);

      nodeUnits = doc.createElement(FATHER_NODE[3])
      root.appendChild(nodeUnits) 

      nodeSources = doc.createElement(FATHER_NODE[4])
      root.appendChild(nodeSources)

      nodePhonetypes = doc.createElement(FATHER_NODE[5])
      root.appendChild(nodePhonetypes)
      
      #create the child element and attribute
      indexRow = 1
      while indexRow < sheet.nrows:
        #traverse the specific column:
        valueID = sheet.cell_value(indexRow, EXCEL_FIELD["XML_id"])
        valueContent = sheet.cell_value(indexRow, EXCEL_FIELD["content"])
        valueOrder = sheet.cell_value(indexRow, EXCEL_FIELD["order"])
        valueVisability = sheet.cell_value(indexRow, EXCEL_FIELD["visability"])
        valueContentSpell = sheet.cell_value(indexRow, EXCEL_FIELD["content_spell"])
        attrContentList = [valueID,valueContent,valueOrder,valueVisability,valueContentSpell]
        
        # accord to the type of node, to create corresponding node
        if -1 != valueID.find(NODES_TYPE[0]):
          nodePrompt = doc.createElement(NODES_TYPE[0])
          self.setNodeAttribute(attrContentList, NODES_TYPE[0], nodePrompt)
          nodePrompts.appendChild(nodePrompt)
        elif -1 != valueID.find(NODES_TYPE[1]):
          #  hint id need start from 0
          if -1 != valueID.find('_0'):
            nodeCategory = doc.createElement(FATHER_NODE[2])
            nodeHints.appendChild(nodeCategory)
          nodeHint = doc.createElement(NODES_TYPE[1])
          self.setNodeAttribute(attrContentList, NODES_TYPE[1], nodeHint)
          nodeCategory.appendChild(nodeHint)
        elif -1 != valueID.find(NODES_TYPE[2]):
          nodeUnit = doc.createElement(NODES_TYPE[2])
          self.setNodeAttribute(attrContentList, NODES_TYPE[2], nodeUnit)
          nodeUnits.appendChild(nodeUnit)
        elif -1 != valueID.find(NODES_TYPE[3]):
          nodeSource = doc.createElement(NODES_TYPE[3])
          self.setNodeAttribute(attrContentList, NODES_TYPE[3], nodeSource)
          nodeSources.appendChild(nodeSource)
        elif -1 != valueID.find(NODES_TYPE[4]):
          nodePhonetype = doc.createElement(NODES_TYPE[4])
          self.setNodeAttribute(attrContentList, NODES_TYPE[4], nodePhonetype)
          nodePhonetypes.appendChild(nodePhonetype)

        indexRow += 1
      
      #creat the road to save the file
      fileRoad = self.outFlieDir + '/' + sheetName.name
      if os.path.exists(fileRoad):
          pass
      else:
          os.makedirs(fileRoad)

      #create xml
      fp = codecs.open(fileRoad +  '/' + OUT_CONFIG_NAME + '.xml', 'w', encoding="utf-8")
      doc.writexml(fp, addindent='\t', newl='\n', encoding="utf-8")
      fp.close()

def matchString(parttern, str):
  match = parttern.search(str)
  if match:
    return match.group(1)
  return ""
  

if __name__ == "__main__":

  # traverse the are item
  for area in AREA_ITEM:
    #  match the excel in the current directory
    inputFileName = area + INPUT_EXCEL
    if os.path.exists(inputFileName):
      outFlieDir = 'config' + '/' + area
      xml = ExcelToXML(inputFileName, outFlieDir)
      xml.createXML()
      print("excel-" + area + " is transformed, ok! ")
    #else:
    #  print("******No excel for " + area + " ******")
      
  



  

 
