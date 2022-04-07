from django.shortcuts import *
from database.forms import *
from database.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def home_page(request):
	return render(request, 'home.html')

def register(request):
	form = register_form(request.POST or None)
	form2 = register2(request.POST or None)

	if form.is_valid() and form2.is_valid():
		register_as = form2.cleaned_data.get("registerf")

		if register_as == "Doctor":
			obj = doctor()
			obj.status = "Active"
			obj.department = " "
			obj.attendence = 0
			obj.salary = 20000
		else:
			obj = patients()


		fname = form.cleaned_data.get("fname")
		lname = form.cleaned_data.get("lname")
		obj.name = fname + " " + lname
		obj.username = form.cleaned_data.get("uname")
		obj.email = form.cleaned_data.get("email")
		
		password = form.cleaned_data.get("password")
		conf_password = form.cleaned_data.get("conf_password")

		obj.phone = form.cleaned_data.get("mobile")
		obj.gender = form2.cleaned_data.get("gender")
		obj.age = form.cleaned_data.get("age")

		if password == conf_password:
			obj.password = password
			user = User.objects.create_user(username=obj.username,
			                 email=obj.email,
			                 password=password)
			obj.save()

		else:
			return HttpResponse("Password and conf_password do not match")

	template = "register.html"
	context = { 'form': form, 'form2': form2}
	return render(request, template, context)

def login(request):
	form = login_form(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get("uname")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		registeras = form.cleaned_data.get("registerf")

		u = User.objects.get(username = username, email = email)
		if u.check_password(password) == True:
			return redirect('/'+str(registeras)+'/'+ str(username))
		else:
			return HttpResponse("Login with correct credentials")

	template = "register.html"
	context = { 'form2': form,}
	return render(request, template, context)	
