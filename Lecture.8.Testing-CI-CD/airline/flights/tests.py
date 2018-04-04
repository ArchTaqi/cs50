from django.test import TestCase
from django.test import Client
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

	def test_departures_count(self):
		a = Airport.objects.get(code='AAA')
		self.assertEqual(a.departures.count(), 3)

	def test_arrivals_count(self):
		a = Airport.objects.get(code='AAA')
		self.assertEqual(a.arivals.count(), 1)

	def test_valid_flights(self):
		a1 = Airport.objects.get(code='AAA')
		a2 = Airport.objects.get(code='BBB')
		f = Flight.objects.get(origin=a1, destination=a2, duration=100)
		self.assertTrue(f.is_valid_flight())

	def test_invalid_flight_duration(self):
		a1 = Airport.objects.get(code='AAA')
		a2 = Airport.objects.get(code='BBB')
		f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
		self.assertFalse(f.is_valid_flight())

	def test_invalid_flight_destination(self):
		a1 = Airport.objects.get(code='AAA')
		a2 = Airport.objects.get(code='BBB')
		f = Flight.objects.get(origin=a1, destination=a1, duration=200)
		self.assertFalse(f.is_valid_flight())

	# Test .view.index
	def test_index_valid_flights(self):
		c = Client()
		response = c.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['flights'].count(), 3)

	def test_index_invalid_flights(self):
		c = Client()
		response = c.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertNotEqual(response.context['flights'].count(), 2)
		# self.assertEqual(response.context['flights'].count(), 4)

	# Test .view.flight
	def test_valid_flight_page(self):
		""" Test if flight id is valid id from datebase, then page should render"""
		a1 = Airport.objects.get(code='AAA')
		f = Flight.objects.get(origin=a1, destination=a1)

		c = Client()
		response = c.get(f"/{f.id}")
		self.assertEqual(response.status_code, 200)

	def test_invalid_flight_page(self):
		""" Test if flight id is not present in datebase, then the view should return 404"""
		max_id = Flight.objects.all().aggregate(max("id"))["id__max"]

		c = Client()
		response = c.get(f"/{max_id + 1}")
		self.assertEqual(response.status_code, 404)


	def test_flight_page_passengers(self):
		f = Flight.objects.get(pk=1)
		p = Passanger.objects.create(first='Alice', last='Adams')
		f.passangers.add(p)

		c = Client()
		response = c.get(f"/{f.id}")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['passangers'].count(), 1)

	def test_flight_page_non_passangers(self):
		f = Flight.objects.get(pk=1)
		p = Passanger.objects.create(first='Alice', last='Adams')

		c = Client()
		response = c.get(f"/{f.id}")

