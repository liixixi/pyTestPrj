
def CreatePanelDevice(x,y,height,width,type):
    pass


def VerifyPanelDeviceCreated(x,y,height, width,type):
    pass


def CreateANewProject():
    import utilities
    utilities.WindowsShell.OpenCCW()

    import testCaseLibrary
    testCaseLibrary.CCW.Menu.newProject(addDevice=False)

    testCaseLibrary.CCW.catalogService.AddDevice('2711R-T10T')

    testCaseLibrary.CCW.projectOrganizer.CreatePV800Project()
    pass

def CloseCCW():
    import testCaseLibrary
    testCaseLibrary.CCW.close()
    pass


def CreateAllPanelDevice():
    import testCaseLibrary
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_1')

    # for paneldevice in list:
    #    CreatePanelDevice(paneldevice.get('x'),y, height, witdth, 'Text')

    # for paneldevice in list:
    #    VerifyPanelDeviceCreated(x,y, height, witdth, 'Text')    

    pass