from django.test import TestCase

from .models import Airport, Flight
# Create your tests here.


class ModelTestCase(TestCase):

	def setUp(self):
		"""
			This function runs before any test run.
		"""

		# create Airports
		a1 = Airport.objects.create(code='AAA', city='City A')
		a2 = Airport.objects.create(code='BBB', city='City B')

		# create flights
		Flight.objects.create(origin=a1, destination=a2, duration=100)
		Flight.objects.create(origin=a1, destination=a1, duration=200)
		Flight.objects.create(origin=a1, destination=a2, duration=-100)

