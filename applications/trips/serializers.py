from rest_framework import serializers

from .models import ( Trip, Passenger, Stop, Assistant )

class TripSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'name', 'date']

class PassengerSimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Passenger
		fields = ['id', 'name', 'trip']

class StopSimpleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stop
		fields = ['id', 'trip', 'name', 'date', 'description']

class AssistantSimpleSerializer(serializers.ModelSerializer):
	passenger = PassengerSimpleSerializer()
	class Meta:
		model = Assistant
		fields = ['id', 'stop', 'passenger', 'has_assisted']



