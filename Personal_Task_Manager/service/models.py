from django.db import models
class Service(models.Model):
     title=models.CharField(max_length=10)
     description=models.TextField()
     date=models.DateField()
     service_image=models.FileField(upload_to="news/",max_length=250,null=True,default=None)
     status=models.TextField()
# Create your models here.
