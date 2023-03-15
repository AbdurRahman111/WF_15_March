from django.shortcuts import render, HttpResponse
from .models import Goal_Model
from . serializers import Goal_Model_serializer
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
        goal_add_team_name = request.POST.get('goal_add_team_name')
        scorer_name = request.POST.get('scorer_name')
        scorer_assist_name = request.POST.get('scorer_assist_name')

        find_goal_with_event_id = request.POST.get('find_goal_with_event_id')


        if Process == 'see':
            get_info = Goal_Model.objects.filter(id=id)
            if get_info:
                get_spacific_info = Goal_Model.objects.get(id=id)
                serializer_var = Goal_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')

        if Process == 'see_with_event':
            if find_goal_with_event_id:
                get_spacific_info = Goal_Model.objects.filter(Event_for_goal=find_goal_with_event_id)
                serializer_var = Goal_Model_serializer(get_spacific_info, many=True)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')



        if user_name and password:

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:
                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):
                    print('get_user_info.User_Roll')
                    print(get_user_info.User_Roll)
                    print('get_user_info.User_Roll')

                    if Process == 'create' and get_user_info.User_Roll =='Operations':
                        print('opppre')
                        get_event_spacific=''
                        home_taem=''
                        way_taem=''
                        if event_id:
                            get_event = Event_Model.objects.filter(id=event_id)
                            if get_event:
                                get_event_spacific = Event_Model.objects.get(id=event_id)
                                home_taem = get_event_spacific.Home_Team
                                way_taem = get_event_spacific.Way_Team

                        if get_event_spacific and goal_add_team_name and scorer_name and scorer_assist_name and home_taem and way_taem:

                            if goal_add_team_name == home_taem:
                                get_spacific_info = Goal_Model(Event_for_goal=get_event_spacific, Home_Team_Goal_Count_In_1='1', Way_Team_Goal_Count_In_1 = '0', Scorer_Name=scorer_name, Goal_Assist_Name=scorer_assist_name)
                                get_spacific_info.save()
                                mag = {'massage':'Data is Created'}
                                json_data = JSONRenderer().render(mag)
                                return HttpResponse(json_data, content_type='application/json')
                            elif goal_add_team_name == way_taem:
                                if goal_add_team_name == home_taem:
                                    get_spacific_info = Goal_Model(Event_for_goal=get_event_spacific, Home_Team_Goal_Count_In_1='0', Way_Team_Goal_Count_In_1 = '1', Scorer_Name=scorer_name, Goal_Assist_Name=scorer_assist_name)
                                    get_spacific_info.save()
                                    mag = {'massage': 'Data is Created'}
                                    json_data = JSONRenderer().render(mag)
                                    return HttpResponse(json_data, content_type='application/json')
                            else:
                                HttpResponse('NOT VALID')

                    elif Process == 'create' and get_user_info.User_Roll =='Admin':
                        print('admin')
                        get_event_spacific=''
                        home_taem=''
                        way_taem=''
                        if event_id:
                            get_event = Event_Model.objects.filter(id=event_id)
                            if get_event:
                                get_event_spacific = Event_Model.objects.get(id=event_id)
                                home_taem = get_event_spacific.Home_Team
                                way_taem = get_event_spacific.Way_Team

                        if get_event_spacific and goal_add_team_name and scorer_name and scorer_assist_name and home_taem and way_taem:

                            if goal_add_team_name == home_taem:
                                get_spacific_info = Goal_Model(Event_for_goal=get_event_spacific, Home_Team_Goal_Count_In_1='1', Way_Team_Goal_Count_In_1 = '0', Scorer_Name=scorer_name, Goal_Assist_Name=scorer_assist_name)
                                get_spacific_info.save()
                                mag = {'massage':'Data is Created'}
                                json_data = JSONRenderer().render(mag)
                                return HttpResponse(json_data, content_type='application/json')
                            elif goal_add_team_name == way_taem:
                                if goal_add_team_name == home_taem:
                                    get_spacific_info = Goal_Model(Event_for_goal=get_event_spacific, Home_Team_Goal_Count_In_1='0', Way_Team_Goal_Count_In_1 = '1', Scorer_Name=scorer_name, Goal_Assist_Name=scorer_assist_name)
                                    get_spacific_info.save()
                                    mag = {'massage': 'Data is Created'}
                                    json_data = JSONRenderer().render(mag)
                                    return HttpResponse(json_data, content_type='application/json')
                            else:
                                HttpResponse('NOT VALID')
                    else:
                        HttpResponse('NOT VALID')




                else:
                    HttpResponse('NOT VALID')


    return HttpResponse('NO GET METHOD ALLOWED')
