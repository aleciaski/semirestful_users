from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from  .models import User, UserManager

def index(request):
	print("INDEX....INDEX")
	context={
		"users": User.objects.all()
	}
	return render(request, "restful_users_app/index.html", context)

def new(request):
	print ("WE MADE IT TO new!!")


	return render(request,"restful_users_app/new.html")

def create(request):
	errors= User.objects.custom_basic_validator(request.POST)
	if len(errors):
		for key in error.keys():
			messages.error(request, errors[key])
			return redirect("restful_users_app/index.html")
	else:
	# print(request.POST['first_name'])
		User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
		return render(request,"restful_users_app/index.html")


def edit(request):
	print ("WE ARE IN EDIT")
	context={
		"user": User.objects.get(id=id)
	}
	return render(request, "restful_users_app/edit.html")

def show(request, id):
	print("SHOW ME")
	context:{
		"user": User.objects.get(id=id)
	}
	return render(request,"restful_users_app/show.html",context)



def update(request, id):
	context={
		'users': User.objects.get(id=id)
	}
	
	return redirect(request, "restful_users_app/edit.html", context)

def destroy(request, id):
	User.objects.get(id=id).delete()
	return redirect("restful_users_app/index.html")