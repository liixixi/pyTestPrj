

def setupEmptyProjectWithT10TAndDefaultSettings():

    import utilities.WindowsShell
    utilities.WindowsShell.OpenCCW()

    import testCaseLibrary.CCW
    testCaseLibrary.CCW.Menu.newProject()

    testCaseLibrary.CCW.catalogService.AddDevice('2711R-T10T')

    testCaseLibrary.CCW.projectOrganizer.CreatePV800Project()

def setup():
    setupEmptyProjectWithT10TAndDefaultSettings()

    pass


def Regression():
    pass