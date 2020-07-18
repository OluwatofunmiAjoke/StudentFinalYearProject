# Create your views here.

from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate 
from django.contrib.auth.forms import UserCreationForm
from predict.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from .models import PredictModel
from predict.forms import MyPredictForm
import json
from .apps import PredictConfig
from django.http import JsonResponse
from rest_framework.views import APIView

# global variable that will hold the highest score
G3 = 0

def home(request):
	return render(request, 'predict/home.html')

@login_required
def predict_result(request):
	if request.method == 'POST':
		# create an instance of the form
		form = MyPredictForm(request.POST, request.FILES)
		#get form data
		student_id=request.POST['student_id']
		fname=request.POST['first_name']
		lname=request.POST['last_name']
		age=request.POST['age']
		sex=request.POST['gender']
		failures=request.POST['failures']
		pstatus=request.POST['pstatus']
		dalc=request.POST['dalc']
		higher=request.POST['higher']
		famrel=request.POST['famrel']
		G1=request.POST['G1']
		G2=request.POST['G2']

		#transform into input suitable for ML model
		if sex =='f':
			sex=1
		else:
			sex=0

		if higher == 'y':
			higher=1
		else:
			higher=0

		if pstatus == 'A':
			pstatus=0
		else:
			pstatus=1

		import pickle
		#input data
		input_data=[[failures,G1,G2,dalc,famrel,sex,higher,pstatus]]
		#importing model
		# this is where the machine learning model makes a prediction

		global G3
		G3 = PredictConfig.loaded_model.predict(input_data)
		
		return redirect('result', student_id = student_id)
			
	else:
		form =  MyPredictForm(request.POST)

	# return render(request, 'predict/predict_result.html', {'form' : form})
	return render(request, 'predict/predict_result.html', {'form': form})
	
# function to diplay the result
@login_required
def result(request, student_id):
	context = {
        'G3': G3,
        'student_id' : student_id
    }

	return render(request, 'predict/result.html', context)

@login_required
def about(request):
	return render(request, 'predict/about.html')

@login_required
def history(request):
	return render(request, 'predict/history.html')
 
def signup(request):
	if request.method == 'POST':
		f = SignUpForm(request.POST)
		if f.is_valid():
			f.save()
			username = f.cleaned_data.get('username')
			raw_password = f.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			django_login(request, user)
			return redirect('predict_result')

	else:
		f = SignUpForm()

	return render(request, 'predict/signup.html', {'form': f})
	#if request.method == 'GET':
	# 	return render(request, 'predict/signup.html', {'form': UserCreationForm()})
	
	# else:
	# 	#Create a new user
	# 	if request.POST['password1'] == request.POST['password2']:
	# 			try:
	# 				user = User.objects.create_user(username= request.POST['username'], password = request.POST['password1'])
	# 				user.save()
	# 				django_login(request, user)
	# 				return  redirect('predict')
	# 			except IntegrityError:
	# 				return render(request, 'predict/signup.html', {'form': UserCreationForm(), 'error':'That username is already taken. Choose new username'} )

	# 	else:
	# 		return render(request, 'predict/signup.html', {'form': UserCreationForm(), 'error':'Passwords did not match'} )


def logout(request):
	if request.method == 'POST':
		django_logout(request)
		return redirect('home') 

def login(request):
	if request.method == 'GET':
		return render(request, 'predict/login.html', {'form': AuthenticationForm()})

	else:
		user= authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'predict/login.html', {'form': AuthenticationForm(), 'error':'Username and password do not match'})
		else: 
			django_login(request, user)
			return redirect('predict_result')