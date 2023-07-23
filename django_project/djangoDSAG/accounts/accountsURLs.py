from django.urls import path
from . import views

urlpatterns = [

	#This portion of code is to allow users to view the login/logout page.
	#The functions "login_user" / "logout_user" are defined in the views file within this login dir.
	path('login_user', views.login_user, name="login"),
	path('logout_user', views.logout_user, name="logout"),
]
