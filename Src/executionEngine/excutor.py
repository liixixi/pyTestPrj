
def Excute(configuration):
    for testCase in configuration:
        ExcuteTestCase(testCase)

    pass

def ExcuteTestCase(testCase):
    from os.path import join
    import importlib
    
    moduleFullName = 'testCaseLibrary.' + testCase.moduleName

    testCaseModule = importlib.import_module(moduleFullName)
    testCaseFunction = getattr(testCaseModule, testCase.mainFunctionName)
    testCaseFunction()
    pass
