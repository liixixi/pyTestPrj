





#test 1
def setup():
    import utilities
    utilities.WindowsShell.OpenCCW()

def tearDown():
    import testCaseLibrary
    testCaseLibrary.CCW.close()

def OpenCrossReferenceWindow():
    # open cross reference tool windows
    import testCaseLibrary.CCW.Menu
    testCaseLibrary.CCW.Menu.openCrossReferenceWindow()

def VerifyCrossReferenceWindowExists():

    # wait until - time out 10 seconds

    # verify exists

    # log if needed
    pass


def TestOpenCrossReferenceWindow():

    OpenCrossReferenceWindow()

    VerifyCrossReferenceWindowExists()

def testcase1():
    OpenCrossReferenceWindow()



