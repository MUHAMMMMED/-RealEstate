from django.db import models

# Create your models here.

from django.db import models

class MediaUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    audio = models.FileField(upload_to='uploads/')
    animated_video = models.FileField(upload_to='animated/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)