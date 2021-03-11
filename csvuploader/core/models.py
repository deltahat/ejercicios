from django.db import models

class File(models.Model):
	file = models.FileField(blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True)

class Calculate(models.Model):
	file_name = models.CharField(max_length=2000, blank=False, null=False)
	file_url = models.CharField(max_length=2000, blank=False, null=False)
	country = models.CharField(max_length=20, blank=False, null=False)
	total_cost = models.FloatField(blank=True, null=True)
	average_cost = models.FloatField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)