from django.shortcuts import *
from database.forms import *
from database.models import *
from django.contrib.auth.models import User
from django.http import *
from django.db.models import *
from django.db import connection

# Create your views here.

def home_page(request, username):
	context = {
			"username":hr.objects.filter(username = username)[0].username,
	}
	return render(request, 'hr/home.html', context)


def dashboard(request, username):
	totaldr = doctor.objects.all().aggregate(Count('id'))
	totalp = patients.objects.all().aggregate(Count('id'))
	ondutydr = doctor.objects.filter(status = "active").aggregate(Count('id'))

	doctors = doctor.objects.all()
	patient = patients.objects.all()

	template = 'hr/dashboard.html'
	context = {
			"username":hr.objects.filter(username = username)[0].username,
			"totaldr": totaldr['id__count'],
			"totalp": totalp['id__count'],
			"ondutydr": ondutydr['id__count'],
			"doctors": doctors,
			"patient": patient,
	}
	return render(request, template, context)

def update(request, username, drid):
	dr = doctor.objects.get(id = drid)
	form = doctormodelform(request.POST or None, instance = dr)

	template = "hr/update.html"
	
	if form.is_valid():
		form.save()
		return redirect('/hr/' + str(username) + '/dashboard/')

	context = {
		'form2': form, 
		"id": f"Update {dr.id}", 
		"dr":dr,
		"username":hr.objects.filter(username = username)[0].username,
		}

	return render(request, template, context)
	

def deletedr(request, username, drid):
	dr = doctor.objects.get(id = drid)

	dr.delete()

	return redirect('/hr/' + str(username) + '/dashboard/')

def accounting(request, username):
	template = 'hr/accounting.html'

	pres = prescriptions.objects.all()	
	inv = invoice.objects.all()

	context = {
		"username":hr.objects.filter(username = username)[0].username,
		"pres": pres,
		"inv": inv,

	}

	return render(request, template, context)
