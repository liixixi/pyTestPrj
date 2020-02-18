
def setupMultipleTab():
    pass

def setupFunctionName():
    #fix error, lack this function
    pass

def tearDownMultipleTab():
    pass

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
    verify(testCaseLibrary.CCW.findToolWindow(leftScreenNames[0]) != None, leftScreenNames[0] + ' is opened')
    verify(testCaseLibrary.CCW.findToolWindow(leftScreenNames[1]) != None, leftScreenNames[1] + ' is opened')

    testCaseLibrary.CCW.findToolWindow(leftScreenNames[1]).close()
    testCaseLibrary.CCW.findToolWindow(leftScreenNames[0]).close()

    pass

def multipleScreenTest():
    import utilities
    caseLogger = utilities.logger.getCaseLogger()

    caseLogger.logCaseInfo('Open more than one screen')
    multipleScreenTest1()

    caseLogger.logCaseInfo('Change current active screen')
    multipleScreenTest2()

    caseLogger.logCaseInfo('Cut/Copy/Paste Across Tabs')
    multipleScreenTest3()

    caseLogger.logCaseInfo('Drag and drop Across Tabs')
    multipleScreenTest4()

    caseLogger.logCaseInfo('Rename active screen name')
    multipleScreenTest5()

    caseLogger.logCaseInfo('Close screen tab')
    multipleScreenTest6()

    caseLogger.logCaseInfo('Change graphic terminal')
    multipleScreenTest7()

    caseLogger.logCaseInfo('Close project')
    multipleScreenTest8()

    caseLogger.logCaseInfo('Upload Application')
    multipleScreenTest9()

    caseLogger.logCaseInfo('Validate, Download Application')
    multipleScreenTest10()

    caseLogger.logCaseInfo('Focus in active screen')
    multipleScreenTest11()

    caseLogger.logCaseInfo('Compability PVC')
    multipleScreenTest12()

    caseLogger.logCaseInfo('Compability old project')
    multipleScreenTest13()
    pass

#open more than one screen
def multipleScreenTest1():
    import utilities.WindowsShell
    import testCaseLibrary 

    stepLogger = utilities.logger.getStepLogger()
    #stepLogger.logStepInfo('open one or more screen')

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    from utilities.verify import verify as verify
    # 1. create new PV800 project
    stepLogger.logStepInfo('create new PV800 project')
    testCaseLibrary.CCW.Menu.newProject(addDevice=False)
    testCaseLibrary.CCW.catalogService.AddDevice('2711R-T10T')
    verify(testCaseLibrary.CCW.projectOrganizer.CreatePV800Project() != None, 'create PV800 project')

    # 2. open default screen Screen_1
    stepLogger.logStepInfo('open default screen Screen_1')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_1') != None, 'Screen_1 is opened')
    
    # 3. add new screen and open, should be Screen_2
    stepLogger.logStepInfo('add new screen and open, should be Screen_2')
    testCaseLibrary.CCW.projectOrganizer.CreateScreen() 
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_2') != None, 'Screen_2 is opened')
                                            #   findToolWindow
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') != False, 'Screen_1 is still open')
    
    # 4. close Screen_1, Screen_2 is still open
    stepLogger.logStepInfo('close Screen_1, Screen_2 is still open')
    testCaseLibrary.CCW.findToolWindow('Screen_1').close()
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == False, 'Screen_1 is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen("Screen_2") != False, 'Screen_2 is still open')

    # 5. open Screen_1 again
    stepLogger.logStepInfo('open Screen_1 again')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_1') != None, 'Screen_1 is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_2') != False, 'Screen_2 is still open')

    # 6. add new screen and open, should be Screen_3
    stepLogger.logStepInfo('add new screen and open, should be Scren_3')
    testCaseLibrary.CCW.projectOrganizer.CreateScreen()
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_3') != None, 'Screen_3 is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') != False, 'Screen_1 is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_2') != False, 'Screen_2 is opened')
    
    # 7. Close Screen_1, Screen_2 and Screen_3 still open
    stepLogger.logStepInfo('Close Screen_1, Screen_2 and Screen_3 still open')
    testCaseLibrary.CCW.findToolWindow('Screen_1').close()
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == False, 'Screen_1 is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_2') != False, 'Screen_2 is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_3') != False, 'Screen_3 is still open')
    
    # 8. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')
    pass 

#change current active screen
def multipleScreenTest2():
    import utilities
    import testCaseLibrary
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    from utilities.verify import verify as verify
    # 1. open MultipleTab project
    stepLogger.logStepInfo('open MultipleTab project')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')

    # 2. open Main
    stepLogger.logStepInfo('open Main')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main is opened')

    # 3. open Diagnostics and active it
    stepLogger.logStepInfo('open Diagnostics and active it')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Diagnostics is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') != False, 'Main is still open')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics is active')

    # 4. open Main and active it
    stepLogger.logStepInfo('opan Main and active it')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Main', 'Main is active')

    # 5. open diagnostics screen by opened screen list (right-top arrow)
    stepLogger.logStepInfo('open diagnostics screen by opened screen list (right-top arrow)')
    testCaseLibrary.CCW.toolWindow.openedScreenList.activeToolWindow('Diagnostics')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics is active')

    # 6. open Alarm Banner and active it
    stepLogger.logStepInfo('open Alarm Banner and active it')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarm Banner') != None, 'Alarm Banner is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarm Banner', 'Alarm Banner is active')

    # 7. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass

#cut/copy/paste across tabs
def multipleScreenTest3():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    

    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    from utilities.verify import verify as verify
    # 1. open MultipleTab project
    stepLogger.logStepInfo('open MultipleTab project')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')

    # 2. open Main 
    stepLogger.logStepInfo('open Main')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main is opened')

    # 3. open Alarms
    stepLogger.logStepInfo('open Alarms')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms is active')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') != False, 'Main is still open')

    # 4. copy ClearAllALarm button from Alarms and paste it to Main 
    stepLogger.logStepInfo('copy ClearAllALarm button from Alarms and paste it to Main')
    testCaseLibrary.CCW.copy.copyPanelDevice('ClearAllAlarm')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main')
    testCaseLibrary.CCW.copy.pasteScreenObject()
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Main', 'Main is active')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('ClearAllAlarm') != None, 'ClearAllAlarm button is pasted')

    # 5. active Alarms
    stepLogger.logStepInfo('active Alarms')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') 
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms is active')

    # 6. cut Up key
    stepLogger.logStepInfo('cut Up key')
    testCaseLibrary.CCW.objectOperate.cutScreenObject('Up')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up') == None, 'Up key is cut')

    # 7. avtive Recipes
    stepLogger.logStepInfo('active Recipes')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Recipes')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Recipes', 'Recipes is active')

    # 8. paste Up key on Recipes
    stepLogger.logStepInfo('paste Up key on Recipes')
    testCaseLibrary.CCW.objectOperate.pasteScreenObject('Up')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up') != None, 'Up key is pasted')  

    # 9. undo paste Up key
    stepLogger.logStepInfo('undo paste Up key')
    testCaseLibrary.CCW.objectOperate.undoOperate()
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up') == None, 'undo Up key paste')  

    # 10. active Alarms
    stepLogger.logStepInfo('active Alarms')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms is active')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up') == None, 'no Up key on screen')

    # 11. undo cut operation
    stepLogger.logStepInfo('undo cut operation')
    testCaseLibrary.CCW.objectOperate.undoOperate()
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up') != None, 'Up key is back on screen')
    
    # 7. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass

#drag and drop across tabs
def multipleScreenTest4():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    

    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. open project MultipleTab
    stepLogger.logStepInfo('open project MultipleTab')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')

    # 2. open Main screen
    stepLogger.logStepInfo('open Main screen')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main is opened')

    # 3. open and active Alarms screen, Enter key on Alarms screen
    stepLogger.logStepInfo('open and active Alarms screen, Enter key on Alarms screen')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms is active')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Enter') != None, 'Enter key on Alarm screen')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') != False, 'Main is still open')

    # 4. drag and drop Enter key from Alarms to Main screen
    stepLogger.logStepInfo('drag and drop Enter key from Alarms to Main screen')
    testCaseLibrary.CCW.objectOperate.dragDropScreenObject('Enter', 'Alarms', 'Main')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Main', 'Main is active')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Enter') != None, 'Enter key on Main screen')

    # 5. back to Alarms screen and no Enter key
    stepLogger.logStepInfo('back to Alarms screen and no Enter key')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Enter') == None, 'no Enter key on Alarms screen')

    # 6. undo drag/drop operation
    stepLogger.logStepInfo('undo drag/drop operation')
    testCaseLibrary.CCW.objectOperate.undoOperate()
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Enter') != None, 'Enter key on Alarm screen')

    # 7. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass

#rename active screen name
def multipleScreenTest5():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. open project MultipleTab
    stepLogger.logStepInfo('open project MultipleTab')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')
     
    # 2. open Main screen
    stepLogger.logStepInfo('open Main screen')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')

    # 3. open and active Alarms screen
    stepLogger.logStepInfo('open and active Alarms screen')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != True, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms screen is active')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == True, 'Main screen is still open')

    # 4. rename Main to Home
    stepLogger.logStepInfo('rename Main to Home')
    verify(testCaseLibrary.CCW.projectOrganizer.renameScreen('Main', 'Home') == True, 'rename Main to Home success')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Home') == True, 'Home screen is still open')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms screen is active')

    # 5. rename Alarms to Alarm
    stepLogger.logStepInfo('rename Alarms to Alarm')
    verify(testCaseLibrary.CCW.projectOrganizer.renameScreen('Alarms', 'Alarm') == True, 'rename Alarms to Alarm')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarm', 'Alarm screen is active')

    # 6. open and active Diagnostics screen
    stepLogger.logStepInfo('open and active Diagnostics sceeen')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics screen is active')

    # 7. rename Alarm to Alarms
    stepLogger.logStepInfo('rename Alarm to Alarms')
    verify(testCaseLibrary.CCW.projectOrganizer.renameScreen('Alarm', 'Alarms') == True, 'rename Alarm to Alarms')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == True, 'Alarms screen is still open')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics screen is active')

    # 8. rename Home to Main
    stepLogger.logStepInfo('rename Home to Main')
    verify(testCaseLibrary.CCW.projectOrganizer.renameScreen('Home', 'Main') == True, 'rename Home to Main')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == True, 'Main screen is still open') 
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics screen is active')

    # 9. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass

#close screen tab
def multipleScreenTest6():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. open project MultipleTab
    stepLogger.logStepInfo('open project MultipleTab')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')
    
    # 2. open Main screen
    stepLogger.logStepInfo('open Main screen')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')

    # 3. open Alarms screen
    stepLogger.logStepInfo('open Alarms screen')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == True, 'Alarms screen is opened')

    # 4. open Recipes screen
    stepLogger.logStepInfo('open Recipes screen')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Recipes')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Recipes') == True, 'Recipes screen is opened')

    # 5. close Recipes screen
    stepLogger.logStepInfo('close Recipes screen')
    testCaseLibrary.CCW.findToolWindow('Recipes').close()
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Recipes') != True, 'Recipes screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == True, 'Alarms screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == True, 'Main screen is still open')

    # 6. close all screens
    stepLogger.logStepInfo('close all screens')
    testCaseLibrary.CCW.findToolWindow('Main').closeAllDocuments()
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Recipes') != True, 'Recipes screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') != True, 'Alarms screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') != True, 'Main screen is closed')

    # 7. open Main, Alarms and Diagnostics
    stepLogger.logStepInfo('open Main, Alarms and Diagnostics')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Diagnostics screen is opened')

    # 8. close all screens but Diagnostics
    stepLogger.logStepInfo('close all screens but Diagnostics')
    testCaseLibrary.CCW.findToolWindow('Diagnostics').closeAllButThis()
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == True, 'Diagnostics screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') != True, 'Main screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') != True, 'Alarms screen is closed')

    # 9. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass

#change graphics terminal
def multipleScreenTest7():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. open project MultipleTab
    stepLogger.logStepInfo('open project MultipleTab')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')

    # 2. open Main, Alarms and Diagnostics screen
    stepLogger.logStepInfo('open Main, Alarms and Diagnostics screen')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Alarms screen is opened')

    # 3. change ternimal size/type
    stepLogger.logStepInfo('change terminal size')
    currentType = testCaseLibrary.CCW.projectOrganizer.GetGraphicsTerminalType()
    testCaseLibrary.CCW.projectOrganizer.ChangeGraphicsTerminal('')
    newType = testCaseLibrary.CCW.projectOrganizer.GetGraphicsTerminalType()
    verify(currentType != newType, 'terminal size is changed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == False, 'Main screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == False, 'Alarms screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == False, 'Diagnostics screen is closed')

    # 4. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass

#close project
def multipleScreenTest8():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. open project MultipleTab
    stepLogger.logStepInfo('open project MultipleTab')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')

    # 2. open Main, Alarms and Diagnostics 
    stepLogger.logStepInfo('open Main, Alarms and Diagnostics')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Diagnostics screen is opened')

    # 3. save project to another name
    stepLogger.logStepInfo('save project to another name')
    verify(testCaseLibrary.CCW.Menu.SaveAs('MultipleTab2') != None, 'save project as MultipleTab2')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == False, 'Main screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == False, 'Alarms screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == False, 'Diagnostics screen is closed')

    # 4. open Main, Alarms and Diagnostics
    stepLogger.logStepInfo('open Main, Alarms and Diagnostics')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Diagnostics screen is opened')

    # 5. close project
    stepLogger.logStepInfo('close project')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == False, 'Main screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == False, 'Alarms screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == False, 'Diagnostics screen is closed')

    # 6. open project MultipleTab, open Main, Alarms and Diagnostics
    stepLogger.logStepInfo('open project MultipleTab, open Main, Alarms and Diagnostics')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Diagnostics screen is opened')

    # 7. open recent project
    stepLogger.logStepInfo('open recent project')
    verify(testCaseLibrary.CCW.Menu.openRecentProject('MultipleTab2') != None, 'recent project MultipleTab2 is opened')
    verify(testCaseLibrary.CCW.Menu.GetCurrentProjectName() != 'MultipleTab', 'MultipleTab project is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == False, 'Main screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == False, 'Alarms screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == False, 'Diagnostics screen is closed')

    # 8. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab2') != None, 'project MultipleTab2 is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass
# Upload Application
def multipleScreenTest9():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. open project MultipleTab
    stepLogger.logStepInfo('open project MultipleTab')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')

    # 2. open Main, Alarms and Diagnostics 
    stepLogger.logStepInfo('open Main, Alarms and Diagnostics')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Diagnostics screen is opened')

    # 3. unload first, then cancel
    stepLogger.logStepInfo('upload first, then cancel')
    testCaseLibrary.CCW.projectOrganizer.Upload()
    testCaseLibrary.CCW.projectOrganizer.CancelUpload()
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == True, 'Main screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == True, 'Alarms screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == True, 'Diagnostics screen is still open')

    # 4. upload application App1
    stepLogger.logStepInfo('upload application')
    testCaseLibrary.CCW.projectOrganizer.Upload('')
    verify(testCaseLibrary.CCW.projectOrganizer.ConfirmUpload() != None, 'application is uploaded')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') == False, 'Main screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') == False, 'Alarms screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == False, 'Diagnostics screen is closed')

    # 5. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass
# Validate, Download Application
def multipleScreenTest10():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. open project MultipleTab
    stepLogger.logStepInfo('open project MultipleTab')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')

    # 2. open Main, Alarms and Diagnostics
    stepLogger.logStepInfo('open Main, Alarms and Diagnostics')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opend')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms screen is opend')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Diagnostics screen is opend')


    # 3. validate application
    stepLogger.logStepInfo('validate application')
    verify(testCaseLibrary.CCW.projectOrganizer.Validate() != None, 'application is validated')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Main') != False, 'Main screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarms') != False, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnotics') != False, 'Diagnotics screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.IsBlink() == False, 'no screen blink')

    # 4. download application
    stepLogger.logStepInfo('download application')
    verify(testCaseLibrary.CCW.projectOrganizer.Download() != None, 'application is downloaded')
    verify(testCaseLibrary.CCW.projectOrganizer.IsBlink() == False, 'no screen blink')

    # 5. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name = 'MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass
# Focus in active screen
def multipleScreenTest11():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. open project MultipleTab
    stepLogger.logStepInfo('open project MultipleTab')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'MultipleTab') != None, 'MultipleTab project is opened')

    # 2. open Main, Alarms and Diagnostics
    stepLogger.logStepInfo('open Main, Alarms and Diagnostics')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main') != None, 'Main screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms') != None, 'Alarms screen is opened')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics') != None, 'Diagnostics screen is opened')

    # 3. focus Alarms screen
    stepLogger.logStepInfo('focus Alarms screen')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarm', 'Alarms screen is shown in front')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms').IsHasFocus() == True, 'Alarms screen has focus')

    # 4. open object explorer
    stepLogger.logStepInfo('open object explorer')
    verify(testCaseLibrary.CCW.Menu.OpenObjectExplorer() != None, 'object explorer is opened')
    
    # 5. select object M_OBJ1 in Main
    stepLogger.logStepInfo('select object M_OBJ1 in Main')
    testCaseLibrary.CCW.Menu.OpenObjectExplorer()
    testCaseLibrary.CCW.objectExplorer.SelectObject('Main', 'M_OBJ1')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Main', 'Main screen is shown')
    screenObject1 = testCaseLibrary.CCW.objectOperate.findScreenObject('M_OBJ1') 
    verify(screenObject1.hasFocus() == True, 'M_OBJ1 has focus')

    # 6. select object A_OBJ1 in Alarms
    stepLogger.logStepInfo('select object A_OBJ1 in Alarms')
    testCaseLibrary.CCW.Menu.OpenObjectExplorer()
    testCaseLibrary.CCW.objectExplorer.SelectObject('Alarms', 'A_OBJ1')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms screen is shown')
    screenObject2 = testCaseLibrary.CCW.objectOperate.findScreenObject('A_OBJ1')
    verify(screenObject2.hasFocus() == True, 'A_OBJ1 has focus')

    # 7. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name = 'MultipleTab') != None, 'project MultipleTab is closed')
    verify(CloseCCW() != None, 'CCW is closed')

    pass
# Compability PVC
def multipleScreenTest12():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy 
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()

    # 1. create new Pvc project 
    stepLogger.logStepInfo('create new Pvc project')
    testCaseLibrary.CCW.Menu.newProject(addDevice=False)
    testCaseLibrary.CCW.catalogService.AddDevice('2711R-T10T')
    verify(testCaseLibrary.CCW.projectOrganizer.CreatePVCProject() != None, 'create new PVC project')

    # 2. open screen Screen_1
    stepLogger.logStepInfo('open screen Screen_1')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_1') != None, 'Screen_1 is opened')

    # 3. open screen Diagnostics 
    stepLogger.logStepInfo('open screen Diagnostics')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics screen is shown')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == True, 'Screen_1 is still open')

    # 4. open screen Alarm Banner
    stepLogger.logStepInfo('open screen Alarm Banner')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarm Banner')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarm Banner', 'Alarm Banner screen is shown')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == True, 'Screen_1 screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == True, 'Diagnostics screen is still open')

    # 5. change graphics ternimal
    stepLogger.logStepInfo('change graphics terminal')
    currentType = testCaseLibrary.CCW.projectOrganizer.GetGraphicsTerminalType()
    testCaseLibrary.CCW.projectOrganizer.ChangeGraphicsTerminal('')
    newType = testCaseLibrary.CCW.projectOrganizer.GetGraphicsTerminalType()
    verify(currentType != newType, 'terminal size is changed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == False, 'Screen_1 screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarm Banner') == False, 'Alarm Banner screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == False, 'Diagnostics screen is closed')

    # 6. open Screen_1, Diagnostics and Alarm Banner
    stepLogger.logStepInfo('open Screen_1, Diagnostics and Alarm Banner')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_1') 
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarm Banner')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == True, 'Screen_1 screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == True, 'Diagnostics screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarm Banner') == True, 'Alarm Banner screen is closed')

    # 7. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name = '') != None, 'project is closed')
    verify(CloseCCW() != None, 'CCW is closed')
    
    pass

def multipleScreenTest13():
    import utilities
    import testCaseLibrary
    import testCaseLibrary.CCW.copy
    from utilities.verify import verify as verify

    stepLogger = utilities.logger.getStepLogger()

    # open ccw, need call Taf in OpenCCW()
    utilities.WindowsShell.OpenCCW()
    
    # 1. open old project OldProject
    stepLogger.logStepInfo('open old project OldProject')
    verify(testCaseLibrary.CCW.Menu.openProject(name = 'OldProject') != None, 'OldProject is opened')

    # 2. open Screen_1 screen
    stepLogger.logStepInfo('open Screen_1 screen')
    verify(testCaseLibrary.CCW.projectOrganizer.OpenScreen('Screen_1') != None, 'Screen_1 screen is opened')

    # 3. open Diagnostics screen
    stepLogger.logStepInfo('open Diagnostics screen')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics screen is shown')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == True, 'Screen_1 screen is still open')

    # 4. open Alarm Banner screen
    stepLogger.logStepInfo('open Alarm Banner screen')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarm Banner')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarm Banner', 'Alarm Banner screen is shown')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == True, 'Screen_1 screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == True, 'Diagnostics screen is still open')

    # 5. validate project
    stepLogger.logStepInfo('validate project')
    verify(testCaseLibrary.CCW.projectOrganizer.Validate() != None, 'project is validated')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == True, 'Screen_1 screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarm Banner') == True, 'Alarm Banner screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == True, 'Diagnostics screen is still open')

    # 6. download application
    stepLogger.logStepInfo('download application')
    verify(testCaseLibrary.CCW.projectOrganizer.Download() != None, 'application is downloaded')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == True, 'Screen_1 screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarm Banner') == True, 'Alarm Banner screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == True, 'Diagnostics screen is still open')

    # 7. cancel upload 
    stepLogger.logStepInfo('cancel upload project')
    testCaseLibrary.CCW.projectOrganizer.Upload('')
    testCaseLibrary.CCW.projectOrganizer.CancelUpload()
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == True, 'Screen_1 screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarm Banner') == True, 'Alarm Banner screen is still open')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == True, 'Diagnostics screen is still open')

    # 8. upload application
    testCaseLibrary.CCW.projectOrganizer.Upload('')
    verify(testCaseLibrary.CCW.projectOrganizer.ConfirmUpload() != None, 'application is uploaded')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Screen_1') == False, 'Screen_1 screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Alarm Banner') == False, 'Alarm Banner screen is closed')
    verify(testCaseLibrary.CCW.projectOrganizer.IsScreenOpen('Diagnostics') == False, 'Diagnostics screen is closed')


    # 9. close project and CCW
    stepLogger.logStepInfo('close project and CCW')
    verify(testCaseLibrary.CCW.Menu.closeProject(name='OldProject') != None, 'project OldProject is closed')
    verify(CloseCCW() != None, 'CCW is closed')

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

def CutCopyAcrossScreen():

    import testCaseLibrary
    import testCaseLibrary.CCW.projectOrganizer
    import testCaseLibrary.CCW.copy 
    import utilities
    from utilities.verify import verify as verify

    stepLogger = utilities.logger.getStepLogger()
    stepLogger.logStepInfo('open main screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')

    stepLogger.logStepInfo('open Alarms screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms') != None, 'Alarms is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms is current active toolWindow')

    stepLogger.logStepInfo('Copy ClearAllAlarm button from Alarms screen to Main screen')

    testCaseLibrary.CCW.copy.copyPanelDevice('ClearAllAlarm')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Main', 'Main is current active toolWindow')  
    testCaseLibrary.CCW.copy.pasteScreenObject()
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('ClearAllAlarm')!=None,'ClearAllAlarm is pasted')
    
    stepLogger.logStepInfo('open Alarms screen again')
    
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name=='Alarms','Alarm is current active Window')
    
    stepLogger.logStepInfo('Cut Up Key from Alarm Screen')
    testCaseLibrary.CCW.objectOperate.cutScreenObject('Up')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up')==None,'Up Key is cut')

    stepLogger.logStepInfo('Open Recipes Screen')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Recipes')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name=='Recipes','Recipes is current active Window')
    
    stepLogger.logStepInfo('Paste Up Key to Recipes screen')
    testCaseLibrary.CCW.objectOperate.pasteScreenObject('Up')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up')!=None,'Up Key is pasted')    
    
    stepLogger.logStepInfo('Undo paste')
    testCaseLibrary.CCW.objectOperate.undoOperate()
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up')==None,'Undo, Up Key is revmoved')

    stepLogger.logStepInfo('open Alarms screen again')
    
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name=='Alarms','Alarm is current active Window')

    stepLogger.logStepInfo('Undo cut')
    testCaseLibrary.CCW.objectOperate.undoOperate()
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Up')!=None,'Undo, Up Key is back')
    pass

def DragDropAcrossScreen():
    import testCaseLibrary.CCW.projectOrganizer
    import utilities
    from utilities.verify import verify as verify
    
    stepLogger = utilities.logger.getStepLogger()
    stepLogger.logStepInfo('open main screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')

    stepLogger.logStepInfo('open Alarms screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms') != None, 'Alarms is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms is current active toolWindow')
   
    stepLogger.logStepInfo('Drag and drop Enter to Main Screen ')

    testCaseLibrary.CCW.objectOperate.DragDropPanelDevice('Enter','Main')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name=='Main','Main is current active Window')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Enter') !=None,'Drag and Drop, Enter Key is on the Main Screen')
    
    stepLogger.logStepInfo('No Enter Key on the Alarms Screen')
    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms') == None, 'Alarms is opened')
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Enter') ==None,'Drag and Drop, Enter Key is NOT on the Main Screen')

    stepLogger.logStepInfo('Undo')
    testCaseLibrary.CCW.objectOperate.undoOperate()
    verify(testCaseLibrary.CCW.objectOperate.findScreenObject('Enter') !=None,'Enter Key is back')

def renameActiveScreen():
    import testCaseLibrary
    import utilities
    from utilities.verify import verify as verify

    stepLogger = utilities.logger.getStepLogger()
    stepLogger.logStepInfo('open main screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Main')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')

    stepLogger.logStepInfo('open Alarms screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Alarms')
    verify(testCaseLibrary.CCW.findToolWindow('Main') != None, 'Main is opened')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms') != None, 'Alarms is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms is current active toolWindow')

    stepLogger.logStepInfo('rename Screen Main to Home')

    testCaseLibrary.CCW.projectOrganizer.renameScreen('Main','Home')
    verify(testCaseLibrary.CCW.findToolWindow('Main') == None, 'Main has been renamed')
    verify(testCaseLibrary.CCW.findToolWindow('Home') != None, 'Home is the new name')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms') != None, 'Alarms is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarms', 'Alarms is current active toolWindow')

    stepLogger.logStepInfo('rename Screen Alarms to Alarm')

    testCaseLibrary.CCW.projectOrganizer.renameScreen('Alarms','Alarm')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms') == None, 'Alarms has been renamed')
    verify(testCaseLibrary.CCW.findToolWindow('Alarm') != None, 'Alarm is the new name')
    verify(testCaseLibrary.CCW.findToolWindow('Home') != None, 'Home is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Alarm', 'Alarm is current active toolWindow')

    stepLogger.logStepInfo('open Diagnostics screen')

    testCaseLibrary.CCW.projectOrganizer.OpenScreen('Diagnostics')
    verify(testCaseLibrary.CCW.findToolWindow('Diagnostics') != None, 'Diagnostics is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics is current active toolWindow')

    stepLogger.logStepInfo('rename Screen Alarm to Alarms')

    testCaseLibrary.CCW.projectOrganizer.renameScreen('Alarm','Alarms')
    verify(testCaseLibrary.CCW.findToolWindow('Alarm') == None, 'Alarm has been renamed')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms') != None, 'Alarms is the new name')
    verify(testCaseLibrary.CCW.findToolWindow('Home') != None, 'Home is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics is current active toolWindow')

    stepLogger.logStepInfo('rename Screen Home to Main')

    testCaseLibrary.CCW.projectOrganizer.renameScreen('Alarm','Alarms')
    verify(testCaseLibrary.CCW.findToolWindow('Alarm') == None, 'Alarm has been renamed')
    verify(testCaseLibrary.CCW.findToolWindow('Alarms') != None, 'Alarms is the new name')
    verify(testCaseLibrary.CCW.findToolWindow('Home') != None, 'Home is opened')
    verify(testCaseLibrary.CCW.getActiveToolWindow().name == 'Diagnostics', 'Diagnostics is current active toolWindow')
    pass