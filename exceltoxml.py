#! /usr/bin/env python
#encoding=utf-8

import sys
import os
import xlrd
import re
import xml.dom.minidom


LANGUAGE_TYPE = ["en","th","pt","es","zh-cn"]
class EasyExcel:
  """docstring for EasyExcel"""
  def __init__(self, fileName):
    if fileName:
      self.filename = fileName
      
      try:
        self.xlBook = xlrd.open_workbook(fileName)
      except Exception as e:
        print(e)
        print('Open file error')
    else:
      pass

  def setSheet(self, sheetName):
    return self.xlBook.sheet_by_name(sheetName)


def matchString(parttern, str):
  match = parttern.search(str)
  if match:
    return match.group(1)
  return ""

# def addNode(valueID, valueContent):
#    if -1 != valueID.find("prompt"):
#       nodePrompt = doc.createElement('prompt')

#       listMatch = patS.findall(valueContent)
#       if "" == len(listMatch):
#         paraNum = 0
#       else:
#         paraNum = len(listMatch)
      
#       nodePrompt.setAttribute('paramcount', str(paraNum))

#       if "" != sheet.cell_value(indexRow, 8):
#         nodePrompt.setAttribute('order', sheet.cell_value(indexRow, 8))
#       nodePrompt.setAttribute('content', valueContent)
    
#       nodePrompt.setAttribute('id', matchString(patID, valueID))
#       nodePrompts.appendChild(nodePrompt)

if __name__ == "__main__":

  #在内存中创建一个空的文档
  doc = xml.dom.minidom.Document() 
  #创建一个根节点Managers对象
  root = doc.createElement('config_sds_prompts') 

  #将根节点添加到文档对象中
  doc.appendChild(root)
  
  fileName = "excel_for_prompts.xls"
  sheetName = "en"

  #read the excel and locate the sheet
  excelForPrompts = EasyExcel(fileName)
  sheet = excelForPrompts.setSheet(sheetName)

  #create the father element
  nodePrompts = doc.createElement('prompts')
  root.appendChild(nodePrompts);

  nodeHints = doc.createElement('hintscategory')
  root.appendChild(nodeHints);

  nodeUnits = doc.createElement('units')
  root.appendChild(nodeUnits) 

  nodeSources = doc.createElement('sources')
  root.appendChild(nodeSources)

  nodePhonetypes = doc.createElement('phonetypes')
  root.appendChild(nodePhonetypes)
  
  #create the child element and attribute
  indexRow = 1
  patS = re.compile(r'%s')
  patID = re.compile(r'_(\w+)')  
  while indexRow < sheet.nrows:
    
    #traverse the specific column:
    valueID = sheet.cell_value(indexRow, 0)
    valueContent = sheet.cell_value(indexRow, 2)
    valueOrder = sheet.cell_value(indexRow, 8)
    valueVisability = sheet.cell_value(indexRow, 9)
    valueContentSpell = sheet.cell_value(indexRow, 10)

    if -1 != valueID.find("prompt"):
      nodePrompt = doc.createElement('prompt')

      listMatch = patS.findall(valueContent)
      if "" == len(listMatch):
        paraNum = 0
      else:
        paraNum = len(listMatch)
      nodePrompt.setAttribute('paramcount', str(paraNum))
      if "" != sheet.cell_value(indexRow, 8):
        nodePrompt.setAttribute('order', valueOrder)  #en is 8, else is 5
      # if "" != valueVisability:
      #   nodeHint.setAttribute('visability', valueVisability)
      # if "" != valueContentSpell:
      #   nodeHint.setAttribute('content_spell', valueContentSpell)
      nodePrompt.setAttribute('content', valueContent)
      nodePrompt.setAttribute('id', matchString(patID, valueID))

      nodePrompts.appendChild(nodePrompt)
    
    if -1 != valueID.find('hint'):
      if -1 != valueID.find('hint_0'):
        nodeCategory = doc.createElement('category')
        nodeHints.appendChild(nodeCategory)

      nodeHint = doc.createElement('hint')

      nodeHint.setAttribute('id', matchString(patID, valueID))
      if "" != valueVisability:
        nodeHint.setAttribute('visability', valueVisability)
      if "" != valueContentSpell:
        nodeHint.setAttribute('content_spell', valueContentSpell)
      nodeHint.setAttribute('content', valueContent)

      nodeCategory.appendChild(nodeHint)

    if -1 != valueID.find('unit'):
      nodeUnit = doc.createElement('unit')
      nodeUnit.setAttribute('id', matchString(patID, valueID))
      nodeUnit.setAttribute('content', valueContent)
      if "" != valueVisability:
        nodeUnit.setAttribute('visability', valueVisability)
      if "" != valueContentSpell:
        nodeUnit.setAttribute('content_spell', valueContentSpell)
      nodeUnits.appendChild(nodeUnit)

    if -1 != valueID.find('source'):
      nodeSource = doc.createElement('source')
      nodeSource.setAttribute('id', matchString(patID, valueID))
      nodeSource.setAttribute('content', valueContent)
      if "" != valueVisability:
        nodeSource.setAttribute('visability', valueVisability)
      if "" != valueContentSpell:
        nodeSource.setAttribute('content_spell', valueContentSpell)
      nodeSources.appendChild(nodeSource)

    if -1 != valueID.find('phonetype'):
      nodePhonetype = doc.createElement('phonetype')
      nodePhonetype.setAttribute('id', matchString(patID, valueID))
      nodePhonetype.setAttribute('content', valueContent)
      if "" != valueVisability:
        nodePhonetype.setAttribute('visability', valueVisability)
      if "" != valueContentSpell:
        nodePhonetype.setAttribute('content_spell', valueContentSpell)
      nodePhonetypes.appendChild(nodePhonetype)
    
    indexRow += 1
  
  #create xml
  fp = open('config_sds_prompts.xml', 'w')
  doc.writexml(fp, addindent='\t', newl='\n', encoding="utf-8")
  fp.close()
  



  

 
