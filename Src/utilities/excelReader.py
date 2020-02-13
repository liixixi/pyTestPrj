from openpyxl import load_workbook 

def loadWorkBook(name):

    workbook = load_workbook(filename=name)
    sheet = workbook.active

    maxRow = sheet.max_row
    titleRowNumber = findTitleRow(sheet, 'ID')

    dataList = obtainDataList(sheet, maxRow, titleRowNumber)
    
    return dataList

def findTitleRow(sheet, title):

    for i in range(1, 1000):
        if (sheet['A' + str(i)].value == title):
            return i

def obtainDataList(sheet, maxRow, startRow):
    
    dataList = []
    for row in range(startRow + 1, maxRow + 1):
        subDataDict = {}
        subDataDict['ID'] = sheet.cell(row,1).value
        subDataDict['Name'] = sheet.cell(row,2).value
        subDataDict['Type'] = sheet.cell(row,3).value
        subDataDict['X'] = sheet.cell(row,4).value
        subDataDict['Y'] = sheet.cell(row,5).value
        subDataDict['Height'] = sheet.cell(row,6).value
        subDataDict['Width'] = sheet.cell(row,7).value
        subDataDict['Notes'] = sheet.cell(row,8).value
        dataList.append(subDataDict)
    
    return dataList


# datalist = loadWorkBook("C:/Users/Iwang1/Desktop/Sample.xlsx")
