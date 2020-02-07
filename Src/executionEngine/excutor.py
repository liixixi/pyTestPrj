
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
    SetupTestCase(testCase.name)
    ret = testCaseFunction()
    TearDownTestCase(testCase.name, ret)
    pass

def SetupConfiguration(configurationName):
    from utilities import logger

    logger.SetupConfiguration(configurationName)

    pass

def SetupTestCase(testCaseName):
    from utilities import logger

    logger.logSetupTestCase(testCaseName)

    pass

def TearDownTestCase(testCaeeName, returnValue):
    pass