from django.db import models


class SampleModel(models.Model):
    text = models.CharField(default='', max_length=100)
    uploaded_file = models.FileField(upload_to='uploaded/')
