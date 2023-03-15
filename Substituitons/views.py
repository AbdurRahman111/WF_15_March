from django.shortcuts import render, HttpResponse
from .models import Substituitons_Model
from . serializers import Substituitons_Model_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from Event.models import Event_Model

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

@csrf_exempt
def find_individual_id(request):
    if request.method == "POST":

        id = request.POST.get('id')

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')


        event_id = request.POST.get('event_id')
        player_name = request.POST.get('player_name')
        substituitons_Name = request.POST.get('substituitons_Name')


        find_substituitons_with_event_id = request.POST.get('find_substituitons_with_event_id')


        if Process == 'see':
            get_info = Substituitons_Model.objects.filter(id=id)
            if get_info:
                get_spacific_info = Substituitons_Model.objects.get(id=id)
                serializer_var = Substituitons_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')

        if Process == 'see_with_event':
            if find_substituitons_with_event_id:
                get_spacific_info = Substituitons_Model.objects.filter(Event_for_goal=find_substituitons_with_event_id)
                serializer_var = Substituitons_Model_serializer(get_spacific_info, many=True)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')



        if user_name and password:

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:
                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'create' and get_user_info.User_Roll =='Operations':
                        get_event_spacific=''
                        if event_id:
                            get_event = Event_Model.objects.filter(id=event_id)
                            if get_event:
                                get_event_spacific = Event_Model.objects.get(id=event_id)


                        if get_event_spacific and player_name and substituitons_Name:

                            get_spacific_info = Substituitons_Model(Event_for_goal=get_event_spacific, PLayer_Name=player_name, Substituitons_Name = substituitons_Name)
                            get_spacific_info.save()
                            mag = {'massage':'Data is Created'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')


                    elif Process == 'create' and get_user_info.User_Roll =='Admin':
                        get_event_spacific = ''
                        if event_id:
                            get_event = Event_Model.objects.filter(id=event_id)
                            if get_event:
                                get_event_spacific = Event_Model.objects.get(id=event_id)

                        if get_event_spacific and player_name and substituitons_Name:
                            get_spacific_info = Substituitons_Model(Event_for_goal=get_event_spacific, PLayer_Name=player_name, Substituitons_Name=substituitons_Name)
                            get_spacific_info.save()
                            mag = {'massage': 'Data is Created'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')
                    else:
                        HttpResponse('NOT VALID')

                else:
                    HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')
