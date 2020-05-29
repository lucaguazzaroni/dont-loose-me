import json 
from django.views.generic import TemplateView
from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework import status

from .models import ( Trip, Passenger, Stop, Assistant )

from. serializers import ( 
	TripSimpleSerializer, 
	PassengerSimpleSerializer, 
	StopSimpleSerializer, 
	AssistantSimpleSerializer  
)

@login_required
def trip_listing(request):
	if request.method == 'GET':
		trips = Trip.objects.all()
		serialized_data = TripSimpleSerializer(instance=trips, many=True).data
		return JsonResponse(serialized_data, safe=False, status=status.HTTP_200_OK)

	
@login_required	
@transaction.atomic
def trip_create(request):
	if request.method == 'POST':
		post_data = json.loads( request.body.decode("UTF-8") )
		trip = Trip.objects.create(
			name = post_data.get('name'),
		)
		return JsonResponse({}, safe=False, status=status.HTTP_201_CREATED)


@login_required
@transaction.atomic
def passengers_managment(request, trip_id):
	if request.method == 'GET':
		trip = Trip.objects.get(id=trip_id)
		passengers = Passenger.objects.filter(trip=trip)
		serialized_data = PassengerSimpleSerializer(instance=passengers, many=True).data
		return JsonResponse(serialized_data, safe=False, status=status.HTTP_200_OK)

	if request.method == 'POST':
		post_data = json.loads( request.body.decode("UTF-8") )
		trip = Trip.objects.get(id=trip_id)
		passengers_to_create = []		

		for passenger in post_data:
			passengers_to_create.append( Passenger(name=passenger.get('name'), trip=trip) )

		Passenger.objects.bulk_create(passengers_to_create)
		return JsonResponse({}, safe=False, status=status.HTTP_201_CREATED)


@login_required
def trip_stops_list(request, trip_id):
	if request.method == 'GET':
		trip = Trip.objects.get(id=trip_id)
		stops = Stop.objects.filter(trip=trip)
		serialized_data = StopSimpleSerializer(instance=stops, many=True).data
		return JsonResponse(serialized_data, safe=False, status=status.HTTP_200_OK)


@login_required
def assistants_list(request, stop_id):
	if request.method == 'GET':
		stop = Stop.objects.get(id=stop_id)
		assistants = Assistant.objects.filter(stop=stop)
		serialized_data = AssistantSimpleSerializer(instance=assistants, many=True).data
		return JsonResponse(serialized_data, safe=False, status=status.HTTP_200_OK)


@login_required
def assistants_managment(request, assistant_id):
	if request.method == 'GET':
		assistant = Assistant.objects.get(id=assistant_id)
		serialized_data = AssistantSimpleSerializer(instance=assistant, many=False).data
		return JsonResponse(serialized_data, safe=False, status=status.HTTP_200_OK)
	if request.method == 'PATCH':
		patch_data = json.loads( request.body.decode("UTF-8") )
		assistant = Assistant.objects.get(id=assistant_id)
		assistant.has_assisted = patch_data.get('has_assisted') 
		assistant.save()
		serialized_data = AssistantSimpleSerializer(instance=assistant, many=False).data
		return JsonResponse(serialized_data, safe=False, status=status.HTTP_202_ACCEPTED)



