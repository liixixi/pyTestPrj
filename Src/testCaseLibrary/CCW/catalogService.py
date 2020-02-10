
def AddDevice(catalog):
    SelectDevice(catalog)
    DoAddDevice()

def SelectDevice(catalog):
    # call taf workflow
    pass

def DoAddDevice():
    # call taf workflow
    pass 


def setup():

    # open CCW
    import utilities.WindowsShell
    utilities.WindowsShell.OpenCCW()

    # new a empty project with default name and location
    import Menu
    Menu.newProject(addDevice=False)

def tearDown():
    # close CCW
    import testCaseLibrary.CCW
    testCaseLibrary.CCW.close()

def Regression():

    setup()

    # open Add device dialog
    import projectOrganizer
    projectOrganizer.OpenAddDeviceDialog()

    # verify PV800 catalogs are there
    pass

    # add every device with every orientation
    pv800Catalogs = ['2711R-T10T', '2711R-T7T', '2711R-T4T']

    import projectOrganizer
    for catalog in pv800Catalogs:
            AddDevice(catalog)

            # any new added device will be named as PV800_App1
            projectOrganizer.removeDevice('PV800_App1')

    tearDown()