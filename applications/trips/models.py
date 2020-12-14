from django.db import models


class Trip(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField("Trip's name", max_length=200)
	date = models.DateField(null=True,default=None) 
	
	def __str__(self):
		return self.name


class Passenger(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField("Passenger's name", max_length=200)
	nacional_id = models.CharField("Passenger's nacional id", max_length=10, default="")
	trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name="passengers")

	def __str__(self):
		return self.name


class Stop(models.Model):
	id = models.AutoField(primary_key=True)
	trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name="stops")
	name = models.CharField("Stop's name", max_length=200)
	date = models.DateField(null=True,default=None)
	description = models.CharField("Stop's description", default="", max_length=200)
	
	def __str__(self):
		return self.name 


class Assistant(models.Model):
	id = models.AutoField(primary_key=True)
	stop = models.ForeignKey("Stop", on_delete=models.CASCADE, related_name="assistants")
	passenger = models.ForeignKey("Passenger", on_delete=models.CASCADE)
	has_assisted = models.BooleanField(default=False)

