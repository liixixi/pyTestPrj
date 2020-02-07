
def CreateObject(data):
    obj = type('', (object,), data)
    for a in dir(obj):
        if a.startswith('__'):
            continue
        if (type(getattr(obj, a)) == type([])):
            setattr(obj, a, CreateList(getattr(obj, a)))
    return  obj

def CreateList(data):
    retList = []
    for d in data:
        if (type(d) == type({})):
             retList.append(CreateObject(d))
        if (type(d)) == type([]):
            retList.append(CreateList(d))
        if (type(d) == type('')): 
            retList.append(d)

    return retList

if (__name__ == '__main__'):
    import json
    with open(r'Src\utilities\test.json') as json_file:
        data = json.load(json_file)

    root = 1
    if (type(data) == type([])):
        root = CreateList(data)
    else:
        root = CreateObject(data)

    print(root)

