from rest_framework.decorators import api_view
from enroll.models import People
from .serializer import PeopleSerializer
from datetime import datetime
from rest_framework.response import Response
# Create your views here.


@api_view(['POST'])
def create(request, **kwargs):
    request = request.data['body']
    print(request['email'])
    email = request.get('email', None)
    if email is not None:
        try:
            person = People.objects.get(email=email)
            return Response({"success": False, "message": "Customer already exists with given Email"})
        except:

            people_serializer = PeopleSerializer(data=request)
            people_serializer.is_valid(raise_exception=True)
            try:
                people_serializer.save()
                check = People.objects.get(email=email)
                return Response({"success": True, "message": f"Customer created with Email : {check.email}"})
            except:
                return Response({"message": "Server Error"})


@api_view(['PUT'])
def make_payment(request,  **kwargs):
    request = request.data['body']
    print(request['email'])
    email = request.get('email', None)

    if email is not None:
        try:
            person = People.objects.get(email=email)
        except:
            return Response({"msg": "User is new , Please do the enrollment "})
        print(person.email)
        fees_paid = person.fees
        old_date = person.fee_date

        if fees_paid:
            return Response({"message": "Fees Already Paid"})
        elif old_date.month != datetime.now().month:
            person.fees = True
            person.fee_date = datetime.now()
            person.save()
        else:
            return Response({"message": "Fees Already Paid"})

        return Response({"success": True, "message": "Fees paid successfully"})


@api_view(['PUT'])
def update_batch(request, **kwargs):
    request = request.data['body']
    print(request['email'])
    email = request.get('email', None)
    batch = request.get('batch', None)

    if not batch or not email:
        return Response({"success": False, "message": "Email or batch missing from request"})

    person = People.objects.get(email=email)
    last_changed = person.date
    print(last_changed)
    today = datetime.now()

    if today.month != last_changed.month:
        person.date = today
        person.batch = request.get("batch")
        person.save()
        return Response({"success": True, "message": "Your batch has been changed"})
    else:
        return Response({"success": False, "message": "You cannot change batch this month"})
