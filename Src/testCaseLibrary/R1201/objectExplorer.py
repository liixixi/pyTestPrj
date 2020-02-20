
def setupObjectExplorer():
    pass

def tearDownObjectExplorer():
    pass

def showCloseHideObjectExplorer():
    import utilities
    import testCaseLibrary

    stepLogger = utilities.logger.getStepLogger()
    from utilities.verify import verify as verify

    # 1. launch CCW, create new project, show object explorer
    stepLogger.logStepInfo('launch CCW, create new project, show object explorer')
    utilities.WindowsShell.OpenCCW()
    testCaseLibrary.CCW.Menu.newProject(addDevice=False)
    testCaseLibrary.CCW.catalogService.AddDevice('2711R-T10T')
    verify(testCaseLibrary.CCW.projectOrganizer.CreatePV800Project() != None, 'create PV800 application')
    verify(testCaseLibrary.CCW.Menu.OpenObjectExplorer() != None, 'Object Explorer is shown')

    # 2. close object explorer
    stepLogger.logStepInfo('close object explorer')
    verify(testCaseLibrary.CCW.objectExplorer.Close(), 'Object Explorer is closed')

    # 3. show object explorer
    stepLogger.logStepInfo('show object explorer')
    verify(testCaseLibrary.CCW.Menu.OpenObjectExplorer() != None, 'Object Explorer is shown')

    # 4. reset window layout
    stepLogger.logStepInfo('reset window layout')
    testCaseLibrary.CCW.Menu.ResetWindowLayout()
    verify(testCaseLibrary.CCW.objectExplorer.IsOpen() == False, 'Object Explorer is closed')

    # 5. show object explorer
    stepLogger.logStepInfo('show object explorer')
    verify(testCaseLibrary.CCW.Menu.OpenObjectExplorer() != None, 'Object Explorer is shown')

    # 6. hide object explorer
    stepLogger.logStepInfo('hide object explorer')
    testCaseLibrary.CCW.objectExplorer.Hide()
    verify(testCaseLibrary.CCW.objectExplorer.IsOpen() == False, 'Object Explorer is closed')

    # 7. close CCW
    stepLogger.logStepInfo('close CCW')
    testCaseLibrary.CCW.close()

    pass