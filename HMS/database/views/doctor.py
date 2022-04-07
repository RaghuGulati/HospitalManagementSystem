from django.shortcuts import render
from database.forms import *
from database.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home_page(request, username):
	doc = doctor.objects.filter(username = username)
	dr = doc[0]

	context = {
			"username": username,
	}
	return render(request, 'doctor/home.html', context)


def dr_appointments(request, username):
	doc = doctor.objects.filter(username = username)
	dr = doc[0]

	app = appointments.objects.filter(consulting_doctor_id = dr.id)

	context = {
			"username" :  doctor.objects.filter(username = username)[0].username,
			"app": app,
	}

	return render(request, 'doctor/appointments.html', context)

def new_prescription(request, username):
	doc = doctor.objects.filter(username = username)
	dr = doc[0]

	app = appointments.objects.filter(consulting_doctor_id = dr.id, status = 'pending')

	template = 'doctor/new_prescription.html'

	context = {
			"username" :  doctor.objects.filter(username = username)[0].username,
			"app": app,
	}

	if request.method == "POST":
		p = prescriptions()
		appid = request.POST.get("appid")
		a = appointments.objects.get(id = appid)
		pat = patients.objects.get(id = a.patient_id_id)
		p.patient_id = pat
		p.doctor_id = dr
		p.app_id = a
		p.symptoms = request.POST.get("symptoms")
		p.details = request.POST.get("dd")  
		p.medicines = request.POST.get("medicines")  
		p.consultant_fees = request.POST.get("cf")
		p.other_fees = 0  
		p.save()

		a.status = 'done'
		a.save()

	return render(request, template, context)	


def prescriptions_history(request, username):
	doc = doctor.objects.filter(username = username)
	dr = doc[0]

	pres = prescriptions.objects.filter(doctor_id = dr)	

	context = {
			"username" : dr.username,
			"pres": pres,
			
	}

	return render(request, 'doctor/prescription_history.html', context)	

	