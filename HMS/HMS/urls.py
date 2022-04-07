"""HMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import database.views.basic_views as basic
import database.views.patient as patient
import database.views.doctor as doctor
import database.views.hr as hr
import database.views.receptionist as rec

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', basic.home_page),
    path('register/', basic.register),
    path('login/', basic.login),

    ### Patient portal urls
    path('patient/<str:username>/', patient.home_page),
    path('patient/<str:username>/appointments/new/', patient.request_appointment),
    path('patient/<str:username>/appointments/', patient.your_appointments),
    path('patient/<str:username>/medical/history/', patient.medical_history),
    path('patient/<str:username>/invoices/', patient.invoice_and_payments),
    path('patient/<str:username>/invoices/<int:invno>/pay/', patient.pay),
    path('patient/<str:username>/payment/history/', patient.paymenthistory),
    path('patient/<str:username>/upload/medical/reports/', patient.upload_report),

    ### Doctor portal urls
	path('doctor/<str:username>/', doctor.home_page),
    path('doctor/<str:username>/appointments/', doctor.dr_appointments),
    path('doctor/<str:username>/prescriptions/new/', doctor.new_prescription),
    path('doctor/<str:username>/prescriptions/history/', doctor.prescriptions_history),
    #path('patient/<str:username>/appointments/new/', patient.request_appointment),

    ### HR portal urls
    path('hr/<str:username>/', hr.home_page),
    path('hr/<str:username>/dashboard/', hr.dashboard),
    path('hr/<str:username>/accounting/', hr.accounting),
    path('hr/<str:username>/dashboard/doctor/<int:drid>/update/', hr.update),
    path('hr/<str:username>/dashboard/doctor/<int:drid>/delete/', hr.deletedr),

    ### Receptionist portal urls
    path('receptionist/<str:username>/', rec.home_page),
    path('receptionist/<str:username>/dashboard/', rec.dashboard),
    path('receptionist/<str:username>/appointments/recommend/', rec.recommend_appointment),
    path('receptionist/<str:username>/appointments/<int:appid>/send/reminder/', rec.send_reminder),
    path('receptionist/<str:username>/appointment/<int:presid>/charge/fees/', rec.charge_fees),
]
