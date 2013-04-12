from django.db import models

# Create your models here.

class ClicksTracked(models.Model):
	post_id = models.IntegerField()
	destination = models.URLField()
	timestamp = models.DateTimeField()


