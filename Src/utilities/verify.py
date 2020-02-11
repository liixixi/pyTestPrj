

def verify(condition, message):
    import utilities
    if (condition):
        utilities.logger.verifyMessage('Verify ' + message + ' passed!\n')
    else:
        utilities.logger.verifyMessage('Verify ' + message + ' failed!\n')