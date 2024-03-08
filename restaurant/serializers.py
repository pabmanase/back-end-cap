from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        #can define this explicitly with:
        #fields = ['id', 'title', 'price', 'inventory']
        #useful when you need to add something to the fields/renaming

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields ='__all__'
