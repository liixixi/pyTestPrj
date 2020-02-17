
def generatenamelist(jsonObject):

    targetList = []
    for subObject in jsonObject:
        targetList.append(subObject.name)
    
    return targetList
    

