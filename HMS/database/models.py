from django.db import models

# Create your models here.

class doctor(models.Model):
	name = models.CharField(max_length = 25)
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 8)
	phone = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 50)
	gender = models.CharField(max_length = 7)
	status = models.CharField(max_length = 10)	
	department = models.CharField(max_length = 25)
	attendence = models.IntegerField()
	salary = models.IntegerField()

class patients(models.Model):
	name = models.CharField(max_length = 25)
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 8)
	phone = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 50)
	gender = models.CharField(max_length = 7)
	age = models.IntegerField()

class patients_medical_details(models.Model):
	patient_id = models.ForeignKey('patients', on_delete = models.CASCADE)
	weight = models.IntegerField()	
	blood_group = models.CharField(max_length = 5)
	allergies = models.CharField(max_length = 250)

class patients_medical_report(models.Model):
	patient_id = models.ForeignKey('patients', on_delete = models.CASCADE)
	medical_reports = models.FileField(upload_to='./medical_reports/')

class prescriptions(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	patient_id = models.ForeignKey('patients', on_delete = models.CASCADE)
	doctor_id = models.ForeignKey('doctor', on_delete = models.CASCADE)
	app_id = models.ForeignKey('appointments', on_delete = models.CASCADE)			
	symptoms = models.EmailField(max_length = 100)
	details = models.EmailField(max_length = 100)
	medicines = models.CharField(max_length = 250)
	consultant_fees = models.IntegerField()
	other_fees = models.IntegerField()

class appointments(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	patient_id = models.ForeignKey('patients', on_delete = models.CASCADE)		
	status = models.CharField(max_length = 25)
	consulting_doctor_id =  models.IntegerField()
	doctor_department = models.CharField(max_length = 25)

class hr(models.Model):
	name = models.CharField(max_length = 25)
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 8)
	phone = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 50)

class receptionist(models.Model):
	name = models.CharField(max_length = 25)
	username = models.CharField(max_length = 10)
	password = models.CharField(max_length = 8)
	phone = models.CharField(max_length = 10)
	email = models.EmailField(max_length = 50)		

class invoice(models.Model):
	invoice_number = models.IntegerField()
	patient_id = models.ForeignKey('patients', on_delete = models.CASCADE)			
	date = models.DateField(auto_now_add=True)
	paid = models.IntegerField()
	outstanding = models.IntegerField()

class patient_notifications(models.Model):
	patient_id = models.ForeignKey('patients', on_delete = models.CASCADE)			
	notification = models.CharField(max_length = 100)
	app_id = models.ForeignKey('appointments', on_delete = models.CASCADE)			

class payment_history(models.Model):
	order_id = models.IntegerField()
	date = models.DateField(auto_now_add=True)
	patient_id = models.ForeignKey('patients', on_delete = models.CASCADE)			
	amount = models.IntegerField()






