from django.shortcuts import redirect
from applift import views
from .models import Message

def message_view(request):

    if request.method == 'POST' :

        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        adress_start = request.POST.get('adress_start')
        stage_start = request.POST.get('stage_start')
        adress_arrived = request.POST.get('adress_arrived')
        stage_arrived = request.POST.get('stage_arrived')
        message = request.POST.get('message')

        Message.objects.create(
            last_name = last_name,
            first_name = first_name,
            telephone = telephone,
            email = email,
            adress_start = adress_start,
            stage_start = stage_start,
            adress_arrived = adress_arrived,
            stage_arrived = stage_arrived,
            message = message,
        )




    return redirect('/')