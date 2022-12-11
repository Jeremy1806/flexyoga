from django.shortcuts import render
from rest_framework.decorators import api_view
from enroll.models import People
from .serializer import PeopleSerializer
from datetime import datetime
from rest_framework.response import Response
# Create your views here.


@api_view(['PUT'])
def make_payment(request,  **kwargs):
    email = request.data.get('email', None)

    if email is not None:
        print("STARTTTTT")
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

    # email = request.data.get("email")

    # person = People.objects.filter(email__contains=email)
    # print(person.values())
    # # new user trying to pay fee {ok
    # if person.exists() is False:
    #     return Response({"msg": "User is new , Please do the enrollment "})
    # # print(person.values()[0])
    # json_data = person.values()[0]
    # # request.data['id'] = json_data.get('id')
    # # print(json_data.get('fees'))
    # fees_paid = json_data.get('fees')
    # old_date = json_data.get('date')

    # if fees_paid is False:
    #     request.data['fees'] = True
    #     request.data['date'] = datetime.now()
    #     print(request.data)
    #     temp = []
    #     temp.append(request.data)
    #     serializer = PeopleSerializer(person, data=temp, many=True)
    #     print("testing........")
    #     # print(serializer.is_valid)
    #     if serializer.is_valid():
    #         print("working")
    #         serializer.save()
    #     else:
    #         return Response({"msg": "Fee Paid1", "data": serializer.data})
