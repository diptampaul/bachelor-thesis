from django.db import models

# Create your models here.
class encodeFile(models.Model):
    file_type = models.CharField(max_length=10, null=True, blank=True)
    upload1 = models.FileField(upload_to='ecdc/decoded', blank=True, null=True)
    upload2 = models.FileField(upload_to='ecdc/main', blank=True, null=True)

class decodeFile(models.Model):
    encoded = models.FileField(upload_to='ecdc/encoded', blank=True, null=True)