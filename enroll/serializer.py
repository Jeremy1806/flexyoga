from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ("name", "age", "email", "batch", "date", "fees")


# class PaymentSerializer(PeopleSerializer):
#     def validate(self, data):
#         exception_fields = ('name', 'age', 'email')
#         return data

#     def update(self, instance, validated_data):
#         if validated_data.get('fees') == 'Yes':
