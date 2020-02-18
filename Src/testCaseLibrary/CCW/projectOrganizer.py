
# open add device dialog
def OpenAddDeviceDialog():
    pass

def removeDevice(deviceName):
    pass

def CreatePV800Project(orientation='Landscape'):
    pass

def OpenScreen(screenName):
    # call taf to open screen

    pass

def IsScreenOpen(screenName):
    # call taf to judge whether screen has opened
    pass
    #return True/Flase

def CreateScreen(count=1):
    pass

def renameScreen(oldName,newName):
    # call taf to rename screen
    pass
    #return True/False

def ChangeGraphicsTerminal(newTerminalType = ''):
    # default get current type first, then change to new type which is different from current type
    currentType = GetGraphicsTerminalType()
    if newTerminalType == '':
        '''if currentType == '2711R-T10T':
            # call taf change type to 2711R-T7T
            pass
        elif currentType == '2711R-T7T':
            # call taf change type to 2711R-T4T
            pass
        elif currentType == '2711R-T4T':
            # call taf change type to 2711R-T10T
            pass'''
        pass
    else:
        pass
    # call taf to change ternimal
    pass

def GetGraphicsTerminalType():
    # call taf to get terminal type
    pass
    #return terminal type 

def Upload(applicationName=''):

    pass

def CancelUpload():

    pass

def ConfirmUpload():

    pass

def Validate():

    pass

def Download():

    pass

def IsBlink():

    pass