from django.contrib import admin
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','description','date','status','service_image')
admin.site.register(Service,ServiceAdmin)
# Register your models here.
