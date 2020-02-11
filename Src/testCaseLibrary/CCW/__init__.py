
def CCWRegression():

    import testCaseLibrary.CCW.catalogService

    # catalog service regression test cases
    #catalogService.Regression()

    pass


def close(save='True'):
    pass

import testCaseLibrary.CCW.toolWindow as toolWindow
toolWindows = {}

def findToolWindow(name):
    return toolWindow.toolWindow()


def getActiveToolWindow():
    # taf get active tool window

    return toolWindow.toolWindow()