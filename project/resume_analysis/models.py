from django.db import models

# Create your models here.
class ResumeAnalysis(models.Model):
    uploaded_file = models.FileField(upload_to='resume', blank=True, null=True)