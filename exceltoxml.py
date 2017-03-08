#! /usr/bin/env python
#encoding=utf-8

import sys
import os
import xlrd
import re
import xml.dom.minidom


LANGUAGES_TYPE = ["en","th","pt","es","zh-cn"]

ATTRIBUTES_TYPE = ["id","paramcount","order","visability","content","content_spell"]

NODES_TYPE = ["prompt","hint","unit","source","phonetype"]

FATHER_NODE = ["prompts","hintscategory","category","units","sources","phonetypes"]

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

def createNode(attrContentList, nodeType):
  # re: parttern
  patS = re.compile(r'%s')
  patID = re.compile(r'_(.+)')

  node = doc.createElement(nodeType)
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

  return node

if __name__ == "__main__":

  #creat document
  doc = xml.dom.minidom.Document() 
  #creat the root
  root = doc.createElement('config_sds_prompts') 
  #add this root to the document
  doc.appendChild(root)
  
  fileName = "Angola_stringID_out.xls"
  sheetName = "en"

  #read the excel and locate the sheet
  excelForPrompts = EasyExcel(fileName)
  sheet = excelForPrompts.setSheet(sheetName)

  
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
    valueID = sheet.cell_value(indexRow, 0)
    valueContent = sheet.cell_value(indexRow, 2)
    valueOrder = sheet.cell_value(indexRow, 8)
    valueVisability = sheet.cell_value(indexRow, 9)
    valueContentSpell = sheet.cell_value(indexRow, 10)
    attrContentList = [valueID,valueContent,valueOrder,valueVisability,valueContentSpell]
    
    # accord to the type of node, to create corresponding node
    if -1 != valueID.find(NODES_TYPE[0]):
      nodePrompt = createNode(attrContentList, NODES_TYPE[0])
      nodePrompts.appendChild(nodePrompt)
    elif -1 != valueID.find(NODES_TYPE[1]):
      if -1 != valueID.find(NODES_TYPE[1]+'_0'):
        nodeCategory = doc.createElement(FATHER_NODE[2])
        nodeHints.appendChild(nodeCategory)
      nodeHint = createNode(attrContentList, NODES_TYPE[1])
      nodeCategory.appendChild(nodeHint)
    elif -1 != valueID.find(NODES_TYPE[2]):
      nodeUnit = createNode(attrContentList, NODES_TYPE[2])
      nodeUnits.appendChild(nodeUnit)
    elif -1 != valueID.find(NODES_TYPE[3]):
      nodeSource = createNode(attrContentList, NODES_TYPE[3])
      nodeSources.appendChild(nodeSource)
    elif -1 != valueID.find(NODES_TYPE[4]):
      nodePhonetype = createNode(attrContentList, NODES_TYPE[4])
      nodePhonetypes.appendChild(nodePhonetype)

    indexRow += 1

  #create xml
  fp = open('config_sds_prompts.xml', 'w')
  doc.writexml(fp, addindent='\t', newl='\n', encoding="utf-8")
  fp.close()
  



  

 
