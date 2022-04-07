from django.shortcuts import *
from database.forms import *
from database.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import *

# Create your views here.

def home_page(request, username):
	pat = patients.objects.filter(username = username)
	patient = pat[0]
	context = {
			"username": patient.username,
	}
	return render(request, 'patients/home.html', context)

def request_appointment(request, username):
	pat = patients.objects.filter(username = username)
	patient = pat[0]
	form = upload_medical_report(request.FILES or None)
	app = appointments()
	template = "patients/request_appointment.html"	
	obj1 = patients.objects.filter(username = username)
	pmdt = patients_medical_details.objects.filter(patient_id = obj1[0])
	pmr = patients_medical_report()

	if pmdt.exists():
		pmd = pmdt[0]
		context = {
				"username": patient.username,
				"patient": obj1[0],
				"pmd": pmd,
				"form": form,
			}
	else:
		pmd = patients_medical_details()
		context = {
				"username": username,
				"patient": obj1[0],
				"form": form,
			}

	if request.method == "POST":
			obj1[0].age = request.POST.get("age")
			obj1[0].save()

			pmd.patient_id = obj1[0]
			pmd.weight = request.POST.get("weight")
			pmd.blood_group = request.POST.get("bg")
			pmd.allergies = request.POST.get("pa")
			pmd.save()

			app.patient_id = obj1[0]
			app.status = "request queued"			
			app.consulting_doctor_id = 0
			app.doctor_department = request.POST.get("dt")
			app.save()

	return render(request, template, context)

def your_appointments(request, username):
	pat = patients.objects.filter(username = username)
	patient = pat[0]

	notification = patient_notifications.objects.filter(patient_id = patient)

	context = {
			"username" : patient.username,
			"notification": notification,

	}

	return render(request, 'patients/appointments.html', context)

def medical_history(request, username):
	pat = patients.objects.filter(username = username)
	patient = pat[0]

	pres = prescriptions.objects.filter(patient_id = patient)	

	context = {
			"username" : patient.username,
			"pres": pres,
	}

	return render(request, 'patients/medical_history.html', context)	

def invoice_and_payments(request, username):
	pat = patients.objects.filter(username = username)
	patient = pat[0]

	inv = invoice.objects.filter(patient_id = patient)

	context = {
			"username" : patient.username,
			"inv": inv,
	}

	return render(request, 'patients/invoice_and_payments.html', context)		

def pay(request, username, invno):
	pat = patients.objects.filter(username = username)
	patient = pat[0]

	inv = invoice.objects.filter(invoice_number = invno)[0]
	ph = payment_history()

	ct = payment_history.objects.all().aggregate(Count('id'))
	inv.invoice_number = 1803526 + ct['id__count']

	ph.order_id = 3659282 + ct['id__count']		
	ph.patient_id = patient

	template = 'patients/pay.html'

	if request.method == "POST":
		pay = request.POST.get("money")
		inv.paid = pay
		inv.outstanding -= int(pay)
		inv.save()

		ph.amount = pay
		ph.save()

		return redirect('/patient/'+str(patient.username)+'/invoices/')

	context = {
			"username" : patient.username,
			"inv": inv,
	}	

	return render(request, 'patients/pay.html', context)		

def paymenthistory(request, username):
	pat = patients.objects.filter(username = username)
	patient = pat[0]

	ph = payment_history.objects.filter(patient_id = patient)

	context = {
			"username" : patient.username,
			"ph": ph,
	}	

	return render(request, 'patients/payment_history.html', context)		

def upload_report(request, username):
	pat = patients.objects.filter(username = username)
	patient = pat[0]

	form = upload_medical_report(request.POST, request.FILES or None)
	pmr = patients_medical_report()

	if form.is_valid():
		pmr.patient_id = patient
		pmr.medical_reports = form.cleaned_data.get('medical_report')
		pmr.save()

	context = {
			"username" : patient.username,
			"form": form,
	}

	return render(request, 'patients/upload.html', context)		