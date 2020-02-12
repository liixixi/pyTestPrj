import random
import importlib
import utilities.logger as logger

def Execute(configuration):

    SetupConfiguration(configuration)

    # random.shuffle(configuration.testCases)

    for testCase in configuration.testCases:
        if (TryExpendConfiguration(testCase) == False):
            ExecuteTestCase(testCase)

        # if (TryExpendConfiguration(testCase) != False):
        #     continue
        
        # if (hasattr(testCase, 'dependency')):
        #     continue

        # ExecuteTestCase(testCase)
    
    TearDownConfiguration(configuration)

    pass

def TryExpendConfiguration(testCase):
    expendedConfigurationName = ''
    try:
        expendedConfigurationName = testCase.defination
    except:
        return False
    
    import executionEngine
    Execute(executionEngine.configurations[expendedConfigurationName])

    pass

def ExecuteTestCase(testCase):
    moduleFullName = 'testCaseLibrary.' + testCase.moduleName

    testCaseModule = importlib.import_module(moduleFullName)
    testCaseFunction = getattr(testCaseModule, testCase.mainFunctionName)

    #basic setup and test support is here, do less work when create test case
    SetupTestCase(testCase)
    ret = testCaseFunction()
    TearDownTestCase(testCase.name, ret)
    pass

def SetupConfiguration(configuration):
    logger.SetupConfiguration(configuration.name)

    if (hasattr(configuration, 'setup') == False):
        return
    else:
        moduleFullName = 'testCaseLibrary.' + configuration.moduleName

        setupModule = importlib.import_module(moduleFullName)
        setupFunction = getattr(setupModule, configuration.setup)

        setupFunction()

    pass

def TearDownConfiguration(configuration):
    logger.TearDownConfiguration(configuration.name)

    if (hasattr(configuration, 'tearDown') == False):
        return
    else:
        moduleFullName = 'testCaseLibrary.' + configuration.moduleName

        tearDownModule = importlib.import_module(moduleFullName)
        tearDownFunction = getattr(tearDownModule, configuration.tearDown)

        tearDownFunction()

    pass


def SetupTestCase(testCase):
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