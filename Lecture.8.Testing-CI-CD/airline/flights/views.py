from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passanger
# Create your views here.


def index(request):
	flights = Flight.objects.all()
	context = {
		'flights': flights,
	}
	return render(request, 'flights/index.html', context)


def flight(request, flight_id):
	try:
		flight = Flight.objects.get(pk=flight_id)
	except:
		raise Http404('Flight does not exists.')

	context = {
		'flight': flight,
		'passangers': flight.passangers.all(),
		'non_passangers': Passanger.objects.exclude(flights=flight).all()
	}
	return render(request, 'flights/flight.html', context)


def book(request, flight_id):
	try:
		passanger_id = int(request.POST['passanger'])
		passanger = Passanger.objects.get(pk=passanger_id)
		flight = Flight.objects.get(pk=flight_id)
	except KeyError:
		return render(request, 'flights/error.html', {'message': 'You did not select passanger'})
	except Flight.DoesNotExist:
		return render(request, 'flights/error.html', {'message': 'No Flight'})
	except Passanger.DoesNotExist:
		return render(request, 'flights/error.html', {'message': 'No passanger'})

	passanger.flights.add(flight)
	return HttpResponseRedirect(reverse('index'))
	# return HttpResponseRedirect(reverse('flight', args=(int(flight_id),)))