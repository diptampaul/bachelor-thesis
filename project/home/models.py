from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class FileUpload(models.Model):
#     file_uploaded = models.FileField()
#     public_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, null=True, default='127.0.0.1')
#     name = models.CharField(max_length=200)
#     paper_code = models.IntegerField()
#     total_marks = models.FloatField()
#     engcount = models.FloatField()
#     ctcount = models.FloatField()
#     statcount = models.FloatField()
#     mathcount = models.FloatField()

class UserExtended(models.Model):
    user_photo = models.ImageField(upload_to='user/Pic', blank=True, null=True)
    id_proof = models.FileField(upload_to='user/idProof', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=8, default='NULL')
    default_password = models.CharField(max_length=9, default='NULL')
    bio = models.TextField(blank=True)
    phNo = models.CharField(max_length=20)
    status = models.CharField(max_length=10, default='NULL')
    