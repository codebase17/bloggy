from pyexpat import model
from django.db import models
from user.models import Tbl_user

# Create your models here.
class Tbl_blog_post(models.Model):
    blog_post_id=models.AutoField(primary_key=True)
    post_user_email_id=models.ForeignKey(Tbl_user, on_delete=models.CASCADE,default=None,null=True)
    post_title=models.CharField(max_length=256)
    post_content=models.CharField(max_length=1200)
    last_modified_date=models.DateField()
    likes=models.IntegerField()
    