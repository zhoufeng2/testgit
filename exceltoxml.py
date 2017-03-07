#! /usr/bin/env python
#encoding=utf-8

import sys
import os
import xlrd
from xml.dom.minidom import Document

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

if __name__ == "__main__":

  #在内存中创建一个空的文档
  doc = Document() 
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
  nodeCategory = doc.createElement('category')
  nodeHints.appendChild(nodeCategory)

  nodeUnits = doc.createElement('units')
  root.appendChild(nodeCategory) 

  nodeSource = doc.createElement('sources')
  root.appendChild(nodeSource)

  nodePhonetypes = doc.createElement('phonetypes')
  root.appendChild(nodePhonetypes)
  
  #create the child element and attribute
  indexRow = 2
  nodePrompt = doc.createElement('prompt')
  nodeHint = doc.createElement('hint')
  nodeUnit = doc.createElement('unit')
  nodeSource = doc.createElement('source')
  nodePhonetype = doc.createElement('phonetype')
  
  while indexRow < sheet.nrows:
    
    #traverse the specific column:
    if find the prompt in the XML_id:
      nodeName = nodePrompt.setAttribute('id', sheet.cell_value(indexRow, 0))
      nodeName = nodePrompt.setAttribute('paramcount', accord to the content's %s)
      if include the %s more than 2:
        nodeName = nodePrompt.setAttribute('order', "12")

      nodeName = nodePrompt.setAttribute('content', sheet.cell_value(indexRow, 2))
      nodePrompts.appendChild(nodePrompt)

    if find the hint in the XML_id:
      nodeName = nodeHint.setAttribute('id', sheet.cell_value(indexRow, 0))

      if the content has the attribute of visability:
        nodeName = nodeHint.setAttribute('visability', 'yes')

      nodeName = nodeHint.setAttribute('content', sheet.cell_value(indexRow, 2))
      nodeCategory.appendChild(nodeHint)

    if find the unit in the XML_id:
      nodeName = nodeUnit.setAttribute('id', sheet.cell_value(indexRow, 0))
      nodeName = nodeUnit.setAttribute('content', sheet.cell_value(indexRow, 2))
      nodeUnits.appendChild(nodeHint)

    if find the source in the XML_id:
      nodeName = nodeSource.setAttribute('id', sheet.cell_value(indexRow, 0))
      nodeName = nodeSource.setAttribute('content', sheet.cell_value(indexRow, 2))
      nodeSources.appendChild(nodeSource)

    if find the phonetype in the XML_id:
      nodeName = nodePhonetype.setAttribute('id', sheet.cell_value(indexRow, 0))
      nodeName = nodePhonetype.setAttribute('content', sheet.cell_value(indexRow, 2))
      nodePhonetypes.appendChild(nodePhonetype)

    indexRow += 1
  
  #create xml
  fp = open('config_sds_prompts.xml', 'w')
  doc.writexml(fp, addindent='\t', newl='\n', encoding="utf-8")
  fp.close()
  



  

 
