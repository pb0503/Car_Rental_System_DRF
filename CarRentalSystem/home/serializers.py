from rest_framework import serializers
from home.models import Customer, Car, Reservation


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name','email','phone']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','vehicle_number','model','seating_capacity','rent_per_day']

class AvailableCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','vehicle_number','model','seating_capacity','rent_per_day','availability']
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id','customer','car','issue_date','return_date']

class CarDetailsReservationSerializer(serializers.Serializer):
    car = CarSerializer()
    current_active_bookings = ReservationSerializer(many=True)