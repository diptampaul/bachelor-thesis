from django.db import models

# Create your models here.
class studentDetails(models.Model):
    user_photo = models.ImageField(upload_to='student', blank=True, null=True)
    name = models.CharField(max_length=200, blank=False)
    call_name = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=20, blank=False)
    class_name = models.CharField(max_length=50, blank=False)
    attendance_count = models.IntegerField(default=0)

class attendanceMark(models.Model):
    uploaded_photo = models.ImageField(upload_to='attendance', blank=True, null=True)