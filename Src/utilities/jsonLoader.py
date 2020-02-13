
def CreateObject(data, name=''):
    obj = type(name, (object,), data)
    for a in dir(obj):
        if a.startswith('__'):
            continue
        if (type(getattr(obj, a)) == type([])):
            setattr(obj, a, CreateList(getattr(obj, a), name))
    return  obj

def CreateList(data, name=''):
    retList = []
    for d in data:
        if (type(d) == type({})):
             retList.append(CreateObject(d,name))
        if (type(d)) == type([]):
            retList.append(CreateList(d,name))
        if (type(d) == type('')): 
            retList.append(d)

    return retList

#basic test of this module
if (__name__ == '__main__'):
    import json
    with open(r'Src\utilities\test.json') as json_file:
        data = json.load(json_file)

    root = 1
    if (type(data) == type([])):
        root = CreateList(data)
    else:
        root = CreateObject(data, 'test')

    print(root)

