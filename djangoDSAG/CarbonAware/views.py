from django.shortcuts import render
from . import commandExecuter as exec
import os
from processing import concatDir as dirJoin
import base64
from django.http import FileResponse
import glob
from processing import mrtMap_IMG
import base64
from processing import gmap_iframe as mapEmbed	

# Create your views here.

def index(request):

		return render(request, 'html/index.html')

def cecResults(request):
	if request.method == "POST":
		transportMode=request.POST['transportMode']
		vehicleType=request.POST['vehicleType']
		fuelType=request.POST['fuelType']
		startPoint=request.POST['startPoint']
		endPoint=request.POST['endPoint']
		metricType=request.POST['metricType']

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

		workingDir = os.getcwd()
		directory = dirJoin.concatDir(workingDir, "/processing")
		command = ["python3", "google_mapper_v8.py", transportMode, vehicleType, fuelType, \
	      startPoint, endPoint, metricType]
		output = exec.execute(command, directory, workingDir)
		
		output = str(output[0])
		if output.startswith("b'"):
			output = output.replace("b", "", 1)
			output = output.replace("'", "", 2)
		
		formatted_output = output.replace('\\n', '\n').replace('\\t', '\t')
		print (formatted_output)

		map = mapEmbed.generateFMap(transportMode, vehicleType, fuelType, startPoint, endPoint, metricType)

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

		startMRT=request.POST['startMRT']
		endMRT=request.POST['endMRT']

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

		graph = mrtMap_IMG.generateMRTimage(startMRT, endMRT)

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

		return render(request, 'html/mrtMap.html', {'graph':graph, 'output':formatted_output})