from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages

#signup
"""
def sign_up(request):
	if request.method == "POST":
		fm = UserCreationForm(request.POST)
		if fm.is_valid():
			fm.save()

	else:
		fm = UserCreationForm()
		
		return render(request, 'signup.html', {'form':fm})

"""

def sign_up(request):
	if request.method == "POST":
		fm = SignUpForm(request.POST)
		if fm.is_valid():
			messages.success(request,'account created sucessfully !!')
			fm.save()
	else:
		fm = SignUpForm()

	return render(request,'signup.html',{'form':fm} )




#login 

def user_login(request):
	
	if request.method == "POST":
		fm = AuthenticationForm(request = request, data = request.POST)
		if fm.is_valid():
			uname = fm.cleaned_data['username']
			upass = fm.cleaned_data['password']
			user = authenticate(username=uname, password=upass)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/profile/')
	else:
		fm = AuthenticationForm()	
	return render(request, 'login.html', {'form':fm})



#Profile

def user_profile(request):
	return render(request, 'profile.html')