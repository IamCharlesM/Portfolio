from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=255)
    title = models.CharField(max_length=100, default='Job Title')

    def __str__(self):
        return self.title