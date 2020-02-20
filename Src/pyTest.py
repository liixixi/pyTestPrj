

# from executionEngine import *
import executionEngine
import os
import json

# ---------------execute the all configuration -------------- #
from executionEngine import *

# accept command line
# pyTest -Regression 
excutor.Execute(Regression)

# -------------- execute the regression you want ------------ #
regressionDict = {'configuration': 'configurations', 'regression': 'multipleTab'}

# obtain current folder path
configurationPath = executionEngine.__file__.replace('__init__.py', regressionDict['configuration'])
regressionPath = os.path.join(configurationPath, regressionDict['regression']) + '.json'

# judge whether the json file you added exist or not
if(os.path.isfile(regressionPath) == False):
    print('The json file you added do not exist!')
    os._exit()


# load configuration class object
configuration = executionEngine.loadConfiguration(regressionPath)

# execut the regression you want to test
executionEngine.excutor.Execute(configuration)



# -------------just executing the testcase you want --------- #
testCaseDict = {'configuration': 'configurations','regression' : 'multipleTab', 'testCase': 'openMultipleScreen'}

# obtain current folder path
configurationPath = executionEngine.__file__.replace('__init__.py', testCaseDict['configuration'])
regressionPath = os.path.join(configurationPath, testCaseDict['regression']) + '.json'

# judge whether the json file you added exist or not
if(os.path.isfile(regressionPath) == False):
    print('The json file you added do not exist!')
    os._exit()

# load configuration class object
configuration = executionEngine.loadConfiguration(regressionPath)

# execut the testCase you want to test
for testCase in configuration.testCases:
    if (testCase.name != testCaseDict['testCase']):
        continue
    executionEngine.excutor.ExecuteTestCase(testCase)

pass
