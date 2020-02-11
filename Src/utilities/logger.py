

def logSetupTestCase(testCaseName):

    print("Start executing test case '{0}'\n".format(testCaseName))
    pass


def SetupConfiguration(configurationName):
    print("Start executing configuration '{0}'\n".format(configurationName))
    pass

def verifyMessage(message):
    print(message)

class stepLogger:
    def __init__(self):
        self.step = 1

    def logStepInfo(self, message):
        print('----------------------------------')
        print('Step' + str(self.step) + ' ' + message)
        self.step += 1

def getStepLogger():
    return stepLogger()