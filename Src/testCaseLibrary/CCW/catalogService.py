
def AddDevice(catalog):
    SelectDevice(catalog)
    DoAddDevice()

def SelectDevice(catalog):
    # call taf workflow
    pass

def DoAddDevice():
    # call taf workflow
    pass 

def closeAddDeviceDialog():
    pass


def setup():

    # open CCW
    import utilities.WindowsShell
    
    utilities.WindowsShell.OpenCCW()

    import testCaseLibrary.CCW.Menu as Menu
    Menu.newProject(addDevice=False)

def tearDown():
    # close CCW
    import testCaseLibrary.CCW
    testCaseLibrary.CCW.close()

def VerifyCatalogList():
    # open Add device dialog
    import testCaseLibrary.CCW.projectOrganizer as projectOrganizer
    projectOrganizer.OpenAddDeviceDialog()

    # verify PV800 catalogs are there
    pass

    # close 
    closeAddDeviceDialog()

def AddEveryPV800CatalogAndVerify():

    import testCaseLibrary.CCW.projectOrganizer as projectOrganizer
    # add every PV800 catalog
    pv800Catalogs = ['2711R-T10T', '2711R-T7T', '2711R-T4T']
    for catalog in pv800Catalogs:
            projectOrganizer.OpenAddDeviceDialog()
            
            AddDevice(catalog)

            # any new added device will be named as PV800_App1
            projectOrganizer.removeDevice('PV800_App1')

    pass

def Regression():

    setup()

    VerifyCatalogList()

    AddEveryPV800CatalogAndVerify()

    tearDown()