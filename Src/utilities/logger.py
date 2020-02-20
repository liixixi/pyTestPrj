

def logSetupTestCase(testCaseName):

    print("Start executing test case '{0}'\n".format(testCaseName))
    pass


def SetupConfiguration(configurationName):
    print("Start executing configuration '{0}'\n".format(configurationName))
    pass

def TearDownConfiguration(configurationName):
    print("Configuration '{0}' has been closed \n".format(configurationName))
    pass

def verifyMessage(message):
    print("    " + message)

class stepLogger:
    def __init__(self):
        self.step = 1

    def logStepInfo(self, message):
        print('----------------------------------')
        print('Step' + str(self.step) + ' ' + message)
        self.step += 1
    
def getStepLogger():
    return stepLogger()

class caseLogger:
    def __init__(self):
        self.case = 1
    def logCaseInfo(self, message):
        print('==================================')
        print('Case ' + str(self.case) + ' ' + message)
        self.case += 1

def getCaseLogger():
    return caseLogger()

def circularrefernceLogger(configuraitonName):
    print("Configuration '{0}' has a circular reference, please check it!\n".format(configuraitonName))
    pass