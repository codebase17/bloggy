from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Tbl_user(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_email_id=models.CharField(max_length=100)
    user_password=models.TextField(max_length=256)
       
    
