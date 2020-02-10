
def Execute(configuration):

    SetupConfiguration(configuration.name)

    for testCase in configuration.testCases:
        ExecuteTestCase(testCase)

    pass

def ExecuteTestCase(testCase):
    from os.path import join
    import importlib
    
    moduleFullName = 'testCaseLibrary.' + testCase.moduleName

    testCaseModule = importlib.import_module(moduleFullName)
    testCaseFunction = getattr(testCaseModule, testCase.mainFunctionName)

    #basic setup and test support is here, do less work when create test case
    SetupTestCase(testCase)
    ret = testCaseFunction()
    TearDownTestCase(testCase.name, ret)
    pass

def SetupConfiguration(configurationName):
    from utilities import logger

    logger.SetupConfiguration(configurationName)

    pass

def SetupTestCase(testCase):
    from utilities import logger
    import importlib

    logger.logSetupTestCase(testCase.name)

    moduleFullName = 'testCaseLibrary.' + testCase.moduleName

    testCaseModule = importlib.import_module(moduleFullName)
    setupFunctionName = "setup" #default name
    try:
        setupFunctionName = testCase.setup
    except:
        pass

    try:
        #test module may not have such function
        testCaseFunction = getattr(testCaseModule, setupFunctionName)

        testCaseFunction()
    except:
        pass

    pass

def TearDownTestCase(testCaeeName, returnValue):
    pass