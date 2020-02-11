
def CreateANewProject():
    import utilities
    utilities.WindowsShell.OpenCCW()

    import testCaseLibrary
    testCaseLibrary.CCW.Menu.newProject(addDevice=False)

    testCaseLibrary.CCW.catalogService.AddDevice('2711R-T10T')

    testCaseLibrary.CCW.projectOrganizer.CreatePV800Project()
    pass

def OpenProjectMulitpleTab():
    import utilities
    utilities.WindowsShell.OpenCCW()

    import testCaseLibrary
    testCaseLibrary.CCW.Menu.openProject(name='MultipleTab')
    pass

def CloseCCW():
    import testCaseLibrary
    testCaseLibrary.CCW.close()
    pass

def openMultipleScreen():
    import utilities
    import testCaseLibrary

    stepLogger = utilities.logger.getStepLogger()
    stepLogger.logStepInfo('open two screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_1')

    testCaseLibrary.CCW.projectOrganizer.CreateScreen()

    from utilities.verify import verify as verify
    verify(testCaseLibrary.CCW.findToolWindow('Screen_1') != None, 'Screen_1 is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Screen_2') != None, 'Screen_2 is opened')
    
    stepLogger.logStepInfo('close Screen_1')

    testCaseLibrary.CCW.findToolWindow('Screen_1').close()

    verify(testCaseLibrary.CCW.findToolWindow('Screen_1') == None, 'Screen_1 is closed')
    verify(testCaseLibrary.CCW.findToolWindow('Screen_2') != None, 'Screen_2 is opened')

    stepLogger.logStepInfo('open Screen_1')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_1')
    verify(testCaseLibrary.CCW.findToolWindow('Screen_1') != None, 'Screen_1 is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Screen_2') != None, 'Screen_2 is opened')

    stepLogger.logStepInfo('Create Screen_3')

    testCaseLibrary.CCW.projectOrganizer.CreateScreen()
    verify(testCaseLibrary.CCW.findToolWindow('Screen_1') != None, 'Screen_1 is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Screen_2') != None, 'Screen_2 is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Screen_3') != None, 'Screen_3 is opened')
    
    stepLogger.logStepInfo('close a random screen')
    #random a screen name
    import utilities.rand as rand
    randomNumber = rand.randrange(1, 3)
    screenName = 'Screen_' + str(randomNumber)

    #close it
    testCaseLibrary.CCW.findToolWindow(screenName).close()
    
    # left screen names
    leftScreenNames = []
    for i in range(1, 4):
        if (i != randomNumber):
            leftScreenNames.append('Screen_' + str(i))

    # verify this step
    verify(testCaseLibrary.CCW.findToolWindow(screenName) == None, screenName + ' is closed')
    verify(testCaseLibrary.CCW.findToolWindow(leftScreenNames[0]) != None, leftScreenNames[0] + 'is opened')
    verify(testCaseLibrary.CCW.findToolWindow(leftScreenNames[1]) != None, leftScreenNames[1] + 'is opened')

    pass

def changeCurrentActiveScreen():

    import testCaseLibrary
    import utilities
    from utilities.verify import verify as verify

    stepLogger = utilities.logger.getStepLogger()
    stepLogger.logStepInfo('open main screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')

    stepLogger.logStepInfo('open diagnostics screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnosctics')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Diagnosctics') != None, 'Diagnosctics is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnosctics', 'Diagnosctics is current active toolWindow')

    stepLogger.logStepInfo('open main screen again')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Main', 'Main is current active toolWindow')

    stepLogger.logStepInfo('open diagnostics screen by opened screen list (right-top arrow)')

    testCaseLibrary.CCW.toolWindow.openedScreenList.activeToolWindow('Diagnosctics')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnosctics', 'Diagnosctics is current active toolWindow')  

    stepLogger.logStepInfo('open alarm banner')
    testCaseLibrary.CCW.toolWindow.openedScreenList.activeToolWindow('Alarm')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Diagnosctics') != None, 'Diagnosctics is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Alarm') != None, 'Alarm is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarm', 'Alarm is current active toolWindow')  

    pass