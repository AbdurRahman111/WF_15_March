from django.shortcuts import render, HttpResponse
from .models import Team_Model
from . serializers import Team_Model_serializer
from User_info.serializers import find_manager_information_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from Event.models import Event_Model

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from Player.models import Player_Model

@csrf_exempt
def find_all_team(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        if Process == 'see_all_team':
            get_spacific_info = Team_Model.objects.all()
            serializer_var = Team_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')


        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def delete_team(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        delete_team_id = request.POST.get('delete_team_id')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'delete' and get_user_info.User_Roll == 'Admin' and delete_team_id:
                        see = Team_Model.objects.filter(id=delete_team_id)
                        if see:
                            get_q_set = Team_Model.objects.get(id=delete_team_id)
                            get_q_set.delete()

                            mag = {'massage': 'Data is Deleted'}
                            mag = {'massage': 'Data is Deleted'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')
                        else:
                            HttpResponse('NOT VALID')

                    elif Process == 'delete' and get_user_info.User_Roll == 'Manager' and delete_team_id:
                        see = Team_Model.objects.filter(id=delete_team_id)
                        if see:
                            get_q_set = Team_Model.objects.get(id=delete_team_id)
                            get_q_set.delete()

                            mag = {'massage': 'Data is Deleted'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')
                        else:
                            HttpResponse('NOT VALID')

                    elif Process == 'delete' and get_user_info.User_Roll == 'Operations' and delete_team_id:
                        see = Team_Model.objects.filter(id=delete_team_id)
                        if see:
                            get_q_set = Team_Model.objects.get(id=delete_team_id)
                            get_q_set.delete()

                            mag = {'massage': 'Data is Deleted'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')
                        else:
                            HttpResponse('NOT VALID')


                    else:
                        HttpResponse('NOT VALID')
                else:
                    HttpResponse('NOT VALID')
            else:
                HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def find_team_with_id(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        specific_id = request.POST.get('specific_id')

        if Process == 'find_team_with_id' and specific_id:
            get_spacifi = Team_Model.objects.filter(id = specific_id)
            if get_spacifi:
                get_spacific_info = Team_Model.objects.get(id = specific_id)
                serializer_var = Team_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')

            else:
                HttpResponse('NOT VALID')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def find_team_with_team_name(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        team_name = request.POST.get('team_name')

        if Process == 'find_team_with_team_name' and team_name:
            get_spacifi = Team_Model.objects.filter(Team_Name=team_name)
            if get_spacifi:
                get_spacific_info = Team_Model.objects.get(Team_Name=team_name)
                serializer_var = Team_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')

            else:
                HttpResponse('NOT VALID')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')



@csrf_exempt
def find_all_manager(request):
    if request.method == "POST":
        Process = request.POST.get('Process')


        if Process == 'find_all_manager':
            user_info = User_information.objects.filter(User_Roll='Manager')
            serializer_var = find_manager_information_serializer(user_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')


        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def create_specific_taem(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        if_admin_then_manager_user_id = request.POST.get('if_admin_then_manager_user_id')


        player_1_id = request.POST.get('player_1_id')
        player_2_id = request.POST.get('player_2_id')
        player_3_id = request.POST.get('player_3_id')
        player_4_id = request.POST.get('player_4_id')
        player_5_id = request.POST.get('player_5_id')
        player_6_id = request.POST.get('player_6_id')
        player_7_id = request.POST.get('player_7_id')
        player_8_id = request.POST.get('player_8_id')
        player_9_id = request.POST.get('player_9_id')
        player_10_id = request.POST.get('player_10_id')
        player_11_id = request.POST.get('player_11_id')
        player_12_id = request.POST.get('player_12_id')
        player_13_id = request.POST.get('player_13_id')
        player_14_id = request.POST.get('player_14_id')
        player_15_id = request.POST.get('player_15_id')
        player_16_id = request.POST.get('player_16_id')
        player_17_id = request.POST.get('player_17_id')
        player_18_id = request.POST.get('player_18_id')

        # active player
        A_player_1_id = request.POST.get('A_player_1_id')
        A_player_2_id = request.POST.get('A_player_2_id')
        A_player_3_id = request.POST.get('A_player_3_id')
        A_player_4_id = request.POST.get('A_player_4_id')
        A_player_5_id = request.POST.get('A_player_5_id')
        A_player_6_id = request.POST.get('A_player_6_id')
        A_player_7_id = request.POST.get('A_player_7_id')
        A_player_8_id = request.POST.get('A_player_8_id')
        A_player_9_id = request.POST.get('A_player_9_id')
        A_player_10_id = request.POST.get('A_player_10_id')
        A_player_11_id = request.POST.get('A_player_11_id')

        # substatute  player
        S_player_1_id = request.POST.get('S_player_1_id')
        S_player_2_id = request.POST.get('S_player_2_id')
        S_player_3_id = request.POST.get('S_player_3_id')
        S_player_4_id = request.POST.get('S_player_4_id')
        S_player_5_id = request.POST.get('S_player_5_id')
        S_player_6_id = request.POST.get('S_player_6_id')
        S_player_7_id = request.POST.get('S_player_7_id')



        Team_Name = request.POST.get('Team_Name')
        Team_short_Name = request.POST.get('Team_short_Name')

        Team_Owner_Name = request.POST.get('Team_Owner_Name')

        Team_Total_play_count = request.POST.get('Team_Total_play_count')
        Win_count = request.POST.get('Win_count')
        Loos_count = request.POST.get('Loos_count')
        Drow_count = request.POST.get('Drow_count')
        GF = request.POST.get('GF')
        GA = request.POST.get('GA')
        PTS = request.POST.get('PTS')

        Team_Official_Link = request.POST.get('Team_Official_Link')

        Team_Logo = request.FILES.get('Team_Logo')
        Team_banner = request.FILES.get('Team_banner')
        Team_description = request.POST.get('Team_description')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):


                    if Process == 'create' and get_user_info.User_Roll =='Admin' and Team_Name and if_admin_then_manager_user_id:
                        manager_info = User_information.objects.filter(id = if_admin_then_manager_user_id)
                        manager_info_one=None
                        if manager_info:
                            manager_info_o = User_information.objects.get(id=if_admin_then_manager_user_id)
                            if manager_info_o.User_Roll == 'Manager':
                                manager_info_one = manager_info_o

                        # get_spacific_info = Team_Model(Manager=manager_info_one, Team_player_1_id_from_Plyer_model=player_1, Team_player_2_id_from_Plyer_model=player_2,  Team_player_3_id_from_Plyer_model=player_3, Team_player_4_id_from_Plyer_model=player_4, Team_player_5_id_from_Plyer_model=player_5, Team_player_6_id_from_Plyer_model=player_6, Team_player_7_id_from_Plyer_model=player_7, Team_player_8_id_from_Plyer_model=player_8, Team_player_9_id_from_Plyer_model=player_9, Team_player_10_id_from_Plyer_model=player_10, Team_player_11_id_from_Plyer_model=player_11, Team_player_12_id_from_Plyer_model=player_12, Team_player_13_id_from_Plyer_model=player_13, Team_player_14_id_from_Plyer_model=player_14, Team_player_15_id_from_Plyer_model=player_15, Team_player_active_1_id_from_Plyer_model=A_player_1, Team_player_active_2_id_from_Plyer_model=A_player_2, Team_player_active_3_id_from_Plyer_model=A_player_3, Team_player_active_4_id_from_Plyer_model=A_player_4, Team_player_active_5_id_from_Plyer_model=A_player_5, Team_player_active_6_id_from_Plyer_model=A_player_6, Team_player_active_7_id_from_Plyer_model=A_player_7, Team_player_active_8_id_from_Plyer_model=A_player_8, Team_player_active_9_id_from_Plyer_model=A_player_9, Team_player_active_10_id_from_Plyer_model=A_player_10, Team_player_active_11_id_from_Plyer_model=A_player_11, Team_player_substitute_1_id_from_Plyer_model=S_player_1, Team_player_substitute_2_id_from_Plyer_model=S_player_2, Team_player_substitute_3_id_from_Plyer_model=S_player_3, Team_player_substitute_4_id_from_Plyer_model=S_player_4, Team_Name=Team_Name, Team_Owner_Name=Team_Owner_Name, Team_Official_Link=Team_Official_Link, Team_Logo=Team_Logo)

                        palyer_1 = None
                        if player_1_id:
                            is_present_1 = Player_Model.objects.filter(id=player_1_id)
                            if is_present_1:
                                palyer_1 = Player_Model.objects.get(id=player_1_id)

                        palyer_2 = None
                        if player_1_id:
                            is_present_2 = Player_Model.objects.filter(id=player_2_id)
                            if is_present_2:
                                palyer_2 = Player_Model.objects.get(id=player_2_id)

                        palyer_3 = None
                        if player_3_id:
                            is_present_3 = Player_Model.objects.filter(id=player_3_id)
                            if is_present_3:
                                palyer_3 = Player_Model.objects.get(id=player_3_id)

                        palyer_4 = None
                        if player_4_id:
                            is_present_4 = Player_Model.objects.filter(id=player_4_id)
                            if is_present_4:
                                palyer_4 = Player_Model.objects.get(id=player_4_id)

                        palyer_5 = None
                        if player_5_id:
                            is_present_5 = Player_Model.objects.filter(id=player_5_id)
                            if is_present_5:
                                palyer_5 = Player_Model.objects.get(id=player_5_id)

                        palyer_6 = None
                        if player_6_id:
                            is_present_6 = Player_Model.objects.filter(id=player_6_id)
                            if is_present_6:
                                palyer_6 = Player_Model.objects.get(id=player_6_id)

                        palyer_7 = None
                        if player_7_id:
                            is_present_7 = Player_Model.objects.filter(id=player_7_id)
                            if is_present_7:
                                palyer_7 = Player_Model.objects.get(id=player_7_id)

                        palyer_8 = None
                        if player_8_id:
                            is_present_8 = Player_Model.objects.filter(id=player_8_id)
                            if is_present_8:
                                palyer_8 = Player_Model.objects.get(id=player_8_id)

                        palyer_9 = None
                        if player_9_id:
                            is_present_9 = Player_Model.objects.filter(id=player_9_id)
                            if is_present_9:
                                palyer_9 = Player_Model.objects.get(id=player_9_id)

                        palyer_10 = None
                        if player_10_id:
                            is_present_10 = Player_Model.objects.filter(id=player_10_id)
                            if is_present_10:
                                palyer_10 = Player_Model.objects.get(id=player_10_id)

                        palyer_11 = None
                        if player_11_id:
                            is_present_11 = Player_Model.objects.filter(id=player_11_id)
                            if is_present_11:
                                palyer_11 = Player_Model.objects.get(id=player_11_id)

                        palyer_12 = None
                        if player_12_id:
                            is_present_12 = Player_Model.objects.filter(id=player_12_id)
                            if is_present_12:
                                palyer_12 = Player_Model.objects.get(id=player_12_id)

                        palyer_13 = None
                        if player_13_id:
                            is_present_13 = Player_Model.objects.filter(id=player_13_id)
                            if is_present_13:
                                palyer_13 = Player_Model.objects.get(id=player_13_id)

                        palyer_14 = None
                        if player_14_id:
                            is_present_14 = Player_Model.objects.filter(id=player_14_id)
                            if is_present_14:
                                palyer_14 = Player_Model.objects.get(id=player_14_id)

                        palyer_15 = None
                        if player_15_id:
                            is_present_15 = Player_Model.objects.filter(id=player_15_id)
                            if is_present_15:
                                palyer_15 = Player_Model.objects.get(id=player_15_id)

                        palyer_16 = None
                        if player_16_id:
                            is_present_16 = Player_Model.objects.filter(id=player_16_id)
                            if is_present_16:
                                palyer_16 = Player_Model.objects.get(id=player_16_id)

                        palyer_17 = None
                        if player_17_id:
                            is_present_17 = Player_Model.objects.filter(id=player_17_id)
                            if is_present_17:
                                palyer_17 = Player_Model.objects.get(id=player_17_id)

                        palyer_18 = None
                        if player_18_id:
                            is_present_18 = Player_Model.objects.filter(id=player_18_id)
                            if is_present_18:
                                palyer_18 = Player_Model.objects.get(id=player_18_id)

                        a_palyer_1 = None
                        if A_player_1_id:
                            a_is_present_1 = Player_Model.objects.filter(id=A_player_1_id)
                            if a_is_present_1:
                                a_palyer_1 = Player_Model.objects.get(id=A_player_1_id)



                        a_palyer_2 = None
                        if A_player_2_id:
                            a_is_present_2 = Player_Model.objects.filter(id=A_player_2_id)
                            if a_is_present_2:
                                a_palyer_2 = Player_Model.objects.get(id=A_player_2_id)



                        a_palyer_3 = None
                        if A_player_3_id:
                            a_is_present_3 = Player_Model.objects.filter(id=A_player_3_id)
                            if a_is_present_3:
                                a_palyer_3 = Player_Model.objects.get(id=A_player_3_id)



                        a_palyer_4 = None
                        if A_player_4_id:
                            a_is_present_4 = Player_Model.objects.filter(id=A_player_4_id)
                            if a_is_present_4:
                                a_palyer_4 = Player_Model.objects.get(id=A_player_4_id)



                        a_palyer_5 = None
                        if A_player_5_id:
                            a_is_present_5 = Player_Model.objects.filter(id=A_player_5_id)
                            if a_is_present_5:
                                a_palyer_5 = Player_Model.objects.get(id=A_player_5_id)



                        a_palyer_6 = None
                        if A_player_6_id:
                            a_is_present_6 = Player_Model.objects.filter(id=A_player_6_id)
                            if a_is_present_6:
                                a_palyer_6 = Player_Model.objects.get(id=A_player_6_id)



                        a_palyer_7 = None
                        if A_player_7_id:
                            a_is_present_7 = Player_Model.objects.filter(id=A_player_7_id)
                            if a_is_present_7:
                                a_palyer_7 = Player_Model.objects.get(id=A_player_7_id)



                        a_palyer_8 = None
                        if A_player_8_id:
                            a_is_present_8 = Player_Model.objects.filter(id=A_player_8_id)
                            if a_is_present_8:
                                a_palyer_8 = Player_Model.objects.get(id=A_player_8_id)



                        a_palyer_9 = None
                        if A_player_9_id:
                            a_is_present_9 = Player_Model.objects.filter(id=A_player_9_id)
                            if a_is_present_9:
                                a_palyer_9 = Player_Model.objects.get(id=A_player_9_id)



                        a_palyer_10 = None
                        if A_player_10_id:
                            a_is_present_10 = Player_Model.objects.filter(id=A_player_10_id)
                            if a_is_present_10:
                                a_palyer_10 = Player_Model.objects.get(id=A_player_10_id)



                        a_palyer_11 = None
                        if A_player_11_id:
                            a_is_present_11 = Player_Model.objects.filter(id=A_player_11_id)
                            if a_is_present_11:
                                a_palyer_11 = Player_Model.objects.get(id=A_player_11_id)


                        s_palyer_1 = None
                        if S_player_1_id:
                            s_is_present_1 = Player_Model.objects.filter(id=S_player_1_id)
                            if s_is_present_1:
                                s_palyer_1 = Player_Model.objects.get(id=S_player_1_id)





                        s_palyer_2 = None
                        if S_player_2_id:
                            s_is_present_2 = Player_Model.objects.filter(id=S_player_2_id)
                            if s_is_present_2:
                                s_palyer_2 = Player_Model.objects.get(id=S_player_2_id)





                        s_palyer_3 = None
                        if S_player_3_id:
                            s_is_present_3 = Player_Model.objects.filter(id=S_player_3_id)
                            if s_is_present_3:
                                s_palyer_3 = Player_Model.objects.get(id=S_player_3_id)





                        s_palyer_4 = None
                        if S_player_4_id:
                            s_is_present_4 = Player_Model.objects.filter(id=S_player_4_id)
                            if s_is_present_4:
                                s_palyer_4 = Player_Model.objects.get(id=S_player_4_id)





                        s_palyer_5 = None
                        if S_player_5_id:
                            s_is_present_5 = Player_Model.objects.filter(id=S_player_5_id)
                            if s_is_present_5:
                                s_palyer_5 = Player_Model.objects.get(id=S_player_5_id)





                        s_palyer_6 = None
                        if S_player_6_id:
                            s_is_present_6 = Player_Model.objects.filter(id=S_player_6_id)
                            if s_is_present_6:
                                s_palyer_6 = Player_Model.objects.get(id=S_player_6_id)





                        s_palyer_7 = None
                        if S_player_7_id:
                            s_is_present_7 = Player_Model.objects.filter(id=S_player_7_id)
                            if s_is_present_7:
                                s_palyer_7 = Player_Model.objects.get(id=S_player_7_id)




                        get_spacific_info = Team_Model(Manager=manager_info_one, Team_player_1_id_from_Plyer_model=palyer_1, Team_player_2_id_from_Plyer_model=palyer_2,  Team_player_3_id_from_Plyer_model=palyer_3, Team_player_4_id_from_Plyer_model=palyer_4, Team_player_5_id_from_Plyer_model=palyer_5, Team_player_6_id_from_Plyer_model=palyer_6, Team_player_7_id_from_Plyer_model=palyer_7, Team_player_8_id_from_Plyer_model=palyer_8, Team_player_9_id_from_Plyer_model=palyer_9, Team_player_10_id_from_Plyer_model=palyer_10, Team_player_11_id_from_Plyer_model=palyer_11, Team_player_12_id_from_Plyer_model=palyer_12, Team_player_13_id_from_Plyer_model=palyer_13, Team_player_14_id_from_Plyer_model=palyer_14, Team_player_15_id_from_Plyer_model=palyer_15, Team_player_16_id_from_Plyer_model=palyer_16, Team_player_17_id_from_Plyer_model=palyer_17, Team_player_18_id_from_Plyer_model=palyer_18, Team_player_active_1_id_from_Plyer_model=a_palyer_1, Team_player_active_2_id_from_Plyer_model=a_palyer_2, Team_player_active_3_id_from_Plyer_model=a_palyer_3, Team_player_active_4_id_from_Plyer_model=a_palyer_4, Team_player_active_5_id_from_Plyer_model=a_palyer_5, Team_player_active_6_id_from_Plyer_model=a_palyer_6, Team_player_active_7_id_from_Plyer_model=a_palyer_7, Team_player_active_8_id_from_Plyer_model=a_palyer_8, Team_player_active_9_id_from_Plyer_model=a_palyer_9, Team_player_active_10_id_from_Plyer_model=a_palyer_10, Team_player_active_11_id_from_Plyer_model=a_palyer_11, Team_player_substitute_1_id_from_Plyer_model=s_palyer_1, Team_player_substitute_2_id_from_Plyer_model=s_palyer_2, Team_player_substitute_3_id_from_Plyer_model=s_palyer_3, Team_player_substitute_4_id_from_Plyer_model=s_palyer_4, Team_player_substitute_5_id_from_Plyer_model=s_palyer_5, Team_player_substitute_6_id_from_Plyer_model=s_palyer_6, Team_player_substitute_7_id_from_Plyer_model=s_palyer_7, Team_Name=Team_Name, Team_short_Name=Team_short_Name,  Team_Owner_Name=Team_Owner_Name, Team_Official_Link=Team_Official_Link, Team_Logo=Team_Logo, Team_banner=Team_banner, Team_description=Team_description)
                        get_spacific_info.save()

                        mag = {'massage': 'Data is Created'}
                        json_data = JSONRenderer().render(mag)
                        return HttpResponse(json_data, content_type='application/json')

                    elif Process == 'create' and get_user_info.User_Roll =='Manager' and Team_Name:

                        manager_info = User_information.objects.filter(id=get_user_info.id)
                        manager_info_one = None
                        if manager_info:
                            manager_info_one = User_information.objects.get(id=get_user_info.id)

                        # get_spacific_info = Team_Model(Manager=manager_info_one,
                        #                                Team_player_1_id_from_Plyer_model=player_1,
                        #                                Team_player_2_id_from_Plyer_model=player_2,
                        #                                Team_player_3_id_from_Plyer_model=player_3,
                        #                                Team_player_4_id_from_Plyer_model=player_4,
                        #                                Team_player_5_id_from_Plyer_model=player_5,
                        #                                Team_player_6_id_from_Plyer_model=player_6,
                        #                                Team_player_7_id_from_Plyer_model=player_7,
                        #                                Team_player_8_id_from_Plyer_model=player_8,
                        #                                Team_player_9_id_from_Plyer_model=player_9,
                        #                                Team_player_10_id_from_Plyer_model=player_10,
                        #                                Team_player_11_id_from_Plyer_model=player_11,
                        #                                Team_player_12_id_from_Plyer_model=player_12,
                        #                                Team_player_13_id_from_Plyer_model=player_13,
                        #                                Team_player_14_id_from_Plyer_model=player_14,
                        #                                Team_player_15_id_from_Plyer_model=player_15,
                        #                                Team_player_active_1_id_from_Plyer_model=A_player_1,
                        #                                Team_player_active_2_id_from_Plyer_model=A_player_2,
                        #                                Team_player_active_3_id_from_Plyer_model=A_player_3,
                        #                                Team_player_active_4_id_from_Plyer_model=A_player_4,
                        #                                Team_player_active_5_id_from_Plyer_model=A_player_5,
                        #                                Team_player_active_6_id_from_Plyer_model=A_player_6,
                        #                                Team_player_active_7_id_from_Plyer_model=A_player_7,
                        #                                Team_player_active_8_id_from_Plyer_model=A_player_8,
                        #                                Team_player_active_9_id_from_Plyer_model=A_player_9,
                        #                                Team_player_active_10_id_from_Plyer_model=A_player_10,
                        #                                Team_player_active_11_id_from_Plyer_model=A_player_11,
                        #                                Team_player_substitute_1_id_from_Plyer_model=S_player_1,
                        #                                Team_player_substitute_2_id_from_Plyer_model=S_player_2,
                        #                                Team_player_substitute_3_id_from_Plyer_model=S_player_3,
                        #                                Team_player_substitute_4_id_from_Plyer_model=S_player_4,
                        #                                Team_Name=Team_Name, Team_Owner_Name=Team_Owner_Name, Team_Official_Link=Team_Official_Link, Team_Logo=Team_Logo)
                        # get_spacific_info.save()

                        palyer_1 = None
                        if player_1_id:
                            is_present_1 = Player_Model.objects.filter(id=player_1_id)
                            if is_present_1:
                                palyer_1 = Player_Model.objects.get(id=player_1_id)

                        palyer_2 = None
                        if player_1_id:
                            is_present_2 = Player_Model.objects.filter(id=player_2_id)
                            if is_present_2:
                                palyer_2 = Player_Model.objects.get(id=player_2_id)

                        palyer_3 = None
                        if player_3_id:
                            is_present_3 = Player_Model.objects.filter(id=player_3_id)
                            if is_present_3:
                                palyer_3 = Player_Model.objects.get(id=player_3_id)

                        palyer_4 = None
                        if player_4_id:
                            is_present_4 = Player_Model.objects.filter(id=player_4_id)
                            if is_present_4:
                                palyer_4 = Player_Model.objects.get(id=player_4_id)

                        palyer_5 = None
                        if player_5_id:
                            is_present_5 = Player_Model.objects.filter(id=player_5_id)
                            if is_present_5:
                                palyer_5 = Player_Model.objects.get(id=player_5_id)

                        palyer_6 = None
                        if player_6_id:
                            is_present_6 = Player_Model.objects.filter(id=player_6_id)
                            if is_present_6:
                                palyer_6 = Player_Model.objects.get(id=player_6_id)

                        palyer_7 = None
                        if player_7_id:
                            is_present_7 = Player_Model.objects.filter(id=player_7_id)
                            if is_present_7:
                                palyer_7 = Player_Model.objects.get(id=player_7_id)

                        palyer_8 = None
                        if player_8_id:
                            is_present_8 = Player_Model.objects.filter(id=player_8_id)
                            if is_present_8:
                                palyer_8 = Player_Model.objects.get(id=player_8_id)

                        palyer_9 = None
                        if player_9_id:
                            is_present_9 = Player_Model.objects.filter(id=player_9_id)
                            if is_present_9:
                                palyer_9 = Player_Model.objects.get(id=player_9_id)

                        palyer_10 = None
                        if player_10_id:
                            is_present_10 = Player_Model.objects.filter(id=player_10_id)
                            if is_present_10:
                                palyer_10 = Player_Model.objects.get(id=player_10_id)

                        palyer_11 = None
                        if player_11_id:
                            is_present_11 = Player_Model.objects.filter(id=player_11_id)
                            if is_present_11:
                                palyer_11 = Player_Model.objects.get(id=player_11_id)

                        palyer_12 = None
                        if player_12_id:
                            is_present_12 = Player_Model.objects.filter(id=player_12_id)
                            if is_present_12:
                                palyer_12 = Player_Model.objects.get(id=player_12_id)

                        palyer_13 = None
                        if player_13_id:
                            is_present_13 = Player_Model.objects.filter(id=player_13_id)
                            if is_present_13:
                                palyer_13 = Player_Model.objects.get(id=player_13_id)

                        palyer_14 = None
                        if player_14_id:
                            is_present_14 = Player_Model.objects.filter(id=player_14_id)
                            if is_present_14:
                                palyer_14 = Player_Model.objects.get(id=player_14_id)

                        palyer_15 = None
                        if player_15_id:
                            is_present_15 = Player_Model.objects.filter(id=player_15_id)
                            if is_present_15:
                                palyer_15 = Player_Model.objects.get(id=player_15_id)

                        palyer_16 = None
                        if player_16_id:
                            is_present_16 = Player_Model.objects.filter(id=player_16_id)
                            if is_present_16:
                                palyer_16 = Player_Model.objects.get(id=player_16_id)

                        palyer_17 = None
                        if player_17_id:
                            is_present_17 = Player_Model.objects.filter(id=player_17_id)
                            if is_present_17:
                                palyer_17 = Player_Model.objects.get(id=player_17_id)

                        palyer_18 = None
                        if player_18_id:
                            is_present_18 = Player_Model.objects.filter(id=player_18_id)
                            if is_present_18:
                                palyer_18 = Player_Model.objects.get(id=player_18_id)

                        a_palyer_1 = None
                        if A_player_1_id:
                            a_is_present_1 = Player_Model.objects.filter(id=A_player_1_id)
                            if a_is_present_1:
                                a_palyer_1 = Player_Model.objects.get(id=A_player_1_id)

                        a_palyer_2 = None
                        if A_player_2_id:
                            a_is_present_2 = Player_Model.objects.filter(id=A_player_2_id)
                            if a_is_present_2:
                                a_palyer_2 = Player_Model.objects.get(id=A_player_2_id)

                        a_palyer_3 = None
                        if A_player_3_id:
                            a_is_present_3 = Player_Model.objects.filter(id=A_player_3_id)
                            if a_is_present_3:
                                a_palyer_3 = Player_Model.objects.get(id=A_player_3_id)

                        a_palyer_4 = None
                        if A_player_4_id:
                            a_is_present_4 = Player_Model.objects.filter(id=A_player_4_id)
                            if a_is_present_4:
                                a_palyer_4 = Player_Model.objects.get(id=A_player_4_id)

                        a_palyer_5 = None
                        if A_player_5_id:
                            a_is_present_5 = Player_Model.objects.filter(id=A_player_5_id)
                            if a_is_present_5:
                                a_palyer_5 = Player_Model.objects.get(id=A_player_5_id)

                        a_palyer_6 = None
                        if A_player_6_id:
                            a_is_present_6 = Player_Model.objects.filter(id=A_player_6_id)
                            if a_is_present_6:
                                a_palyer_6 = Player_Model.objects.get(id=A_player_6_id)

                        a_palyer_7 = None
                        if A_player_7_id:
                            a_is_present_7 = Player_Model.objects.filter(id=A_player_7_id)
                            if a_is_present_7:
                                a_palyer_7 = Player_Model.objects.get(id=A_player_7_id)

                        a_palyer_8 = None
                        if A_player_8_id:
                            a_is_present_8 = Player_Model.objects.filter(id=A_player_8_id)
                            if a_is_present_8:
                                a_palyer_8 = Player_Model.objects.get(id=A_player_8_id)

                        a_palyer_9 = None
                        if A_player_9_id:
                            a_is_present_9 = Player_Model.objects.filter(id=A_player_9_id)
                            if a_is_present_9:
                                a_palyer_9 = Player_Model.objects.get(id=A_player_9_id)

                        a_palyer_10 = None
                        if A_player_10_id:
                            a_is_present_10 = Player_Model.objects.filter(id=A_player_10_id)
                            if a_is_present_10:
                                a_palyer_10 = Player_Model.objects.get(id=A_player_10_id)

                        a_palyer_11 = None
                        if A_player_11_id:
                            a_is_present_11 = Player_Model.objects.filter(id=A_player_11_id)
                            if a_is_present_11:
                                a_palyer_11 = Player_Model.objects.get(id=A_player_11_id)

                        s_palyer_1 = None
                        if S_player_1_id:
                            s_is_present_1 = Player_Model.objects.filter(id=S_player_1_id)
                            if s_is_present_1:
                                s_palyer_1 = Player_Model.objects.get(id=S_player_1_id)

                        s_palyer_2 = None
                        if S_player_2_id:
                            s_is_present_2 = Player_Model.objects.filter(id=S_player_2_id)
                            if s_is_present_2:
                                s_palyer_2 = Player_Model.objects.get(id=S_player_2_id)

                        s_palyer_3 = None
                        if S_player_3_id:
                            s_is_present_3 = Player_Model.objects.filter(id=S_player_3_id)
                            if s_is_present_3:
                                s_palyer_3 = Player_Model.objects.get(id=S_player_3_id)

                        s_palyer_4 = None
                        if S_player_4_id:
                            s_is_present_4 = Player_Model.objects.filter(id=S_player_4_id)
                            if s_is_present_4:
                                s_palyer_4 = Player_Model.objects.get(id=S_player_4_id)

                        s_palyer_5 = None
                        if S_player_5_id:
                            s_is_present_5 = Player_Model.objects.filter(id=S_player_5_id)
                            if s_is_present_5:
                                s_palyer_5 = Player_Model.objects.get(id=S_player_5_id)

                        s_palyer_6 = None
                        if S_player_6_id:
                            s_is_present_6 = Player_Model.objects.filter(id=S_player_6_id)
                            if s_is_present_6:
                                s_palyer_6 = Player_Model.objects.get(id=S_player_6_id)

                        s_palyer_7 = None
                        if S_player_7_id:
                            s_is_present_7 = Player_Model.objects.filter(id=S_player_7_id)
                            if s_is_present_7:
                                s_palyer_7 = Player_Model.objects.get(id=S_player_7_id)

                        get_spacific_info = Team_Model(Manager=manager_info_one,
                                                       Team_player_1_id_from_Plyer_model=palyer_1,
                                                       Team_player_2_id_from_Plyer_model=palyer_2,
                                                       Team_player_3_id_from_Plyer_model=palyer_3,
                                                       Team_player_4_id_from_Plyer_model=palyer_4,
                                                       Team_player_5_id_from_Plyer_model=palyer_5,
                                                       Team_player_6_id_from_Plyer_model=palyer_6,
                                                       Team_player_7_id_from_Plyer_model=palyer_7,
                                                       Team_player_8_id_from_Plyer_model=palyer_8,
                                                       Team_player_9_id_from_Plyer_model=palyer_9,
                                                       Team_player_10_id_from_Plyer_model=palyer_10,
                                                       Team_player_11_id_from_Plyer_model=palyer_11,
                                                       Team_player_12_id_from_Plyer_model=palyer_12,
                                                       Team_player_13_id_from_Plyer_model=palyer_13,
                                                       Team_player_14_id_from_Plyer_model=palyer_14,
                                                       Team_player_15_id_from_Plyer_model=palyer_15,
                                                       Team_player_16_id_from_Plyer_model=palyer_16,
                                                       Team_player_17_id_from_Plyer_model=palyer_17,
                                                       Team_player_18_id_from_Plyer_model=palyer_18,
                                                       Team_player_active_1_id_from_Plyer_model=a_palyer_1,
                                                       Team_player_active_2_id_from_Plyer_model=a_palyer_2,
                                                       Team_player_active_3_id_from_Plyer_model=a_palyer_3,
                                                       Team_player_active_4_id_from_Plyer_model=a_palyer_4,
                                                       Team_player_active_5_id_from_Plyer_model=a_palyer_5,
                                                       Team_player_active_6_id_from_Plyer_model=a_palyer_6,
                                                       Team_player_active_7_id_from_Plyer_model=a_palyer_7,
                                                       Team_player_active_8_id_from_Plyer_model=a_palyer_8,
                                                       Team_player_active_9_id_from_Plyer_model=a_palyer_9,
                                                       Team_player_active_10_id_from_Plyer_model=a_palyer_10,
                                                       Team_player_active_11_id_from_Plyer_model=a_palyer_11,
                                                       Team_player_substitute_1_id_from_Plyer_model=s_palyer_1,
                                                       Team_player_substitute_2_id_from_Plyer_model=s_palyer_2,
                                                       Team_player_substitute_3_id_from_Plyer_model=s_palyer_3,
                                                       Team_player_substitute_4_id_from_Plyer_model=s_palyer_4,
                                                       Team_player_substitute_5_id_from_Plyer_model=s_palyer_5,
                                                       Team_player_substitute_6_id_from_Plyer_model=s_palyer_6,
                                                       Team_player_substitute_7_id_from_Plyer_model=s_palyer_7,
                                                       Team_Name=Team_Name, Team_short_Name=Team_short_Name, Team_Owner_Name=Team_Owner_Name,
                                                       Team_Official_Link=Team_Official_Link, Team_Logo=Team_Logo, Team_banner=Team_banner, Team_description=Team_description)
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



@csrf_exempt
def update_specific_taem(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        if_admin_then_manager_user_id = request.POST.get('if_admin_then_manager_user_id')


        player_1_id = request.POST.get('player_1_id')
        player_2_id = request.POST.get('player_2_id')
        player_3_id = request.POST.get('player_3_id')
        player_4_id = request.POST.get('player_4_id')
        player_5_id = request.POST.get('player_5_id')
        player_6_id = request.POST.get('player_6_id')
        player_7_id = request.POST.get('player_7_id')
        player_8_id = request.POST.get('player_8_id')
        player_9_id = request.POST.get('player_9_id')
        player_10_id = request.POST.get('player_10_id')
        player_11_id = request.POST.get('player_11_id')
        player_12_id = request.POST.get('player_12_id')
        player_13_id = request.POST.get('player_13_id')
        player_14_id = request.POST.get('player_14_id')
        player_15_id = request.POST.get('player_15_id')
        player_16_id = request.POST.get('player_16_id')
        player_17_id = request.POST.get('player_17_id')
        player_18_id = request.POST.get('player_18_id')

        # active player
        A_player_1_id = request.POST.get('A_player_1_id')
        A_player_2_id = request.POST.get('A_player_2_id')
        A_player_3_id = request.POST.get('A_player_3_id')
        A_player_4_id = request.POST.get('A_player_4_id')
        A_player_5_id = request.POST.get('A_player_5_id')
        A_player_6_id = request.POST.get('A_player_6_id')
        A_player_7_id = request.POST.get('A_player_7_id')
        A_player_8_id = request.POST.get('A_player_8_id')
        A_player_9_id = request.POST.get('A_player_9_id')
        A_player_10_id = request.POST.get('A_player_10_id')
        A_player_11_id = request.POST.get('A_player_11_id')

        # substatute  player
        S_player_1_id = request.POST.get('S_player_1_id')
        S_player_2_id = request.POST.get('S_player_2_id')
        S_player_3_id = request.POST.get('S_player_3_id')
        S_player_4_id = request.POST.get('S_player_4_id')
        S_player_5_id = request.POST.get('S_player_5_id')
        S_player_6_id = request.POST.get('S_player_6_id')
        S_player_7_id = request.POST.get('S_player_7_id')



        # Team_Name = request.POST.get('Team_Name')
        Team_short_Name = request.POST.get('Team_short_Name')

        Team_Owner_Name = request.POST.get('Team_Owner_Name')

        Team_Total_play_count = request.POST.get('Team_Total_play_count')
        Win_count = request.POST.get('Win_count')
        Loos_count = request.POST.get('Loos_count')
        Drow_count = request.POST.get('Drow_count')
        GF = request.POST.get('GF')
        GA = request.POST.get('GA')
        PTS = request.POST.get('PTS')

        Team_Official_Link = request.POST.get('Team_Official_Link')

        Team_Logo = request.FILES.get('Team_Logo')
        Team_banner = request.FILES.get('Team_banner')
        Team_description = request.POST.get('Team_description')

        Team_id = request.POST.get('Team_id')

        live_game_video_link = request.POST.get('live_game_video_link')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):


                    if Process == 'update' and get_user_info.User_Roll =='Admin' and Team_id and if_admin_then_manager_user_id:
                        manager_info = User_information.objects.filter(id = if_admin_then_manager_user_id)
                        manager_info_one=None
                        if manager_info:
                            manager_info_o = User_information.objects.get(id=if_admin_then_manager_user_id)
                            if manager_info_o.User_Roll == 'Manager':
                                manager_info_one = manager_info_o



                        palyer_1 = None
                        if player_1_id:
                            is_present_1 = Player_Model.objects.filter(id=player_1_id)
                            if is_present_1:
                                palyer_1 = Player_Model.objects.get(id=player_1_id)

                        palyer_2 = None
                        if player_1_id:
                            is_present_2 = Player_Model.objects.filter(id=player_2_id)
                            if is_present_2:
                                palyer_2 = Player_Model.objects.get(id=player_2_id)

                        palyer_3 = None
                        if player_3_id:
                            is_present_3 = Player_Model.objects.filter(id=player_3_id)
                            if is_present_3:
                                palyer_3 = Player_Model.objects.get(id=player_3_id)

                        palyer_4 = None
                        if player_4_id:
                            is_present_4 = Player_Model.objects.filter(id=player_4_id)
                            if is_present_4:
                                palyer_4 = Player_Model.objects.get(id=player_4_id)

                        palyer_5 = None
                        if player_5_id:
                            is_present_5 = Player_Model.objects.filter(id=player_5_id)
                            if is_present_5:
                                palyer_5 = Player_Model.objects.get(id=player_5_id)

                        palyer_6 = None
                        if player_6_id:
                            is_present_6 = Player_Model.objects.filter(id=player_6_id)
                            if is_present_6:
                                palyer_6 = Player_Model.objects.get(id=player_6_id)

                        palyer_7 = None
                        if player_7_id:
                            is_present_7 = Player_Model.objects.filter(id=player_7_id)
                            if is_present_7:
                                palyer_7 = Player_Model.objects.get(id=player_7_id)

                        palyer_8 = None
                        if player_8_id:
                            is_present_8 = Player_Model.objects.filter(id=player_8_id)
                            if is_present_8:
                                palyer_8 = Player_Model.objects.get(id=player_8_id)

                        palyer_9 = None
                        if player_9_id:
                            is_present_9 = Player_Model.objects.filter(id=player_9_id)
                            if is_present_9:
                                palyer_9 = Player_Model.objects.get(id=player_9_id)

                        palyer_10 = None
                        if player_10_id:
                            is_present_10 = Player_Model.objects.filter(id=player_10_id)
                            if is_present_10:
                                palyer_10 = Player_Model.objects.get(id=player_10_id)

                        palyer_11 = None
                        if player_11_id:
                            is_present_11 = Player_Model.objects.filter(id=player_11_id)
                            if is_present_11:
                                palyer_11 = Player_Model.objects.get(id=player_11_id)

                        palyer_12 = None
                        if player_12_id:
                            is_present_12 = Player_Model.objects.filter(id=player_12_id)
                            if is_present_12:
                                palyer_12 = Player_Model.objects.get(id=player_12_id)

                        palyer_13 = None
                        if player_13_id:
                            is_present_13 = Player_Model.objects.filter(id=player_13_id)
                            if is_present_13:
                                palyer_13 = Player_Model.objects.get(id=player_13_id)

                        palyer_14 = None
                        if player_14_id:
                            is_present_14 = Player_Model.objects.filter(id=player_14_id)
                            if is_present_14:
                                palyer_14 = Player_Model.objects.get(id=player_14_id)

                        palyer_15 = None
                        if player_15_id:
                            is_present_15 = Player_Model.objects.filter(id=player_15_id)
                            if is_present_15:
                                palyer_15 = Player_Model.objects.get(id=player_15_id)

                        palyer_16 = None
                        if player_16_id:
                            is_present_16 = Player_Model.objects.filter(id=player_16_id)
                            if is_present_16:
                                palyer_16 = Player_Model.objects.get(id=player_16_id)

                        palyer_17 = None
                        if player_17_id:
                            is_present_17 = Player_Model.objects.filter(id=player_17_id)
                            if is_present_17:
                                palyer_17 = Player_Model.objects.get(id=player_17_id)

                        palyer_18 = None
                        if player_18_id:
                            is_present_18 = Player_Model.objects.filter(id=player_18_id)
                            if is_present_18:
                                palyer_18 = Player_Model.objects.get(id=player_18_id)

                        a_palyer_1 = None
                        if A_player_1_id:
                            a_is_present_1 = Player_Model.objects.filter(id=A_player_1_id)
                            if a_is_present_1:
                                a_palyer_1 = Player_Model.objects.get(id=A_player_1_id)



                        a_palyer_2 = None
                        if A_player_2_id:
                            a_is_present_2 = Player_Model.objects.filter(id=A_player_2_id)
                            if a_is_present_2:
                                a_palyer_2 = Player_Model.objects.get(id=A_player_2_id)



                        a_palyer_3 = None
                        if A_player_3_id:
                            a_is_present_3 = Player_Model.objects.filter(id=A_player_3_id)
                            if a_is_present_3:
                                a_palyer_3 = Player_Model.objects.get(id=A_player_3_id)



                        a_palyer_4 = None
                        if A_player_4_id:
                            a_is_present_4 = Player_Model.objects.filter(id=A_player_4_id)
                            if a_is_present_4:
                                a_palyer_4 = Player_Model.objects.get(id=A_player_4_id)



                        a_palyer_5 = None
                        if A_player_5_id:
                            a_is_present_5 = Player_Model.objects.filter(id=A_player_5_id)
                            if a_is_present_5:
                                a_palyer_5 = Player_Model.objects.get(id=A_player_5_id)



                        a_palyer_6 = None
                        if A_player_6_id:
                            a_is_present_6 = Player_Model.objects.filter(id=A_player_6_id)
                            if a_is_present_6:
                                a_palyer_6 = Player_Model.objects.get(id=A_player_6_id)



                        a_palyer_7 = None
                        if A_player_7_id:
                            a_is_present_7 = Player_Model.objects.filter(id=A_player_7_id)
                            if a_is_present_7:
                                a_palyer_7 = Player_Model.objects.get(id=A_player_7_id)



                        a_palyer_8 = None
                        if A_player_8_id:
                            a_is_present_8 = Player_Model.objects.filter(id=A_player_8_id)
                            if a_is_present_8:
                                a_palyer_8 = Player_Model.objects.get(id=A_player_8_id)



                        a_palyer_9 = None
                        if A_player_9_id:
                            a_is_present_9 = Player_Model.objects.filter(id=A_player_9_id)
                            if a_is_present_9:
                                a_palyer_9 = Player_Model.objects.get(id=A_player_9_id)



                        a_palyer_10 = None
                        if A_player_10_id:
                            a_is_present_10 = Player_Model.objects.filter(id=A_player_10_id)
                            if a_is_present_10:
                                a_palyer_10 = Player_Model.objects.get(id=A_player_10_id)



                        a_palyer_11 = None
                        if A_player_11_id:
                            a_is_present_11 = Player_Model.objects.filter(id=A_player_11_id)
                            if a_is_present_11:
                                a_palyer_11 = Player_Model.objects.get(id=A_player_11_id)


                        s_palyer_1 = None
                        if S_player_1_id:
                            s_is_present_1 = Player_Model.objects.filter(id=S_player_1_id)
                            if s_is_present_1:
                                s_palyer_1 = Player_Model.objects.get(id=S_player_1_id)





                        s_palyer_2 = None
                        if S_player_2_id:
                            s_is_present_2 = Player_Model.objects.filter(id=S_player_2_id)
                            if s_is_present_2:
                                s_palyer_2 = Player_Model.objects.get(id=S_player_2_id)





                        s_palyer_3 = None
                        if S_player_3_id:
                            s_is_present_3 = Player_Model.objects.filter(id=S_player_3_id)
                            if s_is_present_3:
                                s_palyer_3 = Player_Model.objects.get(id=S_player_3_id)





                        s_palyer_4 = None
                        if S_player_4_id:
                            s_is_present_4 = Player_Model.objects.filter(id=S_player_4_id)
                            if s_is_present_4:
                                s_palyer_4 = Player_Model.objects.get(id=S_player_4_id)





                        s_palyer_5 = None
                        if S_player_5_id:
                            s_is_present_5 = Player_Model.objects.filter(id=S_player_5_id)
                            if s_is_present_5:
                                s_palyer_5 = Player_Model.objects.get(id=S_player_5_id)





                        s_palyer_6 = None
                        if S_player_6_id:
                            s_is_present_6 = Player_Model.objects.filter(id=S_player_6_id)
                            if s_is_present_6:
                                s_palyer_6 = Player_Model.objects.get(id=S_player_6_id)





                        s_palyer_7 = None
                        if S_player_7_id:
                            s_is_present_7 = Player_Model.objects.filter(id=S_player_7_id)
                            if s_is_present_7:
                                s_palyer_7 = Player_Model.objects.get(id=S_player_7_id)

                        is_present = Team_Model.objects.filter(id=Team_id)
                        if is_present:
                            is_present = Team_Model.objects.get(id=Team_id)

                            if manager_info_one and manager_info_one != None:
                                is_present.Manager=manager_info_one
                            if palyer_1 and palyer_1 != None:
                                is_present.Team_player_1_id_from_Plyer_model=palyer_1
                            if palyer_2 and palyer_2 != None:
                                is_present.Team_player_2_id_from_Plyer_model=palyer_2
                            if palyer_3 and palyer_3 != None:
                                is_present.Team_player_3_id_from_Plyer_model=palyer_3
                            if palyer_4 and palyer_4 != None:
                                is_present.Team_player_4_id_from_Plyer_model=palyer_4
                            if palyer_5 and palyer_5 != None:
                                is_present.Team_player_5_id_from_Plyer_model=palyer_5
                            if palyer_6 and palyer_6 != None:
                                is_present.Team_player_6_id_from_Plyer_model=palyer_6
                            if palyer_7 and palyer_7 != None:
                                is_present.Team_player_7_id_from_Plyer_model=palyer_7
                            if palyer_8 and palyer_8 != None:
                                is_present.Team_player_8_id_from_Plyer_model=palyer_8
                            if palyer_9 and palyer_9 != None:
                                is_present.Team_player_9_id_from_Plyer_model=palyer_9
                            if palyer_10 and palyer_10 != None:
                                is_present.Team_player_10_id_from_Plyer_model=palyer_10
                            if palyer_11 and palyer_11 != None:
                                is_present.Team_player_11_id_from_Plyer_model=palyer_11
                            if palyer_12 and palyer_12 != None:
                                is_present.Team_player_12_id_from_Plyer_model=palyer_12

                            if palyer_13 and palyer_13 != None:
                                is_present.Team_player_13_id_from_Plyer_model=palyer_13
                            if palyer_14 and palyer_14 != None:
                                is_present.Team_player_14_id_from_Plyer_model=palyer_14
                            if palyer_15 and palyer_15 != None:
                                is_present.Team_player_15_id_from_Plyer_model=palyer_15
                            if palyer_16 and palyer_16 != None:
                                is_present.Team_player_16_id_from_Plyer_model=palyer_16
                            if palyer_17 and palyer_17 != None:
                                is_present.Team_player_17_id_from_Plyer_model=palyer_17
                            if palyer_18 and palyer_18 != None:
                                is_present.Team_player_18_id_from_Plyer_model=palyer_18
                            if a_palyer_1 and a_palyer_1 != None:
                                is_present.Team_player_active_1_id_from_Plyer_model=a_palyer_1
                            if a_palyer_2 and a_palyer_2 != None:
                                is_present.Team_player_active_2_id_from_Plyer_model=a_palyer_2
                            if a_palyer_3 and a_palyer_3 != None:
                                is_present.Team_player_active_3_id_from_Plyer_model=a_palyer_3
                            if a_palyer_4 and a_palyer_4 != None:
                                is_present.Team_player_active_4_id_from_Plyer_model=a_palyer_4
                            if a_palyer_5 and a_palyer_5 != None:
                                is_present.Team_player_active_5_id_from_Plyer_model=a_palyer_5
                            if a_palyer_6 and a_palyer_6 != None:
                                is_present.Team_player_active_6_id_from_Plyer_model=a_palyer_6
                            if a_palyer_7 and a_palyer_7 != None:
                                is_present.Team_player_active_7_id_from_Plyer_model=a_palyer_7
                            if a_palyer_8 and a_palyer_8 != None:
                                is_present.Team_player_active_8_id_from_Plyer_model=a_palyer_8
                            if a_palyer_9 and a_palyer_9 != None:
                                is_present.Team_player_active_9_id_from_Plyer_model=a_palyer_9
                            if a_palyer_10 and a_palyer_10 != None:
                                is_present.Team_player_active_10_id_from_Plyer_model=a_palyer_10
                            if a_palyer_11 and a_palyer_11 != None:
                                is_present.Team_player_active_11_id_from_Plyer_model=a_palyer_11
                            if s_palyer_1 and s_palyer_1 != None:
                                is_present.Team_player_substitute_1_id_from_Plyer_model=s_palyer_1
                            if s_palyer_2 and s_palyer_2 != None:
                                is_present.Team_player_substitute_2_id_from_Plyer_model=s_palyer_2
                            if s_palyer_3 and s_palyer_3 != None:
                                is_present.Team_player_substitute_3_id_from_Plyer_model=s_palyer_3
                            if s_palyer_4 and s_palyer_4 != None:
                                is_present.Team_player_substitute_4_id_from_Plyer_model=s_palyer_4
                            if s_palyer_5 and s_palyer_5 != None:
                                is_present.Team_player_substitute_5_id_from_Plyer_model=s_palyer_5
                            if s_palyer_6 and s_palyer_6 != None:
                                is_present.Team_player_substitute_6_id_from_Plyer_model=s_palyer_6
                            if s_palyer_7 and s_palyer_7 != None:
                                is_present.Team_player_substitute_7_id_from_Plyer_model=s_palyer_7
                            if Team_short_Name:
                                is_present.Team_short_Name=Team_short_Name
                            if Team_Owner_Name:
                                is_present.Team_Owner_Name=Team_Owner_Name
                            if Team_Official_Link:
                                is_present.Team_Official_Link=Team_Official_Link
                            if Team_Logo:
                                is_present.Team_Logo=Team_Logo
                            if Team_banner:
                                is_present.Team_banner=Team_banner
                            if Team_description:
                                is_present.Team_description=Team_description
                            if live_game_video_link:
                                is_present.live_game_link=live_game_video_link
                            is_present.save()



                        mag = {'massage': 'Data is Updated'}
                        json_data = JSONRenderer().render(mag)
                        return HttpResponse(json_data, content_type='application/json')

                    elif Process == 'update' and get_user_info.User_Roll =='Operations' and Team_id and if_admin_then_manager_user_id:
                        manager_info = User_information.objects.filter(id = if_admin_then_manager_user_id)
                        manager_info_one=None
                        if manager_info:
                            manager_info_o = User_information.objects.get(id=if_admin_then_manager_user_id)
                            if manager_info_o.User_Roll == 'Manager':
                                manager_info_one = manager_info_o



                        palyer_1 = None
                        if player_1_id:
                            is_present_1 = Player_Model.objects.filter(id=player_1_id)
                            if is_present_1:
                                palyer_1 = Player_Model.objects.get(id=player_1_id)

                        palyer_2 = None
                        if player_1_id:
                            is_present_2 = Player_Model.objects.filter(id=player_2_id)
                            if is_present_2:
                                palyer_2 = Player_Model.objects.get(id=player_2_id)

                        palyer_3 = None
                        if player_3_id:
                            is_present_3 = Player_Model.objects.filter(id=player_3_id)
                            if is_present_3:
                                palyer_3 = Player_Model.objects.get(id=player_3_id)

                        palyer_4 = None
                        if player_4_id:
                            is_present_4 = Player_Model.objects.filter(id=player_4_id)
                            if is_present_4:
                                palyer_4 = Player_Model.objects.get(id=player_4_id)

                        palyer_5 = None
                        if player_5_id:
                            is_present_5 = Player_Model.objects.filter(id=player_5_id)
                            if is_present_5:
                                palyer_5 = Player_Model.objects.get(id=player_5_id)

                        palyer_6 = None
                        if player_6_id:
                            is_present_6 = Player_Model.objects.filter(id=player_6_id)
                            if is_present_6:
                                palyer_6 = Player_Model.objects.get(id=player_6_id)

                        palyer_7 = None
                        if player_7_id:
                            is_present_7 = Player_Model.objects.filter(id=player_7_id)
                            if is_present_7:
                                palyer_7 = Player_Model.objects.get(id=player_7_id)

                        palyer_8 = None
                        if player_8_id:
                            is_present_8 = Player_Model.objects.filter(id=player_8_id)
                            if is_present_8:
                                palyer_8 = Player_Model.objects.get(id=player_8_id)

                        palyer_9 = None
                        if player_9_id:
                            is_present_9 = Player_Model.objects.filter(id=player_9_id)
                            if is_present_9:
                                palyer_9 = Player_Model.objects.get(id=player_9_id)

                        palyer_10 = None
                        if player_10_id:
                            is_present_10 = Player_Model.objects.filter(id=player_10_id)
                            if is_present_10:
                                palyer_10 = Player_Model.objects.get(id=player_10_id)

                        palyer_11 = None
                        if player_11_id:
                            is_present_11 = Player_Model.objects.filter(id=player_11_id)
                            if is_present_11:
                                palyer_11 = Player_Model.objects.get(id=player_11_id)

                        palyer_12 = None
                        if player_12_id:
                            is_present_12 = Player_Model.objects.filter(id=player_12_id)
                            if is_present_12:
                                palyer_12 = Player_Model.objects.get(id=player_12_id)

                        palyer_13 = None
                        if player_13_id:
                            is_present_13 = Player_Model.objects.filter(id=player_13_id)
                            if is_present_13:
                                palyer_13 = Player_Model.objects.get(id=player_13_id)

                        palyer_14 = None
                        if player_14_id:
                            is_present_14 = Player_Model.objects.filter(id=player_14_id)
                            if is_present_14:
                                palyer_14 = Player_Model.objects.get(id=player_14_id)

                        palyer_15 = None
                        if player_15_id:
                            is_present_15 = Player_Model.objects.filter(id=player_15_id)
                            if is_present_15:
                                palyer_15 = Player_Model.objects.get(id=player_15_id)

                        palyer_16 = None
                        if player_16_id:
                            is_present_16 = Player_Model.objects.filter(id=player_16_id)
                            if is_present_16:
                                palyer_16 = Player_Model.objects.get(id=player_16_id)

                        palyer_17 = None
                        if player_17_id:
                            is_present_17 = Player_Model.objects.filter(id=player_17_id)
                            if is_present_17:
                                palyer_17 = Player_Model.objects.get(id=player_17_id)

                        palyer_18 = None
                        if player_18_id:
                            is_present_18 = Player_Model.objects.filter(id=player_18_id)
                            if is_present_18:
                                palyer_18 = Player_Model.objects.get(id=player_18_id)

                        a_palyer_1 = None
                        if A_player_1_id:
                            a_is_present_1 = Player_Model.objects.filter(id=A_player_1_id)
                            if a_is_present_1:
                                a_palyer_1 = Player_Model.objects.get(id=A_player_1_id)



                        a_palyer_2 = None
                        if A_player_2_id:
                            a_is_present_2 = Player_Model.objects.filter(id=A_player_2_id)
                            if a_is_present_2:
                                a_palyer_2 = Player_Model.objects.get(id=A_player_2_id)



                        a_palyer_3 = None
                        if A_player_3_id:
                            a_is_present_3 = Player_Model.objects.filter(id=A_player_3_id)
                            if a_is_present_3:
                                a_palyer_3 = Player_Model.objects.get(id=A_player_3_id)



                        a_palyer_4 = None
                        if A_player_4_id:
                            a_is_present_4 = Player_Model.objects.filter(id=A_player_4_id)
                            if a_is_present_4:
                                a_palyer_4 = Player_Model.objects.get(id=A_player_4_id)



                        a_palyer_5 = None
                        if A_player_5_id:
                            a_is_present_5 = Player_Model.objects.filter(id=A_player_5_id)
                            if a_is_present_5:
                                a_palyer_5 = Player_Model.objects.get(id=A_player_5_id)



                        a_palyer_6 = None
                        if A_player_6_id:
                            a_is_present_6 = Player_Model.objects.filter(id=A_player_6_id)
                            if a_is_present_6:
                                a_palyer_6 = Player_Model.objects.get(id=A_player_6_id)



                        a_palyer_7 = None
                        if A_player_7_id:
                            a_is_present_7 = Player_Model.objects.filter(id=A_player_7_id)
                            if a_is_present_7:
                                a_palyer_7 = Player_Model.objects.get(id=A_player_7_id)



                        a_palyer_8 = None
                        if A_player_8_id:
                            a_is_present_8 = Player_Model.objects.filter(id=A_player_8_id)
                            if a_is_present_8:
                                a_palyer_8 = Player_Model.objects.get(id=A_player_8_id)



                        a_palyer_9 = None
                        if A_player_9_id:
                            a_is_present_9 = Player_Model.objects.filter(id=A_player_9_id)
                            if a_is_present_9:
                                a_palyer_9 = Player_Model.objects.get(id=A_player_9_id)



                        a_palyer_10 = None
                        if A_player_10_id:
                            a_is_present_10 = Player_Model.objects.filter(id=A_player_10_id)
                            if a_is_present_10:
                                a_palyer_10 = Player_Model.objects.get(id=A_player_10_id)



                        a_palyer_11 = None
                        if A_player_11_id:
                            a_is_present_11 = Player_Model.objects.filter(id=A_player_11_id)
                            if a_is_present_11:
                                a_palyer_11 = Player_Model.objects.get(id=A_player_11_id)


                        s_palyer_1 = None
                        if S_player_1_id:
                            s_is_present_1 = Player_Model.objects.filter(id=S_player_1_id)
                            if s_is_present_1:
                                s_palyer_1 = Player_Model.objects.get(id=S_player_1_id)





                        s_palyer_2 = None
                        if S_player_2_id:
                            s_is_present_2 = Player_Model.objects.filter(id=S_player_2_id)
                            if s_is_present_2:
                                s_palyer_2 = Player_Model.objects.get(id=S_player_2_id)





                        s_palyer_3 = None
                        if S_player_3_id:
                            s_is_present_3 = Player_Model.objects.filter(id=S_player_3_id)
                            if s_is_present_3:
                                s_palyer_3 = Player_Model.objects.get(id=S_player_3_id)





                        s_palyer_4 = None
                        if S_player_4_id:
                            s_is_present_4 = Player_Model.objects.filter(id=S_player_4_id)
                            if s_is_present_4:
                                s_palyer_4 = Player_Model.objects.get(id=S_player_4_id)





                        s_palyer_5 = None
                        if S_player_5_id:
                            s_is_present_5 = Player_Model.objects.filter(id=S_player_5_id)
                            if s_is_present_5:
                                s_palyer_5 = Player_Model.objects.get(id=S_player_5_id)





                        s_palyer_6 = None
                        if S_player_6_id:
                            s_is_present_6 = Player_Model.objects.filter(id=S_player_6_id)
                            if s_is_present_6:
                                s_palyer_6 = Player_Model.objects.get(id=S_player_6_id)





                        s_palyer_7 = None
                        if S_player_7_id:
                            s_is_present_7 = Player_Model.objects.filter(id=S_player_7_id)
                            if s_is_present_7:
                                s_palyer_7 = Player_Model.objects.get(id=S_player_7_id)

                        is_present = Team_Model.objects.filter(id=Team_id)
                        if is_present:
                            is_present = Team_Model.objects.get(id=Team_id)

                            if manager_info_one and manager_info_one != None:
                                is_present.Manager=manager_info_one
                            if palyer_1 and palyer_1 != None:
                                is_present.Team_player_1_id_from_Plyer_model=palyer_1
                            if palyer_2 and palyer_2 != None:
                                is_present.Team_player_2_id_from_Plyer_model=palyer_2
                            if palyer_3 and palyer_3 != None:
                                is_present.Team_player_3_id_from_Plyer_model=palyer_3
                            if palyer_4 and palyer_4 != None:
                                is_present.Team_player_4_id_from_Plyer_model=palyer_4
                            if palyer_5 and palyer_5 != None:
                                is_present.Team_player_5_id_from_Plyer_model=palyer_5
                            if palyer_6 and palyer_6 != None:
                                is_present.Team_player_6_id_from_Plyer_model=palyer_6
                            if palyer_7 and palyer_7 != None:
                                is_present.Team_player_7_id_from_Plyer_model=palyer_7
                            if palyer_8 and palyer_8 != None:
                                is_present.Team_player_8_id_from_Plyer_model=palyer_8
                            if palyer_9 and palyer_9 != None:
                                is_present.Team_player_9_id_from_Plyer_model=palyer_9
                            if palyer_10 and palyer_10 != None:
                                is_present.Team_player_10_id_from_Plyer_model=palyer_10
                            if palyer_11 and palyer_11 != None:
                                is_present.Team_player_11_id_from_Plyer_model=palyer_11
                            if palyer_12 and palyer_12 != None:
                                is_present.Team_player_12_id_from_Plyer_model=palyer_12

                            if palyer_13 and palyer_13 != None:
                                is_present.Team_player_13_id_from_Plyer_model=palyer_13
                            if palyer_14 and palyer_14 != None:
                                is_present.Team_player_14_id_from_Plyer_model=palyer_14
                            if palyer_15 and palyer_15 != None:
                                is_present.Team_player_15_id_from_Plyer_model=palyer_15
                            if palyer_16 and palyer_16 != None:
                                is_present.Team_player_16_id_from_Plyer_model=palyer_16
                            if palyer_17 and palyer_17 != None:
                                is_present.Team_player_17_id_from_Plyer_model=palyer_17
                            if palyer_18 and palyer_18 != None:
                                is_present.Team_player_18_id_from_Plyer_model=palyer_18
                            if a_palyer_1 and a_palyer_1 != None:
                                is_present.Team_player_active_1_id_from_Plyer_model=a_palyer_1
                            if a_palyer_2 and a_palyer_2 != None:
                                is_present.Team_player_active_2_id_from_Plyer_model=a_palyer_2
                            if a_palyer_3 and a_palyer_3 != None:
                                is_present.Team_player_active_3_id_from_Plyer_model=a_palyer_3
                            if a_palyer_4 and a_palyer_4 != None:
                                is_present.Team_player_active_4_id_from_Plyer_model=a_palyer_4
                            if a_palyer_5 and a_palyer_5 != None:
                                is_present.Team_player_active_5_id_from_Plyer_model=a_palyer_5
                            if a_palyer_6 and a_palyer_6 != None:
                                is_present.Team_player_active_6_id_from_Plyer_model=a_palyer_6
                            if a_palyer_7 and a_palyer_7 != None:
                                is_present.Team_player_active_7_id_from_Plyer_model=a_palyer_7
                            if a_palyer_8 and a_palyer_8 != None:
                                is_present.Team_player_active_8_id_from_Plyer_model=a_palyer_8
                            if a_palyer_9 and a_palyer_9 != None:
                                is_present.Team_player_active_9_id_from_Plyer_model=a_palyer_9
                            if a_palyer_10 and a_palyer_10 != None:
                                is_present.Team_player_active_10_id_from_Plyer_model=a_palyer_10
                            if a_palyer_11 and a_palyer_11 != None:
                                is_present.Team_player_active_11_id_from_Plyer_model=a_palyer_11
                            if s_palyer_1 and s_palyer_1 != None:
                                is_present.Team_player_substitute_1_id_from_Plyer_model=s_palyer_1
                            if s_palyer_2 and s_palyer_2 != None:
                                is_present.Team_player_substitute_2_id_from_Plyer_model=s_palyer_2
                            if s_palyer_3 and s_palyer_3 != None:
                                is_present.Team_player_substitute_3_id_from_Plyer_model=s_palyer_3
                            if s_palyer_4 and s_palyer_4 != None:
                                is_present.Team_player_substitute_4_id_from_Plyer_model=s_palyer_4
                            if s_palyer_5 and s_palyer_5 != None:
                                is_present.Team_player_substitute_5_id_from_Plyer_model=s_palyer_5
                            if s_palyer_6 and s_palyer_6 != None:
                                is_present.Team_player_substitute_6_id_from_Plyer_model=s_palyer_6
                            if s_palyer_7 and s_palyer_7 != None:
                                is_present.Team_player_substitute_7_id_from_Plyer_model=s_palyer_7
                            if Team_short_Name:
                                is_present.Team_short_Name=Team_short_Name
                            if Team_Owner_Name:
                                is_present.Team_Owner_Name=Team_Owner_Name
                            if Team_Official_Link:
                                is_present.Team_Official_Link=Team_Official_Link
                            if Team_Logo:
                                is_present.Team_Logo=Team_Logo
                            if Team_banner:
                                is_present.Team_banner=Team_banner
                            if Team_description:
                                is_present.Team_description=Team_description

                            if live_game_video_link:
                                is_present.live_game_link=live_game_video_link
                            is_present.save()



                        mag = {'massage': 'Data is Updated'}
                        json_data = JSONRenderer().render(mag)
                        return HttpResponse(json_data, content_type='application/json')

                    elif Process == 'update' and get_user_info.User_Roll =='Manager' and Team_id:

                        manager_info = User_information.objects.filter(id=get_user_info.id)
                        manager_info_one = None
                        if manager_info:
                            manager_info_one = User_information.objects.get(id=get_user_info.id)



                        palyer_1 = None
                        if player_1_id:
                            is_present_1 = Player_Model.objects.filter(id=player_1_id)
                            if is_present_1:
                                palyer_1 = Player_Model.objects.get(id=player_1_id)

                        palyer_2 = None
                        if player_1_id:
                            is_present_2 = Player_Model.objects.filter(id=player_2_id)
                            if is_present_2:
                                palyer_2 = Player_Model.objects.get(id=player_2_id)

                        palyer_3 = None
                        if player_3_id:
                            is_present_3 = Player_Model.objects.filter(id=player_3_id)
                            if is_present_3:
                                palyer_3 = Player_Model.objects.get(id=player_3_id)

                        palyer_4 = None
                        if player_4_id:
                            is_present_4 = Player_Model.objects.filter(id=player_4_id)
                            if is_present_4:
                                palyer_4 = Player_Model.objects.get(id=player_4_id)

                        palyer_5 = None
                        if player_5_id:
                            is_present_5 = Player_Model.objects.filter(id=player_5_id)
                            if is_present_5:
                                palyer_5 = Player_Model.objects.get(id=player_5_id)

                        palyer_6 = None
                        if player_6_id:
                            is_present_6 = Player_Model.objects.filter(id=player_6_id)
                            if is_present_6:
                                palyer_6 = Player_Model.objects.get(id=player_6_id)

                        palyer_7 = None
                        if player_7_id:
                            is_present_7 = Player_Model.objects.filter(id=player_7_id)
                            if is_present_7:
                                palyer_7 = Player_Model.objects.get(id=player_7_id)

                        palyer_8 = None
                        if player_8_id:
                            is_present_8 = Player_Model.objects.filter(id=player_8_id)
                            if is_present_8:
                                palyer_8 = Player_Model.objects.get(id=player_8_id)

                        palyer_9 = None
                        if player_9_id:
                            is_present_9 = Player_Model.objects.filter(id=player_9_id)
                            if is_present_9:
                                palyer_9 = Player_Model.objects.get(id=player_9_id)

                        palyer_10 = None
                        if player_10_id:
                            is_present_10 = Player_Model.objects.filter(id=player_10_id)
                            if is_present_10:
                                palyer_10 = Player_Model.objects.get(id=player_10_id)

                        palyer_11 = None
                        if player_11_id:
                            is_present_11 = Player_Model.objects.filter(id=player_11_id)
                            if is_present_11:
                                palyer_11 = Player_Model.objects.get(id=player_11_id)

                        palyer_12 = None
                        if player_12_id:
                            is_present_12 = Player_Model.objects.filter(id=player_12_id)
                            if is_present_12:
                                palyer_12 = Player_Model.objects.get(id=player_12_id)

                        palyer_13 = None
                        if player_13_id:
                            is_present_13 = Player_Model.objects.filter(id=player_13_id)
                            if is_present_13:
                                palyer_13 = Player_Model.objects.get(id=player_13_id)

                        palyer_14 = None
                        if player_14_id:
                            is_present_14 = Player_Model.objects.filter(id=player_14_id)
                            if is_present_14:
                                palyer_14 = Player_Model.objects.get(id=player_14_id)

                        palyer_15 = None
                        if player_15_id:
                            is_present_15 = Player_Model.objects.filter(id=player_15_id)
                            if is_present_15:
                                palyer_15 = Player_Model.objects.get(id=player_15_id)

                        palyer_16 = None
                        if player_16_id:
                            is_present_16 = Player_Model.objects.filter(id=player_16_id)
                            if is_present_16:
                                palyer_16 = Player_Model.objects.get(id=player_16_id)

                        palyer_17 = None
                        if player_17_id:
                            is_present_17 = Player_Model.objects.filter(id=player_17_id)
                            if is_present_17:
                                palyer_17 = Player_Model.objects.get(id=player_17_id)

                        palyer_18 = None
                        if player_18_id:
                            is_present_18 = Player_Model.objects.filter(id=player_18_id)
                            if is_present_18:
                                palyer_18 = Player_Model.objects.get(id=player_18_id)

                        a_palyer_1 = None
                        if A_player_1_id:
                            a_is_present_1 = Player_Model.objects.filter(id=A_player_1_id)
                            if a_is_present_1:
                                a_palyer_1 = Player_Model.objects.get(id=A_player_1_id)

                        a_palyer_2 = None
                        if A_player_2_id:
                            a_is_present_2 = Player_Model.objects.filter(id=A_player_2_id)
                            if a_is_present_2:
                                a_palyer_2 = Player_Model.objects.get(id=A_player_2_id)

                        a_palyer_3 = None
                        if A_player_3_id:
                            a_is_present_3 = Player_Model.objects.filter(id=A_player_3_id)
                            if a_is_present_3:
                                a_palyer_3 = Player_Model.objects.get(id=A_player_3_id)

                        a_palyer_4 = None
                        if A_player_4_id:
                            a_is_present_4 = Player_Model.objects.filter(id=A_player_4_id)
                            if a_is_present_4:
                                a_palyer_4 = Player_Model.objects.get(id=A_player_4_id)

                        a_palyer_5 = None
                        if A_player_5_id:
                            a_is_present_5 = Player_Model.objects.filter(id=A_player_5_id)
                            if a_is_present_5:
                                a_palyer_5 = Player_Model.objects.get(id=A_player_5_id)

                        a_palyer_6 = None
                        if A_player_6_id:
                            a_is_present_6 = Player_Model.objects.filter(id=A_player_6_id)
                            if a_is_present_6:
                                a_palyer_6 = Player_Model.objects.get(id=A_player_6_id)

                        a_palyer_7 = None
                        if A_player_7_id:
                            a_is_present_7 = Player_Model.objects.filter(id=A_player_7_id)
                            if a_is_present_7:
                                a_palyer_7 = Player_Model.objects.get(id=A_player_7_id)

                        a_palyer_8 = None
                        if A_player_8_id:
                            a_is_present_8 = Player_Model.objects.filter(id=A_player_8_id)
                            if a_is_present_8:
                                a_palyer_8 = Player_Model.objects.get(id=A_player_8_id)

                        a_palyer_9 = None
                        if A_player_9_id:
                            a_is_present_9 = Player_Model.objects.filter(id=A_player_9_id)
                            if a_is_present_9:
                                a_palyer_9 = Player_Model.objects.get(id=A_player_9_id)

                        a_palyer_10 = None
                        if A_player_10_id:
                            a_is_present_10 = Player_Model.objects.filter(id=A_player_10_id)
                            if a_is_present_10:
                                a_palyer_10 = Player_Model.objects.get(id=A_player_10_id)

                        a_palyer_11 = None
                        if A_player_11_id:
                            a_is_present_11 = Player_Model.objects.filter(id=A_player_11_id)
                            if a_is_present_11:
                                a_palyer_11 = Player_Model.objects.get(id=A_player_11_id)

                        s_palyer_1 = None
                        if S_player_1_id:
                            s_is_present_1 = Player_Model.objects.filter(id=S_player_1_id)
                            if s_is_present_1:
                                s_palyer_1 = Player_Model.objects.get(id=S_player_1_id)

                        s_palyer_2 = None
                        if S_player_2_id:
                            s_is_present_2 = Player_Model.objects.filter(id=S_player_2_id)
                            if s_is_present_2:
                                s_palyer_2 = Player_Model.objects.get(id=S_player_2_id)

                        s_palyer_3 = None
                        if S_player_3_id:
                            s_is_present_3 = Player_Model.objects.filter(id=S_player_3_id)
                            if s_is_present_3:
                                s_palyer_3 = Player_Model.objects.get(id=S_player_3_id)

                        s_palyer_4 = None
                        if S_player_4_id:
                            s_is_present_4 = Player_Model.objects.filter(id=S_player_4_id)
                            if s_is_present_4:
                                s_palyer_4 = Player_Model.objects.get(id=S_player_4_id)

                        s_palyer_5 = None
                        if S_player_5_id:
                            s_is_present_5 = Player_Model.objects.filter(id=S_player_5_id)
                            if s_is_present_5:
                                s_palyer_5 = Player_Model.objects.get(id=S_player_5_id)

                        s_palyer_6 = None
                        if S_player_6_id:
                            s_is_present_6 = Player_Model.objects.filter(id=S_player_6_id)
                            if s_is_present_6:
                                s_palyer_6 = Player_Model.objects.get(id=S_player_6_id)

                        s_palyer_7 = None
                        if S_player_7_id:
                            s_is_present_7 = Player_Model.objects.filter(id=S_player_7_id)
                            if s_is_present_7:
                                s_palyer_7 = Player_Model.objects.get(id=S_player_7_id)

                        is_present = Team_Model.objects.filter(id=Team_id)
                        if is_present:
                            is_present = Team_Model.objects.get(id=Team_id)

                            if manager_info_one and manager_info_one != None:
                                is_present.Manager = manager_info_one
                            if palyer_1 and palyer_1 != None:
                                is_present.Team_player_1_id_from_Plyer_model = palyer_1
                            if palyer_2 and palyer_2 != None:
                                is_present.Team_player_2_id_from_Plyer_model = palyer_2
                            if palyer_3 and palyer_3 != None:
                                is_present.Team_player_3_id_from_Plyer_model = palyer_3
                            if palyer_4 and palyer_4 != None:
                                is_present.Team_player_4_id_from_Plyer_model = palyer_4
                            if palyer_5 and palyer_5 != None:
                                is_present.Team_player_5_id_from_Plyer_model = palyer_5
                            if palyer_6 and palyer_6 != None:
                                is_present.Team_player_6_id_from_Plyer_model = palyer_6
                            if palyer_7 and palyer_7 != None:
                                is_present.Team_player_7_id_from_Plyer_model = palyer_7
                            if palyer_8 and palyer_8 != None:
                                is_present.Team_player_8_id_from_Plyer_model = palyer_8
                            if palyer_9 and palyer_9 != None:
                                is_present.Team_player_9_id_from_Plyer_model = palyer_9
                            if palyer_10 and palyer_10 != None:
                                is_present.Team_player_10_id_from_Plyer_model = palyer_10
                            if palyer_11 and palyer_11 != None:
                                is_present.Team_player_11_id_from_Plyer_model = palyer_11
                            if palyer_12 and palyer_12 != None:
                                is_present.Team_player_12_id_from_Plyer_model = palyer_12

                            if palyer_13 and palyer_13 != None:
                                is_present.Team_player_13_id_from_Plyer_model = palyer_13
                            if palyer_14 and palyer_14 != None:
                                is_present.Team_player_14_id_from_Plyer_model = palyer_14
                            if palyer_15 and palyer_15 != None:
                                is_present.Team_player_15_id_from_Plyer_model = palyer_15
                            if palyer_16 and palyer_16 != None:
                                is_present.Team_player_16_id_from_Plyer_model = palyer_16
                            if palyer_17 and palyer_17 != None:
                                is_present.Team_player_17_id_from_Plyer_model = palyer_17
                            if palyer_18 and palyer_18 != None:
                                is_present.Team_player_18_id_from_Plyer_model = palyer_18
                            if a_palyer_1 and a_palyer_1 != None:
                                is_present.Team_player_active_1_id_from_Plyer_model = a_palyer_1
                            if a_palyer_2 and a_palyer_2 != None:
                                is_present.Team_player_active_2_id_from_Plyer_model = a_palyer_2
                            if a_palyer_3 and a_palyer_3 != None:
                                is_present.Team_player_active_3_id_from_Plyer_model = a_palyer_3
                            if a_palyer_4 and a_palyer_4 != None:
                                is_present.Team_player_active_4_id_from_Plyer_model = a_palyer_4
                            if a_palyer_5 and a_palyer_5 != None:
                                is_present.Team_player_active_5_id_from_Plyer_model = a_palyer_5
                            if a_palyer_6 and a_palyer_6 != None:
                                is_present.Team_player_active_6_id_from_Plyer_model = a_palyer_6
                            if a_palyer_7 and a_palyer_7 != None:
                                is_present.Team_player_active_7_id_from_Plyer_model = a_palyer_7
                            if a_palyer_8 and a_palyer_8 != None:
                                is_present.Team_player_active_8_id_from_Plyer_model = a_palyer_8
                            if a_palyer_9 and a_palyer_9 != None:
                                is_present.Team_player_active_9_id_from_Plyer_model = a_palyer_9
                            if a_palyer_10 and a_palyer_10 != None:
                                is_present.Team_player_active_10_id_from_Plyer_model = a_palyer_10
                            if a_palyer_11 and a_palyer_11 != None:
                                is_present.Team_player_active_11_id_from_Plyer_model = a_palyer_11
                            if s_palyer_1 and s_palyer_1 != None:
                                is_present.Team_player_substitute_1_id_from_Plyer_model = s_palyer_1
                            if s_palyer_2 and s_palyer_2 != None:
                                is_present.Team_player_substitute_2_id_from_Plyer_model = s_palyer_2
                            if s_palyer_3 and s_palyer_3 != None:
                                is_present.Team_player_substitute_3_id_from_Plyer_model = s_palyer_3
                            if s_palyer_4 and s_palyer_4 != None:
                                is_present.Team_player_substitute_4_id_from_Plyer_model = s_palyer_4
                            if s_palyer_5 and s_palyer_5 != None:
                                is_present.Team_player_substitute_5_id_from_Plyer_model = s_palyer_5
                            if s_palyer_6 and s_palyer_6 != None:
                                is_present.Team_player_substitute_6_id_from_Plyer_model = s_palyer_6
                            if s_palyer_7 and s_palyer_7 != None:
                                is_present.Team_player_substitute_7_id_from_Plyer_model = s_palyer_7
                            if Team_short_Name:
                                is_present.Team_short_Name = Team_short_Name
                            if Team_Owner_Name:
                                is_present.Team_Owner_Name = Team_Owner_Name
                            if Team_Official_Link:
                                is_present.Team_Official_Link = Team_Official_Link
                            if Team_Logo:
                                is_present.Team_Logo = Team_Logo
                            if Team_banner:
                                is_present.Team_banner = Team_banner
                            if Team_description:
                                is_present.Team_description = Team_description
                            is_present.save()







                        mag = {'massage': 'Data is Updated'}
                        json_data = JSONRenderer().render(mag)
                        return HttpResponse(json_data, content_type='application/json')

                    else:
                        HttpResponse('NOT VALID')

            else:
                HttpResponse('NOT VALID')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')
