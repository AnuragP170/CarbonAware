import os

def concatDir(directory, string):
	try:
		outputDir = directory + string
	except Exception as e:
		if string.startswith('/'):
			string = string[1:]
		
		outputDir = os.path.join(directory, string)
	
	return outputDir