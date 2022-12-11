from django.shortcuts import render
from rest_framework.decorators import api_view
from enroll.models import People
from .serializer import PeopleSerializer
from datetime import datetime
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def create(request, **kwargs):
    email = request.data.get('email', None)
    if email is not None:
        try:
            person = People.objects.get(email=email)
            return Response({"success": False, "message": "Customer already exists with given Email"})
        except:

            people_serializer = PeopleSerializer(data=request.data)
            people_serializer.is_valid(raise_exception=True)
            try:
                people_serializer.save()
                check = People.objects.get(email=email)
                return Response({"success": True, "message": f"Customer created with Email : {check.email}"})
            except:
                return Response({"message": "Server Error"})


@api_view(['PUT'])
def make_payment(request,  **kwargs):
    email = request.data.get('email', None)

    if email is not None:
        try:
            person = People.objects.get(email=email)
        except:
            return Response({"msg": "User is new , Please do the enrollment "})
        print(person.email)
        fees_paid = person.fees
        old_date = person.date

        if fees_paid:
            return Response({"message": "Fees Already Paid"})
        else:
            person.fees = True
            person.date = datetime.now()
            person.save()

        return Response({"email": email, "fee": person.fees, "date_paid": person.date})
