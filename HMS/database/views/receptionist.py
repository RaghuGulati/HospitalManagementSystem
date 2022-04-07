from django.shortcuts import *
from database.forms import *
from database.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import *
from pytz import timezone
# Create your views here.

def home_page(request, username):
	context = {
			"username":receptionist.objects.filter(username = username)[0].username,
	}
	return render(request, 'receptionist/home.html', context)

def dashboard(request, username):
	totala = appointments.objects.all().aggregate(Count('id'))
	queuesa = appointments.objects.filter(status = "request queued").aggregate(Count('id'))
	pendinga = appointments.objects.filter(status = "pending").aggregate(Count('id'))
	donea =appointments.objects.filter(status = "done").aggregate(Count('id'))
	
	apq = appointments.objects.filter(status = "request queued")
	app = appointments.objects.filter(status = "pending")
	apd = prescriptions.objects.all()

	template = 'receptionist/dashboard.html'
	context = {
			"username":receptionist.objects.filter(username = username)[0].username,
			"totala": totala['id__count'],
			"queuesa": queuesa['id__count'],
			"pendinga": pendinga['id__count'],
			"donea": donea['id__count'],
			"apq": apq,
			"app": app,
			"apd": apd,
	}
	return render(request, template, context)

def recommend_appointment(request, username):
	form = app_recommend_form(request.POST or None)

	if form.is_valid() and request.method == 'POST':
		appid = form.cleaned_data.get("appid")
		app = appointments.objects.get(id = appid)
		drid = form.cleaned_data.get("drid")
		dr = doctor.objects.filter(name = drid)

		app.consulting_doctor_id = dr[0].id
		app.datetime = request.POST.get("datetime")
		print(app.datetime)
		app.status = "pending"
		app.save()

	template = 'receptionist/recommend.html'
	context = {
			"username": username,
			"form": form,
	}
	return render(request, template, context)

def send_reminder(request, username, appid):
	app = appointments.objects.get(id = appid)
	patient = patients.objects.get(id = app.patient_id_id)
	dr = doctor.objects.get(id = app.consulting_doctor_id)
	notification = patient_notifications()

	print(app.datetime)

	notification.patient_id = patient
	notification.notification = "Appointment fixed on " + str(app.datetime.astimezone(timezone('Asia/Kolkata'))) + " with Dr. " + str(dr.name)
	notification.app_id = app
	notification.save()

	context = {
			"username":receptionist.objects.filter(username = username)[0].username,
	}

	return render(request, 'receptionist/home.html', context)

def charge_fees(request, username, presid):
	pres = prescriptions.objects.get(id = presid)
	form = prescriptionmodelform(request.POST or None, instance = pres)

	template = "receptionist/charge.html"
		

	if form.is_valid():
		form.save()
		inv = invoice()
		ct = invoice.objects.all().aggregate(Count('id'))
		inv.invoice_number = 1803526 + ct['id__count']
		inv.patient_id = pres.patient_id
		inv.paid = 0
		inv.outstanding = int(pres.consultant_fees) + int(pres.other_fees)
		inv.save()
	
		return redirect('/receptionist/' + str(username) + '/dashboard/')

	context = {
		'form2': form, 
		"id": f"Update {pres.id}", 
		"pres":pres,
		"username":receptionist.objects.filter(username = username)[0].username,
		}

	return render(request, template, context)
