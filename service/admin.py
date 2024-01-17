from django.contrib import admin
from service.models import Contact, Patient, Feed, Hospitalinfo, Appointmentinfo
from django.contrib.auth.admin import UserAdmin


class ContactAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'add')
admin.site.register(Contact, ContactAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display=('first_name', 'lastname', 'gender', 'date_of_birth', 'marital_status', 'bloodgroup',
        'aadharnumber', 'email', 'phonenumber', 'add', 'symptoms','ename','relation', 'emergencynumber')
admin.site.register(Patient, PatientAdmin)

class FeedAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'msg')
admin.site.register(Feed, FeedAdmin)

class HospitalinfoAdmin(admin.ModelAdmin):
    list_display=('hospitalname', 'doctorname', 'specialization','phonenumber', 'area', 'location', 'link')
admin.site.register(Hospitalinfo, HospitalinfoAdmin)
    
class AppointmentinfoAdmin(admin.ModelAdmin):
    list_display=('hospitalname','location', 'link')
admin.site.register(Appointmentinfo, AppointmentinfoAdmin)
    
# Register your models here.
