from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
	
	#User login. If using POST request, send username and password to backend.
	#If request is not POST (ie. GET), then just display the page.
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		
		#If user is in the database, send user to dashboard after successful login.
		#If user is not in the database, return error message as shown below.
		if user is not None:
			login(request, user)
			return redirect('CarbonAware')
		else:
			messages.success(request, "There was an error logging in, please try again.")
			return redirect('login')
	else:
		return render(request, 'html/login.html', {})

# The logout request will just log the user out and show the main page, with message
# containing successful logout.
def logout_user(request):
	logout(request)
	messages.success(request, "You have logged out!")
	return redirect('CarbonAware')