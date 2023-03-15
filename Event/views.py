from django.shortcuts import render, HttpResponse
from . models import Event_Model
from . serializers import Event_Model_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import datetime

from django.contrib.auth.hashers import make_password, check_password

@csrf_exempt
def find_individual_id(request):
    if request.method == "POST":

        id = request.POST.get('id')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        # password = make_password(password1)

        updated_data_id = request.POST.get('updated_data_id')

        home_team_name = request.POST.get('home_team_name')
        way_team_name = request.POST.get('way_team_name')
        stadium_name = request.POST.get('stadium_name')

        event_logo = request.FILES.get('event_logo')
        datetime = request.POST.get('datetime')

        # Process are delete, update, create, see
        Process = request.POST.get('Process')

        if Process == 'see':
            get_info = Event_Model.objects.filter(id=id)
            if get_info:
                get_spacific_info = Event_Model.objects.get(id=id)
                print('get_spacific_info.Event_Date_Time')
                print(get_spacific_info.Event_Date_Time)
                serializer_var =Event_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')

        if Process == 'see_latest':
            import datetime

            now=datetime.datetime.now()

            get_info = Event_Model.objects.filter(Event_Date_Time__range=[now, "2030-01-31 11:32:58.194644"])
            dd = Event_Model.objects.order_by('-Event_Date_Time').first().Event_Date_Time
            print('dd')
            print(dd)
            print('dd')
            if get_info:
                get_spacific_info = Event_Model.objects.filter(Event_Date_Time__range=[now, "2030-01-31 11:32:58.194644"])
                serializer_var =Event_Model_serializer(get_spacific_info, many=True)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')



        if user_name and password:

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:
                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'delete':
                        get_info = Event_Model.objects.filter(id=id)
                        if get_info:
                            instance = Event_Model.objects.get(id=id)
                            instance.delete()
                            mag = {'massage':'Data Deleted'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')

                    elif Process == 'create':
                        if home_team_name and way_team_name and stadium_name and datetime:
                            get_spacific_info = Event_Model(Home_Team=home_team_name, Way_Team=way_team_name, Stadium_Name=stadium_name, Event_Logo=event_logo, Event_Date_Time=datetime)
                            get_spacific_info.save()
                            mag = {'massage':'Data is Created'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')

                    elif Process == 'update':
                        if home_team_name or way_team_name or stadium_name:
                            get_info = Event_Model.objects.filter(id=updated_data_id)
                            if get_info:
                                get_spacific_info = Event_Model.objects.get(id=updated_data_id)
                                if home_team_name:
                                    get_spacific_info.Home_Team = home_team_name
                                if way_team_name:
                                    get_spacific_info.Way_Team = way_team_name
                                if stadium_name:
                                    get_spacific_info.Stadium_Name = stadium_name
                                get_spacific_info.save()
                            mag = {'massage':'Data is Updated'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')
                    else:
                        HttpResponse('NOT VALID')
                else:
                    HttpResponse('NOT VALID')


    return HttpResponse('NO GET METHOD ALLOWED')

@csrf_exempt
def find_all(request):
    if request.method == "POST":
        # Process are  see
        Process = request.POST.get('Process')

        if Process == 'see':
            get_spacific_info = Event_Model.objects.all()
            serializer_var =Event_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)


            import json
            print(type(json.loads(json_data)))


            return HttpResponse(json_data, content_type='application/json')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


