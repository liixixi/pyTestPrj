from openpyxl import load_workbook 

def loadWorkBook(name):

    workbook = load_workbook(filename="sample.xlsx")
    sheet = workbook.active

    titleRowNumber = findTitleRow(sheet)

    colCount = getColCount(sheet, titleRowNumber)

def getColCount(sheet, titleRowNumber):
    #for i in range (1, 1000):
     #   if (sheet.)
     pass

def findTitleRow(sheet):

    for i in range(1, 1000):
        if (sheet['A' + str(i)].value != None):
            return i