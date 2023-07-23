from django.shortcuts import render
from . import commandExecuter as exec
import os
from processing import concatDir as dirJoin
from processing import mrtMap_IMG
from processing import cec_iframe as mapEmbed	

# Create your views here.

# Function to display the homepage to take in values
def index(request):

		return render(request, 'html/index.html')

# This function serves at the main processing point for the
# Carbon Emissions Calculator. 
def cecResults(request):
	if request.method == "POST":

		# Collection of values from the webpage
		##################################################
		transportMode=request.POST['transportMode']
		vehicleType=request.POST['vehicleType']
		fuelType=request.POST['fuelType']
		startPoint=request.POST['startPoint']
		endPoint=request.POST['endPoint']
		metricType=request.POST['metricType']
		##################################################

		# Processing of the values that were taken in 
		# from the webpage.
		##################################################
		if transportMode == "1":
			transportMode = "Driving"
		elif transportMode == "2":
			transportMode = "Transit"
		elif transportMode == "3":
			transportMode = "Walking"
		else:
			transportMode = "Error - Not Found"

		if vehicleType == "4":
			vehicleType = "Car"
		elif vehicleType == "5":
			vehicleType = "Motorcycle"
		else:
			vehicleType = ""
		
		if fuelType == "6":
			fuelType = "Petrol"
		elif fuelType == "7":
			fuelType = "Diesel"
		else:
			fuelType = ""

		if metricType == "8":
			metricType = "Distance"
		elif metricType == "9": 
			metricType = "Duration"
		elif metricType == "10":
			metricType = "Emissions"
		else:
			metricType = ""
		##################################################

		# This section of code deals with generation of the output for
		# the directions. The "Concat Directory" function returns a 
		# directory string, which is used to automate the execution of 
		# the Google Mapper file for generation of directions.
		#
		# The execution of the Google Mapper file will return the 
		# directions from the given start point and end point. This is stored
		# in the "output" variable, which is a tuple. The relevant output is 
		# taken from the tuple, namely the first entry, and then formatted
		# using string manipulation to remove certain punctuation marks as well as
		# special characters.
		##################################################
		workingDir = os.getcwd()
		directory = dirJoin.concatDir(workingDir, "/processing")
		command = ["python3", "carbon_emission_calculator.py", transportMode, vehicleType, fuelType, \
	      startPoint, endPoint, metricType]
		output = exec.execute(command, directory, workingDir)
		
		output = str(output[0])
		if output.startswith("b'"):
			output = output.replace("b", "", 1)
			output = output.replace("'", "", 2)
		
		formatted_output = output.replace('\\n', '\n').replace('\\t', '\t')
		##################################################

		# This function points to a duplicate Google Mapper file, but instead
		# of returning output, it returns a Folium map object to be rendered on the 
		# webpage.
		##################################################
		map = mapEmbed.generateFMap(transportMode, vehicleType, fuelType, startPoint, endPoint, metricType)
		##################################################

		# Return the webpage to be loaded as well as the variables that will be
		# displayed on the page.
		return render(request, 'html/display.html', {'transportMode': transportMode, 
					       	'vehicleType': vehicleType,
						    'fuelType': fuelType,
							'startPoint': startPoint,
							'endPoint': endPoint,
							'output': formatted_output,
							'map': map,
							})
	else:
		return render(request, 'html/display.html')

def mrtOptimizer(request):
	if request.method == 'POST':

		# Collection of values from the webpage
		##################################################
		startMRT=request.POST['startMRT']
		endMRT=request.POST['endMRT']
		##################################################

		# Processing of the values that were taken in 
		# from the webpage.
		##################################################
		if startMRT == "11":
			startMRT = "Ang Mo Kio (Red Line)"
		elif startMRT=="12":
			startMRT = "HarbourFront (Purple Line)"
		elif startMRT=="13":
			startMRT = "Jurong East (Green Line)"
		elif startMRT=="14":
			startMRT = "Bukit Panjang (Blue Line)"
		else:
			startMRT = "Stevens (Brown Line)"

		if endMRT == "16":
			endMRT = "Dhoby Ghaut (Red Line)"
		elif endMRT=="17":
			endMRT = "Tampines (Green Line)"
		elif endMRT=="18":
			endMRT = "Punggol (Purple Line)"
		elif endMRT=="19":
			endMRT = "Bedok North (Blue Line)"
		else:
			endMRT = "Orchard (Brown Line)"
		##################################################

		# This section of code deals with generation of the output for
		# the directions. The "Concat Directory" function returns a 
		# directory string, which is used to automate the execution of 
		# the MRT Optimizer file for generation of directions.
		#
		# The execution of the MRT Optimizer file will return the 
		# directions from the given start point and end point. This is stored
		# in the "output" variable, which is a tuple. The relevant output is 
		# taken from the tuple, namely the first entry, and then formatted
		# using string manipulation to remove certain punctuation marks as well as
		# special characters.
		##################################################
		workingDir = os.getcwd()
		directory = dirJoin.concatDir(workingDir, "/processing")
		command = ["python3", "mrt_route_optimizer_final.py", startMRT, endMRT]
		output = exec.execute(command, directory, workingDir)
		output = str(output[0])
		
		if output.startswith("b'"):
			output = output.replace("b", "", 1)
			output = output.replace("'", "", 2)
		
		formatted_output = output.replace('\\n', '\n').replace('\\t', '\t')
		print (formatted_output)
		##################################################

		# This function points to a duplicate MRT Optimizer file, but instead
		# of returning output, it returns a MatPlotLib chart to be returned to
		# the webpage for display.
		##################################################
		graph = mrtMap_IMG.generateMRTimage(startMRT, endMRT)

		# Return the webpage to be loaded as well as the variables that will be
		# displayed on the page.
		return render(request, 'html/mrtMap.html', {'graph':graph, 'output':formatted_output})