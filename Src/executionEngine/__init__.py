

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
		setattr(thismodule, splitext(f)[0], loadConfiguration(join(configurationPath, f)))

def loadConfiguration(fileName):
	import json

	with open(fileName) as json_file:
		data = json.load(json_file)

	return [type('',(object,),tc)() for tc in data ]

__all__ = []
loadAllConfigurationFiles(__path__[0])