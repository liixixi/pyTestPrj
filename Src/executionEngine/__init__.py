

#load all configurations

def loadAllConfigurationFiles(currentPath):
	from os import listdir
	from os.path import isfile, join, splitext, abspath
	import sys

	thismodule = sys.modules[__name__]
	configurationPath = join(currentPath, "configurations")

	for f in listdir(configurationPath):
		if (isfile(join(configurationPath, f)) == False):
			continue
		__all__.append(splitext(f)[0])
		configuration = loadConfiguration(join(configurationPath, f))
		setattr(thismodule, splitext(f)[0], configuration)
		configurations[splitext(f)[0]] = configuration

def loadConfiguration(fileName):
	import json

	with open(fileName) as json_file:
		data = json.load(json_file)
	
	from utilities import jsonLoader 
	configuration = jsonLoader.CreateObject(data)

	return configuration

__all__ = ['excutor']
configurations = {}
loadAllConfigurationFiles(__path__[0])

import executionEngine.excutor as excutor