from django.db import models

# Create your models here.

class Airport(models.Model):
	code = models.CharField(max_length=5)
	city = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.city} ({self.code})"

class Flight(models.Model):
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures') # isb.departures.all()
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arivals') # isb.arivals.all()
	duration = models.IntegerField()

	def __str__(self):
		# return str({self.id})+" - "+str(self.origin)+" to "+str(self.destination)
		return f"{self.id} - {self.origin} to {self.destination}."


class Passanger(models.Model):
	first = models.CharField(max_length=64)
	last = models.CharField(max_length=64)
	flights = models.ManyToManyField(Flight, blank=True, related_name='passangers')

	def __str__(self):
		return f"{self.first} {self.last}"