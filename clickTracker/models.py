from django.db import models
from contentSubmit.models import Post
# Create your models here.

class ClicksTracked(models.Model):
	post = models.ForeignKey(Post)
	destination = models.URLField()
	timestamp = models.DateTimeField()


