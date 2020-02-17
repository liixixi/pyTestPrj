import random
import importlib
import sys
sys.path.append('./')
import utilities.logger as logger
import utilities.generatelist as generater

def ExecuteTestCase(testCase):
    moduleFullName = 'testCaseLibrary.' + testCase.moduleName

    testCaseModule = importlib.import_module(moduleFullName)
    testCaseFunction = getattr(testCaseModule, testCase.mainFunctionName)

    #basic setup and test support is here, do less work when create test case
    SetupTestCase(testCase)
    ret = testCaseFunction()
    TearDownTestCase(testCase.name, ret)
    pass

def Execute(configuration, testCaseExecutor=ExecuteTestCase):

    SetupConfiguration(configuration)

    leftTestCases = configuration.testCases

    while (len(leftTestCases) > 0):

        random.shuffle(leftTestCases)
        leftTestCasesNameList = generater.generatenamelist(leftTestCases)

        executedTestCases = []
        for testCase in leftTestCases:

            if (TryExpendConfiguration(testCase) != False):
                executedTestCases.append(testCase)
                continue
            
            if (hasattr(testCase, 'dependency') != False and testCase.dependency in leftTestCasesNameList):
                continue

            testCaseExecutor(testCase)
            executedTestCases.append(testCase)
        
        for testCase in executedTestCases:
            leftTestCases.remove(testCase)
    
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

# Fake function for testing
def FakeExecuteTestCase(testCase):

    FakeSetupTestCase(testCase)
    FakeTestCaseFunction(testCase)
    FakeTearDownTestCase(testCase)

    pass

def FakeSetupTestCase(testCase):

    print("---------------------------\n")
    print("Start executing test case '{0}'\n".format(testCase.name))

    pass

def FakeTearDownTestCase(testCase):

    print("Test case '{0}' has been closed\n".format(testCase.name))

    pass

def FakeTestCaseFunction(testCase):

    print("Executing test case '{0}'\n".format(testCase.name))

    pass


if (__name__=='__main__'):
    # add utilities to python path
    from utilities import jsonLoader
    import json

    # load test configurationS
    with open(r'executionEngine\test\testConfiguration.json') as json_file:
        data = json.load(json_file)
    
    testconfiguration = jsonLoader.CreateObject(data)

    # call Execute
    # 1. provide a fake execute function, add to json
    # 2. provide a fake execute case function, add to Execute function

    Execute(testconfiguration, testCaseExecutor = FakeExecuteTestCase)

    # 3. adopt a python unit test framework
    from unittest import mock
    mock_fakeTestCase = mock.Mock(return_value = 'Execute test case', side_effect = FakeExecuteTestCase)
    Execute(testconfiguration, testCaseExecutor=mock_fakeTestCase)

    pass