from rest_framework import serializers

from .models import ( Trip, Passenger, Stop, Assistant )

class TripSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'name']

class PassengerSimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Passenger
		fields = ['id', 'name', 'trip']

class PassengerSimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stop
		fields = ['id', 'name', 'trip']

class AssistantSimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assistant
		fields = ['id', 'stop', 'passenger', 'has_assisted']



