from django.db import models

# Create your models here.
class Tweet(models.Model):
	tweet = models.CharField(max_length=200)
	username = models.CharField(max_length=100)
	time = models.CharField(max_length=100)

	def __str__(self):
		return self.tweet