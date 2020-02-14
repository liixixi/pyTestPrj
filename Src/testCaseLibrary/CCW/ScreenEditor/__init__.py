
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

    panelDeviceInfoColumnTitle = ['ID', 'Name', 'Type', 'X', 'Y', 'Height', 'Width', 'Notes']

    import utilities
    panelDeviceInfoList = utilities.excelReader.loadWorkBook("Sample.xlsx", panelDeviceInfoColumnTitle)

    for paneldevice in panelDeviceInfoList:
        CreatePanelDevice(paneldevice['X'], paneldevice['Y'], paneldevice['Height'], paneldevice['Width'], paneldevice['Type'])

    for paneldevice in panelDeviceInfoList:
        pass
        VerifyPanelDeviceCreated(paneldevice['X'], paneldevice['Y'], paneldevice['Height'], paneldevice['Width'], paneldevice['Type'])    

    pass

CreateAllPanelDevice()