from django.shortcuts import render, HttpResponse
from .models import Game_Model
from . serializers import Game_Model_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from Event.models import Event_Model
from Player.models import Player_Model

from Team.models import Team_Model
from django.http import JsonResponse

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q


from Goal.serializers import Goal_Model_serializer
from Substituitons.serializers import Substituitons_Model_serializer
from Goal.models import Goal_Model
from Substituitons.models import Substituitons_Model


@csrf_exempt
def find_all_Game(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        if Process == 'see_all_Game':
            get_spacific_info = Game_Model.objects.all()
            serializer_var = Game_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')


        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def find_game_with_id(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        specific_id = request.POST.get('specific_id')

        if Process == 'find_Game_with_id' and specific_id:
            get_spacifi = Game_Model.objects.filter(id = specific_id)
            if get_spacifi:
                get_spacific_info = Game_Model.objects.get(id = specific_id)
                serializer_var = Game_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')

            else:
                HttpResponse('NOT VALID')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def find_game_with_Event_id(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        Event_id = request.POST.get('Event_id')

        if Process == 'find_game_with_Event_id' and Event_id:
            event_find = Event_Model.objects.filter(id=Event_id)
            event_find_info=''
            if event_find:
                event_find_info = Event_Model.objects.get(id=Event_id)
            if event_find_info:
                get_spacifi = Game_Model.objects.filter(Event_for_game=event_find_info)

                game_json_data_to_dict={}
                if get_spacifi:
                    get_spacific_info = Game_Model.objects.get(Event_for_game=event_find_info)
                    serializer_var = Game_Model_serializer(get_spacific_info, many=False)
                    game_json_data = JSONRenderer().render(serializer_var.data)
                    # return HttpResponse(json_data, content_type='application/json')
                    import json
                    game_json_data_to_dict = json.loads(game_json_data)
                    # print(type(json.loads(game_json_data)))
                    # print(game_json_data_to_dict)

                Goal_json_data_to_dict={}
                Goal_get_spacifi = Goal_Model.objects.filter(Event_for_goal=event_find_info)
                if Goal_get_spacifi:
                    Goal_get_spacific_info = Goal_Model.objects.filter(Event_for_goal=event_find_info)
                    h=776
                    yty=878
                    serializer_var = Goal_Model_serializer(Goal_get_spacific_info, many=True)
                    Goal_json_data = JSONRenderer().render(serializer_var.data)
                    import json
                    Goal_json_data_to_dict = json.loads(Goal_json_data)
                    print(type(json.loads(Goal_json_data)))
                    print(Goal_json_data_to_dict)
                # game_json_data_to_dict.update(Goal_json_data_to_dict)

                Substituitons_json_data_to_dict={}
                Substituitons_get_spacifi = Substituitons_Model.objects.filter(Event_for_goal=event_find_info)
                if Substituitons_get_spacifi:
                    get_spacific_info = Substituitons_Model.objects.filter(
                        Event_for_goal=event_find_info)
                    Substituitons_serializer_var = Substituitons_Model_serializer(get_spacific_info, many=True)
                    Substituitons_json_data = JSONRenderer().render(Substituitons_serializer_var.data)

                    import json
                    Substituitons_json_data_to_dict = json.loads(Substituitons_json_data)
                    print(type(json.loads(Substituitons_json_data)))
                    print(Substituitons_json_data_to_dict)
                # there = two_here.update(Goal_json_data_to_dict)
                #
                # print(there)

                mag = {
                    'game_json_data_to_dict': game_json_data_to_dict,
                    'Goal_json_data_to_dict':Goal_json_data_to_dict,
                    'Substituitons_json_data_to_dict':Substituitons_json_data_to_dict
                       }
                # json_data = JSONRenderer().render(mag)
                # return HttpResponse(json_data, content_type='application/json')

                json = {
                    "key": "value",
                    "key_two": "value_two"
                }
                json_data = JSONRenderer().render(mag)
                return HttpResponse(json_data, content_type='application/json')




            else:
                HttpResponse('NOT VALID')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')



@csrf_exempt
def create_specific_game(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        event_id = request.POST.get('event_id')


        # for goal
        home_team_goal_count_total = request.POST.get('home_team_goal_count_total')
        way_team_goal_count_total = request.POST.get('way_team_goal_count_total')
        scorer_name = request.POST.get('scorer_name')
        assist_name = request.POST.get('assist_name')

        scorer_id = request.POST.get('scorer_id')
        assist_id = request.POST.get('assist_id')

        # for subsitute
        substitute_team_Home_or_way = request.POST.get('substitute_team_Home_or_way')
        player = request.POST.get('player')
        substitute_player = request.POST.get('substitute_player')


        home_team_shot_on_target = request.POST.get('home_team_shot_on_target')
        way_team_shot_on_target = request.POST.get('way_team_shot_on_target')

        home_team_position = request.POST.get('home_team_position')
        way_team_position = request.POST.get('way_team_position')

        home_team_corner = request.POST.get('home_team_corner')
        way_team_corner = request.POST.get('way_team_corner')

        is_it_finished = request.POST.get('is_it_finished')



        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):
                    d = get_user_info.User_Roll


                    if Process == 'create' and get_user_info.User_Roll =='Admin':
                        if is_it_finished:
                            is_enevt = Event_Model.objects.filter(id=event_id)
                            if is_enevt:
                                one_enevt = Event_Model.objects.get(id=event_id)
                                is_game_present = Game_Model.objects.filter(Event_for_game=one_enevt)


                                # if present  and -----------------finished -------------------------------------------
                                if is_game_present:
                                    the_game_present = Game_Model.objects.get(Event_for_game=one_enevt)



                                    # find win twm name--------------------------------------------------
                                    previous_Home_Team_Score = the_game_present.Home_Team_Score
                                    previous_Way_Team_Score = the_game_present.Way_Team_Score

                                    if home_team_goal_count_total:
                                        previous_Home_Team_Score = int(previous_Home_Team_Score) + int(
                                            home_team_goal_count_total)
                                    else:
                                        pass

                                    if way_team_goal_count_total:
                                        previous_Way_Team_Score = int(previous_Way_Team_Score) + int(
                                            way_team_goal_count_total)
                                    else:
                                        pass



                                    win_option = ''
                                    if previous_Way_Team_Score > previous_Home_Team_Score:
                                        the_game_present.Win_or_Lose_team_auto = the_game_present.way_Team_name
                                        win_option = the_game_present.way_Team_name

                                    elif previous_Home_Team_Score > previous_Way_Team_Score:
                                        the_game_present.Win_or_Lose_team_auto = the_game_present.home_Team_name
                                        win_option = the_game_present.home_Team_name

                                    elif previous_Home_Team_Score == previous_Way_Team_Score:
                                        the_game_present.Win_or_Lose_team_auto = 'DROW'
                                        win_option = 'DROW'
                                    else:
                                        pass
                                    # ----------------------------------------------------------------


                                    if previous_Home_Team_Score:
                                        the_game_present.Home_Team_Score = previous_Home_Team_Score
                                    if previous_Way_Team_Score:
                                        the_game_present.Way_Team_Score = previous_Way_Team_Score
                                    if home_team_shot_on_target:
                                        the_game_present.Home_Team_Shot_on_target = home_team_shot_on_target
                                    if way_team_shot_on_target:
                                        the_game_present.Way_Team_Shot_on_target = way_team_shot_on_target
                                    if home_team_position:
                                        the_game_present.Home_Team_Position = home_team_position
                                    if way_team_position:
                                        the_game_present.Way_Team_Position = way_team_position
                                    if home_team_corner:
                                        the_game_present.Home_Team_Corner = home_team_corner
                                    if way_team_corner:
                                        the_game_present.Way_Team_Corner = way_team_corner
                                    the_game_present.is_game_finished = "yes"

                                    one_enevt.is_game_finished = "yes"
                                    one_enevt.save()

                                    the_game_present.save()

                                    if scorer_name and assist_name:
                                        if home_team_goal_count_total:
                                            goal_create = Goal_Model(Event_for_goal=one_enevt,
                                                                     Home_Team_Goal_Count_In_1='1',
                                                                     Scorer_Name=scorer_name,
                                                                     Goal_Assist_Name=assist_name)
                                            goal_create.save()
                                        if way_team_goal_count_total:
                                            goal_create = Goal_Model(Event_for_goal=one_enevt,
                                                                     way_team_goal_count_total='1',
                                                                     Scorer_Name=scorer_name,
                                                                     Goal_Assist_Name=assist_name)
                                            goal_create.save()



                                        if scorer_id:
                                            d = Player_Model.objects.filter(id=scorer_id)
                                            if d:
                                                d2 = Player_Model.objects.get(id=scorer_id)
                                                previous_goal = d2.Total_goal_count
                                                d2.Total_goal_count = previous_goal + 1
                                                d2.save()

                                        if assist_id:
                                            dw = Player_Model.objects.filter(id=assist_id)
                                            if dw:
                                                dw2 = Player_Model.objects.get(id=assist_id)
                                                previous_assist = dw2.Total_assist_count
                                                dw2.Total_assist_count = previous_assist + 1
                                                dw2.save()


                                    if player and substitute_player and substitute_team_Home_or_way:
                                        Substituiton_create = Substituitons_Model(Event_for_goal=one_enevt,
                                                                                  PLayer_Name=player,
                                                                                  Substituitons_Name=substitute_player,
                                                                                  substitute_team_Home_or_way=substitute_team_Home_or_way)
                                        Substituiton_create.save()



                                    # change on team
                                    if win_option:
                                        Home_Team = Team_Model.objects.filter(Team_Name=one_enevt.Home_Team)

                                        if Home_Team:
                                            Home_Team = Team_Model.objects.get(Team_Name=one_enevt.Home_Team)

                                            # previous all record
                                            previous_Win_count = Home_Team.Win_count
                                            previous_Loos_count = Home_Team.Loos_count
                                            previous_Drow_count = Home_Team.Drow_count
                                            previous_GF = Home_Team.GF
                                            previous_GA = Home_Team.GA
                                            previous_GD = Home_Team.GD
                                            previous_PTS = Home_Team.PTS

                                            if win_option == one_enevt.Home_Team:
                                                Home_Team.Win_count = int(previous_Win_count)+1
                                                Home_Team.GF = int(previous_GF)+int(previous_Home_Team_Score)
                                                Home_Team.GA = int(previous_GA)+int(previous_Way_Team_Score)
                                                total_GA = int(previous_GF)+int(previous_Home_Team_Score)
                                                total_GF = int(previous_GA)+int(previous_Way_Team_Score)
                                                Home_Team.GD = total_GA - total_GF
                                                win_count = int(previous_Win_count)+1
                                                Home_Team.PTS = win_count*3

                                                Home_Team.save()

                                        way_Team = Team_Model.objects.filter(Team_Name=one_enevt.Way_Team)
                                        if way_Team:
                                            way_Team = Team_Model.objects.get(Team_Name=one_enevt.Way_Team)

                                            # previous all record
                                            previous_Win_count = way_Team.Win_count
                                            previous_Loos_count = way_Team.Loos_count
                                            previous_Drow_count = way_Team.Drow_count
                                            previous_GF = way_Team.GF
                                            previous_GA = way_Team.GA
                                            previous_GD = way_Team.GD
                                            previous_PTS = way_Team.PTS

                                            if win_option == one_enevt.Way_Team:
                                                way_Team.Win_count = int(previous_Win_count) + 1
                                                way_Team.GF = int(previous_GF) + int(previous_Way_Team_Score)
                                                way_Team.GA = int(previous_GA) + int(previous_Home_Team_Score)
                                                total_GA = int(previous_GF) + int(previous_Way_Team_Score)
                                                total_GF = int(previous_GA) + int(previous_Home_Team_Score)
                                                way_Team.GD = total_GA - total_GF
                                                win_count = int(previous_Win_count) + 1
                                                way_Team.PTS = win_count * 3

                                                way_Team.save()






                                    mag = {'massage': 'Data is Created'}
                                    json_data = JSONRenderer().render(mag)
                                    return HttpResponse(json_data, content_type='application/json')







                        else:
                            is_enevt = Event_Model.objects.filter(id=event_id)
                            if is_enevt:
                                one_enevt = Event_Model.objects.get(id=event_id)
                                is_game_present = Game_Model.objects.filter(Event_for_game=one_enevt)

                                # if present but not finished -------------------------------------------
                                if is_game_present:
                                    the_game_present = Game_Model.objects.get(Event_for_game=one_enevt)

                                    previous_Home_Team_Score = the_game_present.Home_Team_Score
                                    previous_Way_Team_Score = the_game_present.Way_Team_Score

                                    if home_team_goal_count_total  and home_team_goal_count_total !=0:
                                        previous_Home_Team_Score = int(previous_Home_Team_Score)+int(home_team_goal_count_total)

                                    if way_team_goal_count_total:
                                        previous_Way_Team_Score = int(previous_Way_Team_Score) + int(
                                            way_team_goal_count_total)

                                    if previous_Home_Team_Score:
                                        the_game_present.Home_Team_Score = previous_Home_Team_Score
                                    if previous_Way_Team_Score:
                                        the_game_present.Way_Team_Score = previous_Way_Team_Score
                                    if home_team_shot_on_target:
                                        the_game_present.Home_Team_Shot_on_target = home_team_shot_on_target
                                    if way_team_shot_on_target:
                                        the_game_present.Way_Team_Shot_on_target = way_team_shot_on_target
                                    if home_team_position:
                                        the_game_present.Home_Team_Position = home_team_position
                                    if way_team_position:
                                        the_game_present.Way_Team_Position = way_team_position
                                    if home_team_corner:
                                        the_game_present.Home_Team_Corner = home_team_corner
                                    if way_team_corner:
                                        the_game_present.Way_Team_Corner = way_team_corner
                                    the_game_present.save()

                                    if scorer_name and assist_name:
                                        if home_team_goal_count_total  and home_team_goal_count_total !=0:
                                            goal_create = Goal_Model(Event_for_goal=one_enevt,
                                                                     Home_Team_Goal_Count_In_1='1',
                                                                     Scorer_Name=scorer_name,
                                                                     Goal_Assist_Name=assist_name)
                                            goal_create.save()
                                        if way_team_goal_count_total  and way_team_goal_count_total != 0:
                                            goal_create = Goal_Model(Event_for_goal=one_enevt,
                                                                     way_team_goal_count_total='1',
                                                                     Scorer_Name=scorer_name,
                                                                     Goal_Assist_Name=assist_name)
                                            goal_create.save()

                                        if scorer_id:
                                            d = Player_Model.objects.filter(id=scorer_id)
                                            if d:
                                                d2 = Player_Model.objects.get(id=scorer_id)
                                                previous_goal = d2.Total_goal_count
                                                d2.Total_goal_count = previous_goal + 1
                                                d2.save()

                                        if assist_id:
                                            dw = Player_Model.objects.filter(id=assist_id)
                                            if dw:
                                                dw2 = Player_Model.objects.get(id=assist_id)
                                                previous_assist = dw2.Total_assist_count
                                                dw2.Total_assist_count = previous_assist + 1
                                                dw2.save()

                                    if player and substitute_player and substitute_team_Home_or_way:
                                        Substituiton_create = Substituitons_Model(Event_for_goal=one_enevt,
                                                                                  PLayer_Name=player,
                                                                                  Substituitons_Name=substitute_player,
                                                                                  substitute_team_Home_or_way=substitute_team_Home_or_way)
                                        Substituiton_create.save()

                                    mag = {'massage': 'Data is Created'}
                                    json_data = JSONRenderer().render(mag)
                                    return HttpResponse(json_data, content_type='application/json')






                                # fully new game-------------------------------------------------------------
                                else:
                                    home_team = one_enevt.Home_Team
                                    way_team = one_enevt.Way_Team

                                    is_home_team = Team_Model.objects.filter(Team_Name = home_team)
                                    is_way_team = Team_Model.objects.filter(Team_Name = way_team)

                                    if is_home_team and is_way_team:
                                        one_home_team = Team_Model.objects.get(Team_Name=home_team)
                                        one_way_team = Team_Model.objects.get(Team_Name=way_team)

                                        if home_team_goal_count_total == '':
                                            home_team_goal_count_total = 0

                                        if way_team_goal_count_total == '':
                                            way_team_goal_count_total = 0

                                        create_new_game = Game_Model(Event_for_game=one_enevt, Home_Team_Score=home_team_goal_count_total, Way_Team_Score=way_team_goal_count_total, Home_Team_Shot_on_target=home_team_shot_on_target, Way_Team_Shot_on_target=way_team_shot_on_target, Home_Team_Position=home_team_position, Way_Team_Position=way_team_position, Home_Team_Corner=home_team_corner, Way_Team_Corner=way_team_corner, home_Team_name=one_home_team.Team_Name, home_Team_manager_name=one_home_team.Manager.User_Name, home_Team_player_1_id_from_Plyer_model=one_home_team.Team_player_1_id_from_Plyer_model.id, home_Team_player_2_id_from_Plyer_model=one_home_team.Team_player_2_id_from_Plyer_model.id, home_Team_player_3_id_from_Plyer_model=one_home_team.Team_player_3_id_from_Plyer_model.id, home_Team_player_4_id_from_Plyer_model=one_home_team.Team_player_4_id_from_Plyer_model.id, home_Team_player_5_id_from_Plyer_model=one_home_team.Team_player_5_id_from_Plyer_model.id, home_Team_player_6_id_from_Plyer_model=one_home_team.Team_player_6_id_from_Plyer_model.id, home_Team_player_7_id_from_Plyer_model=one_home_team.Team_player_7_id_from_Plyer_model.id, home_Team_player_8_id_from_Plyer_model=one_home_team.Team_player_8_id_from_Plyer_model.id, home_Team_player_9_id_from_Plyer_model=one_home_team.Team_player_9_id_from_Plyer_model.id, home_Team_player_10_id_from_Plyer_model=one_home_team.Team_player_10_id_from_Plyer_model.id, home_Team_player_11_id_from_Plyer_model=one_home_team.Team_player_11_id_from_Plyer_model.id, home_Team_player_12_id_from_Plyer_model=one_home_team.Team_player_12_id_from_Plyer_model.id,home_Team_player_13_id_from_Plyer_model=one_home_team.Team_player_13_id_from_Plyer_model.id, home_Team_player_14_id_from_Plyer_model=one_home_team.Team_player_14_id_from_Plyer_model.id, home_Team_player_15_id_from_Plyer_model=one_home_team.Team_player_15_id_from_Plyer_model.id, home_Team_player_16_id_from_Plyer_model=one_home_team.Team_player_16_id_from_Plyer_model.id, home_Team_player_17_id_from_Plyer_model=one_home_team.Team_player_17_id_from_Plyer_model.id, home_Team_player_18_id_from_Plyer_model=one_home_team.Team_player_18_id_from_Plyer_model.id, home_Team_player_active_1_id_from_Plyer_model=one_home_team.Team_player_active_1_id_from_Plyer_model.id, home_Team_player_active_2_id_from_Plyer_model=one_home_team.Team_player_active_2_id_from_Plyer_model.id, home_Team_player_active_3_id_from_Plyer_model=one_home_team.Team_player_active_3_id_from_Plyer_model.id, home_Team_player_active_4_id_from_Plyer_model=one_home_team.Team_player_active_4_id_from_Plyer_model.id, home_Team_player_active_5_id_from_Plyer_model=one_home_team.Team_player_active_5_id_from_Plyer_model.id, home_Team_player_active_6_id_from_Plyer_model=one_home_team.Team_player_active_6_id_from_Plyer_model.id, home_Team_player_active_7_id_from_Plyer_model=one_home_team.Team_player_active_7_id_from_Plyer_model.id, home_Team_player_active_8_id_from_Plyer_model=one_home_team.Team_player_active_8_id_from_Plyer_model.id, home_Team_player_active_9_id_from_Plyer_model=one_home_team.Team_player_active_9_id_from_Plyer_model.id, home_Team_player_active_10_id_from_Plyer_model=one_home_team.Team_player_active_10_id_from_Plyer_model.id, home_Team_player_active_11_id_from_Plyer_model=one_home_team.Team_player_active_11_id_from_Plyer_model.id, home_Team_player_substitute_1_id_from_Plyer_model=one_home_team.Team_player_substitute_1_id_from_Plyer_model.id, home_Team_player_substitute_2_id_from_Plyer_model=one_home_team.Team_player_substitute_2_id_from_Plyer_model.id, home_Team_player_substitute_3_id_from_Plyer_model=one_home_team.Team_player_substitute_3_id_from_Plyer_model.id, home_Team_player_substitute_4_id_from_Plyer_model=one_home_team.Team_player_substitute_4_id_from_Plyer_model.id,home_Team_player_substitute_5_id_from_Plyer_model=one_home_team.Team_player_substitute_5_id_from_Plyer_model.id,home_Team_player_substitute_6_id_from_Plyer_model=one_home_team.Team_player_substitute_6_id_from_Plyer_model.id,home_Team_player_substitute_7_id_from_Plyer_model=one_home_team.Team_player_substitute_7_id_from_Plyer_model.id, way_Team_name =one_way_team.Team_Name, way_Team_manager_name=one_way_team.Manager.User_Name, way_Team_player_1_id_from_Plyer_model=one_way_team.Team_player_1_id_from_Plyer_model.id, way_Team_player_2_id_from_Plyer_model=one_way_team.Team_player_2_id_from_Plyer_model.id, way_Team_player_3_id_from_Plyer_model=one_way_team.Team_player_3_id_from_Plyer_model.id, way_Team_player_4_id_from_Plyer_model=one_way_team.Team_player_4_id_from_Plyer_model.id, way_Team_player_5_id_from_Plyer_model=one_way_team.Team_player_5_id_from_Plyer_model.id, way_Team_player_6_id_from_Plyer_model=one_way_team.Team_player_6_id_from_Plyer_model.id, way_Team_player_7_id_from_Plyer_model=one_way_team.Team_player_7_id_from_Plyer_model.id, way_Team_player_8_id_from_Plyer_model=one_way_team.Team_player_8_id_from_Plyer_model.id, way_Team_player_9_id_from_Plyer_model=one_way_team.Team_player_9_id_from_Plyer_model.id, way_Team_player_10_id_from_Plyer_model=one_way_team.Team_player_10_id_from_Plyer_model.id, way_Team_player_11_id_from_Plyer_model=one_way_team.Team_player_11_id_from_Plyer_model.id, way_Team_player_12_id_from_Plyer_model=one_way_team.Team_player_12_id_from_Plyer_model.id,way_Team_player_13_id_from_Plyer_model=one_way_team.Team_player_13_id_from_Plyer_model.id, way_Team_player_14_id_from_Plyer_model=one_way_team.Team_player_14_id_from_Plyer_model.id, way_Team_player_15_id_from_Plyer_model=one_way_team.Team_player_15_id_from_Plyer_model.id,way_Team_player_16_id_from_Plyer_model=one_way_team.Team_player_16_id_from_Plyer_model.id,way_Team_player_17_id_from_Plyer_model=one_way_team.Team_player_17_id_from_Plyer_model.id,way_Team_player_18_id_from_Plyer_model=one_way_team.Team_player_18_id_from_Plyer_model.id, way_Team_player_active_1_id_from_Plyer_model=one_way_team.Team_player_active_1_id_from_Plyer_model.id, way_Team_player_active_2_id_from_Plyer_model=one_way_team.Team_player_active_2_id_from_Plyer_model.id, way_Team_player_active_3_id_from_Plyer_model=one_way_team.Team_player_active_3_id_from_Plyer_model.id, way_Team_player_active_4_id_from_Plyer_model=one_way_team.Team_player_active_4_id_from_Plyer_model.id, way_Team_player_active_5_id_from_Plyer_model=one_way_team.Team_player_active_5_id_from_Plyer_model.id, way_Team_player_active_6_id_from_Plyer_model=one_way_team.Team_player_active_6_id_from_Plyer_model.id, way_Team_player_active_7_id_from_Plyer_model=one_way_team.Team_player_active_7_id_from_Plyer_model.id, way_Team_player_active_8_id_from_Plyer_model=one_way_team.Team_player_active_8_id_from_Plyer_model.id, way_Team_player_active_9_id_from_Plyer_model=one_way_team.Team_player_active_9_id_from_Plyer_model.id, way_Team_player_active_10_id_from_Plyer_model=one_way_team.Team_player_active_10_id_from_Plyer_model.id, way_Team_player_active_11_id_from_Plyer_model=one_way_team.Team_player_active_11_id_from_Plyer_model.id, way_Team_player_substitute_1_id_from_Plyer_model=one_way_team.Team_player_substitute_1_id_from_Plyer_model.id, way_Team_player_substitute_2_id_from_Plyer_model=one_way_team.Team_player_substitute_2_id_from_Plyer_model.id, way_Team_player_substitute_3_id_from_Plyer_model=one_way_team.Team_player_substitute_3_id_from_Plyer_model.id, way_Team_player_substitute_4_id_from_Plyer_model=one_way_team.Team_player_substitute_4_id_from_Plyer_model.id,way_Team_player_substitute_5_id_from_Plyer_model=one_way_team.Team_player_substitute_5_id_from_Plyer_model.id,way_Team_player_substitute_6_id_from_Plyer_model=one_way_team.Team_player_substitute_6_id_from_Plyer_model.id,way_Team_player_substitute_7_id_from_Plyer_model=one_way_team.Team_player_substitute_7_id_from_Plyer_model.id, is_game_finished="running")
                                        create_new_game.save()

                                        one_enevt.is_game_finished = "running"
                                        one_enevt.save()



                                        if scorer_name and assist_name:
                                            if home_team_goal_count_total and home_team_goal_count_total !=0:
                                                goal_create = Goal_Model(Event_for_goal=one_enevt, Home_Team_Goal_Count_In_1 = '1', Scorer_Name=scorer_name, Goal_Assist_Name=assist_name)
                                                goal_create.save()
                                            if way_team_goal_count_total and way_team_goal_count_total != 0:
                                                goal_create = Goal_Model(Event_for_goal=one_enevt, way_team_goal_count_total='1', Scorer_Name=scorer_name, Goal_Assist_Name=assist_name)
                                                goal_create.save()

                                            if scorer_id:
                                                d = Player_Model.objects.filter(id=scorer_id)
                                                if d:
                                                    d2 = Player_Model.objects.get(id=scorer_id)
                                                    previous_goal = d2.Total_goal_count
                                                    d2.Total_goal_count = previous_goal + 1
                                                    d2.save()

                                            if assist_id:
                                                dw = Player_Model.objects.filter(id=assist_id)
                                                if dw:
                                                    dw2 = Player_Model.objects.get(id=assist_id)
                                                    previous_assist = dw2.Total_assist_count
                                                    dw2.Total_assist_count = previous_assist + 1
                                                    dw2.save()


                                        if player and substitute_player and substitute_team_Home_or_way:
                                            Substituiton_create = Substituitons_Model(Event_for_goal=one_enevt, PLayer_Name=player, Substituitons_Name=substitute_player, substitute_team_Home_or_way=substitute_team_Home_or_way)
                                            Substituiton_create.save()

                                        mag = {'massage': 'Data is Created'}
                                        json_data = JSONRenderer().render(mag)
                                        return HttpResponse(json_data, content_type='application/json')





                            else:
                                HttpResponse('NOT VALID')









                    elif Process == 'create' and get_user_info.User_Roll =='Operations':

                        if is_it_finished:
                            is_enevt = Event_Model.objects.filter(id=event_id)
                            if is_enevt:
                                one_enevt = Event_Model.objects.get(id=event_id)
                                is_game_present = Game_Model.objects.filter(Event_for_game=one_enevt)

                                # if present  and -----------------finished -------------------------------------------
                                if is_game_present:
                                    the_game_present = Game_Model.objects.get(Event_for_game=one_enevt)



                                    # find win twm name--------------------------------------------------
                                    previous_Home_Team_Score = the_game_present.Home_Team_Score
                                    previous_Way_Team_Score = the_game_present.Way_Team_Score

                                    if home_team_goal_count_total:
                                        previous_Home_Team_Score = int(previous_Home_Team_Score) + int(
                                            home_team_goal_count_total)
                                    else:
                                        pass

                                    if way_team_goal_count_total:
                                        previous_Way_Team_Score = int(previous_Way_Team_Score) + int(
                                            way_team_goal_count_total)
                                    else:
                                        pass



                                    win_option = ''
                                    if previous_Way_Team_Score > previous_Home_Team_Score:
                                        the_game_present.Win_or_Lose_team_auto = the_game_present.way_Team_name
                                        win_option = the_game_present.way_Team_name

                                    elif previous_Home_Team_Score > previous_Way_Team_Score:
                                        the_game_present.Win_or_Lose_team_auto = the_game_present.home_Team_name
                                        win_option = the_game_present.home_Team_name

                                    elif previous_Home_Team_Score == previous_Way_Team_Score:
                                        the_game_present.Win_or_Lose_team_auto = 'DROW'
                                        win_option = 'DROW'
                                    else:
                                        pass
                                    # ----------------------------------------------------------------


                                    if previous_Home_Team_Score:
                                        the_game_present.Home_Team_Score = previous_Home_Team_Score
                                    if previous_Way_Team_Score:
                                        the_game_present.Way_Team_Score = previous_Way_Team_Score
                                    if home_team_shot_on_target:
                                        the_game_present.Home_Team_Shot_on_target = home_team_shot_on_target
                                    if way_team_shot_on_target:
                                        the_game_present.Way_Team_Shot_on_target = way_team_shot_on_target
                                    if home_team_position:
                                        the_game_present.Home_Team_Position = home_team_position
                                    if way_team_position:
                                        the_game_present.Way_Team_Position = way_team_position
                                    if home_team_corner:
                                        the_game_present.Home_Team_Corner = home_team_corner
                                    if way_team_corner:
                                        the_game_present.Way_Team_Corner = way_team_corner
                                    the_game_present.is_game_finished = "yes"


                                    one_enevt.is_game_finished = "yes"
                                    one_enevt.save()

                                    the_game_present.save()

                                    if scorer_name and assist_name:
                                        if home_team_goal_count_total:
                                            goal_create = Goal_Model(Event_for_goal=one_enevt,
                                                                     Home_Team_Goal_Count_In_1='1',
                                                                     Scorer_Name=scorer_name,
                                                                     Goal_Assist_Name=assist_name)
                                            goal_create.save()
                                        if way_team_goal_count_total:
                                            goal_create = Goal_Model(Event_for_goal=one_enevt,
                                                                     way_team_goal_count_total='1',
                                                                     Scorer_Name=scorer_name,
                                                                     Goal_Assist_Name=assist_name)
                                            goal_create.save()
                                        if scorer_id:
                                            d = Player_Model.objects.filter(id=scorer_id)
                                            if d:
                                                d2 = Player_Model.objects.get(id=scorer_id)
                                                previous_goal = d2.Total_goal_count
                                                d2.Total_goal_count = previous_goal + 1
                                                d2.save()

                                        if assist_id:
                                            dw = Player_Model.objects.filter(id=assist_id)
                                            if dw:
                                                dw2 = Player_Model.objects.get(id=assist_id)
                                                previous_assist = dw2.Total_assist_count
                                                dw2.Total_assist_count = previous_assist + 1
                                                dw2.save()

                                    if player and substitute_player and substitute_team_Home_or_way:
                                        Substituiton_create = Substituitons_Model(Event_for_goal=one_enevt,
                                                                                  PLayer_Name=player,
                                                                                  Substituitons_Name=substitute_player,
                                                                                  substitute_team_Home_or_way=substitute_team_Home_or_way)
                                        Substituiton_create.save()



                                    # change on team
                                    if win_option:
                                        Home_Team = Team_Model.objects.filter(Team_Name=one_enevt.Home_Team)

                                        if Home_Team:
                                            Home_Team = Team_Model.objects.get(Team_Name=one_enevt.Home_Team)

                                            # previous all record
                                            previous_Win_count = Home_Team.Win_count
                                            previous_Loos_count = Home_Team.Loos_count
                                            previous_Drow_count = Home_Team.Drow_count
                                            previous_GF = Home_Team.GF
                                            previous_GA = Home_Team.GA
                                            previous_GD = Home_Team.GD
                                            previous_PTS = Home_Team.PTS

                                            if win_option == one_enevt.Home_Team:
                                                Home_Team.Win_count = int(previous_Win_count)+1
                                                Home_Team.GF = int(previous_GF)+int(previous_Home_Team_Score)
                                                Home_Team.GA = int(previous_GA)+int(previous_Way_Team_Score)
                                                total_GA = int(previous_GF)+int(previous_Home_Team_Score)
                                                total_GF = int(previous_GA)+int(previous_Way_Team_Score)
                                                Home_Team.GD = total_GA - total_GF
                                                win_count = int(previous_Win_count)+1
                                                Home_Team.PTS = win_count*3

                                                Home_Team.save()

                                        way_Team = Team_Model.objects.filter(Team_Name=one_enevt.Way_Team)
                                        if way_Team:
                                            way_Team = Team_Model.objects.get(Team_Name=one_enevt.Way_Team)

                                            # previous all record
                                            previous_Win_count = way_Team.Win_count
                                            previous_Loos_count = way_Team.Loos_count
                                            previous_Drow_count = way_Team.Drow_count
                                            previous_GF = way_Team.GF
                                            previous_GA = way_Team.GA
                                            previous_GD = way_Team.GD
                                            previous_PTS = way_Team.PTS

                                            if win_option == one_enevt.Way_Team:
                                                way_Team.Win_count = int(previous_Win_count) + 1
                                                way_Team.GF = int(previous_GF) + int(previous_Way_Team_Score)
                                                way_Team.GA = int(previous_GA) + int(previous_Home_Team_Score)
                                                total_GA = int(previous_GF) + int(previous_Way_Team_Score)
                                                total_GF = int(previous_GA) + int(previous_Home_Team_Score)
                                                way_Team.GD = total_GA - total_GF
                                                win_count = int(previous_Win_count) + 1
                                                way_Team.PTS = win_count * 3

                                                way_Team.save()






                                    mag = {'massage': 'Data is Created'}
                                    json_data = JSONRenderer().render(mag)
                                    return HttpResponse(json_data, content_type='application/json')







                        else:
                            is_enevt = Event_Model.objects.filter(id=event_id)
                            if is_enevt:
                                one_enevt = Event_Model.objects.get(id=event_id)
                                is_game_present = Game_Model.objects.filter(Event_for_game=one_enevt)

                                # if present but not finished -------------------------------------------
                                if is_game_present:
                                    the_game_present = Game_Model.objects.get(Event_for_game=one_enevt)

                                    previous_Home_Team_Score = the_game_present.Home_Team_Score
                                    previous_Way_Team_Score = the_game_present.Way_Team_Score

                                    if home_team_goal_count_total and home_team_goal_count_total !=0:
                                        previous_Home_Team_Score = int(previous_Home_Team_Score)+int(home_team_goal_count_total)

                                    if way_team_goal_count_total  and way_team_goal_count_total != 0:
                                        previous_Way_Team_Score = int(previous_Way_Team_Score) + int(
                                            way_team_goal_count_total)

                                    if previous_Home_Team_Score:
                                        the_game_present.Home_Team_Score = previous_Home_Team_Score
                                    if previous_Way_Team_Score:
                                        the_game_present.Way_Team_Score = previous_Way_Team_Score
                                    if home_team_shot_on_target:
                                        the_game_present.Home_Team_Shot_on_target = home_team_shot_on_target
                                    if way_team_shot_on_target:
                                        the_game_present.Way_Team_Shot_on_target = way_team_shot_on_target
                                    if home_team_position:
                                        the_game_present.Home_Team_Position = home_team_position
                                    if way_team_position:
                                        the_game_present.Way_Team_Position = way_team_position
                                    if home_team_corner:
                                        the_game_present.Home_Team_Corner = home_team_corner
                                    if way_team_corner:
                                        the_game_present.Way_Team_Corner = way_team_corner
                                    the_game_present.save()

                                    if scorer_name and assist_name:
                                        if home_team_goal_count_total and home_team_goal_count_total !=0:
                                            goal_create = Goal_Model(Event_for_goal=one_enevt,
                                                                     Home_Team_Goal_Count_In_1='1',
                                                                     Scorer_Name=scorer_name,
                                                                     Goal_Assist_Name=assist_name)
                                            goal_create.save()
                                        if way_team_goal_count_total and way_team_goal_count_total != 0:
                                            goal_create = Goal_Model(Event_for_goal=one_enevt,
                                                                     way_team_goal_count_total='1',
                                                                     Scorer_Name=scorer_name,
                                                                     Goal_Assist_Name=assist_name)
                                            goal_create.save()

                                        if scorer_id:
                                            d = Player_Model.objects.filter(id=scorer_id)
                                            if d:
                                                d2 = Player_Model.objects.get(id=scorer_id)
                                                previous_goal = d2.Total_goal_count
                                                d2.Total_goal_count = previous_goal + 1
                                                d2.save()

                                        if assist_id:
                                            dw = Player_Model.objects.filter(id=assist_id)
                                            if dw:
                                                dw2 = Player_Model.objects.get(id=assist_id)
                                                previous_assist = dw2.Total_assist_count
                                                dw2.Total_assist_count = previous_assist + 1
                                                dw2.save()


                                    if player and substitute_player and substitute_team_Home_or_way:
                                        Substituiton_create = Substituitons_Model(Event_for_goal=one_enevt,
                                                                                  PLayer_Name=player,
                                                                                  Substituitons_Name=substitute_player,
                                                                                  substitute_team_Home_or_way=substitute_team_Home_or_way)
                                        Substituiton_create.save()

                                    mag = {'massage': 'Data is Created'}
                                    json_data = JSONRenderer().render(mag)
                                    return HttpResponse(json_data, content_type='application/json')






                                # fully new game-------------------------------------------------------------
                                else:
                                    home_team = one_enevt.Home_Team
                                    way_team = one_enevt.Way_Team

                                    is_home_team = Team_Model.objects.filter(Team_Name = home_team)
                                    is_way_team = Team_Model.objects.filter(Team_Name = way_team)


                                    if is_home_team and is_way_team:
                                        one_home_team = Team_Model.objects.get(Team_Name=home_team)
                                        one_way_team = Team_Model.objects.get(Team_Name=way_team)

                                        # home_team_goal_count_total = int(home_team_goal_count_total)
                                        # way_team_goal_count_total = int(way_team_goal_count_total)


                                        if home_team_goal_count_total == '':
                                            home_team_goal_count_total = 0

                                        if way_team_goal_count_total == '':
                                            way_team_goal_count_total = 0

                                        create_new_game = Game_Model(
                                            Event_for_game=one_enevt,


                                            Home_Team_Score=home_team_goal_count_total,

                                            Way_Team_Score=way_team_goal_count_total,

                                            Home_Team_Shot_on_target=home_team_shot_on_target,

                                            Way_Team_Shot_on_target=way_team_shot_on_target,

                                            Home_Team_Position=home_team_position,

                                            Way_Team_Position=way_team_position,

                                            Home_Team_Corner=home_team_corner,

                                            Way_Team_Corner=way_team_corner,

                                            home_Team_name=one_home_team.Team_Name,

                                            home_Team_manager_name=one_home_team.Manager.User_Name,

                                            home_Team_player_1_id_from_Plyer_model=one_home_team.Team_player_1_id_from_Plyer_model.id,

                                            home_Team_player_2_id_from_Plyer_model=one_home_team.Team_player_2_id_from_Plyer_model.id,

                                            home_Team_player_3_id_from_Plyer_model=one_home_team.Team_player_3_id_from_Plyer_model.id,

                                            home_Team_player_4_id_from_Plyer_model=one_home_team.Team_player_4_id_from_Plyer_model.id,

                                            home_Team_player_5_id_from_Plyer_model=one_home_team.Team_player_5_id_from_Plyer_model.id,

                                            home_Team_player_6_id_from_Plyer_model=one_home_team.Team_player_6_id_from_Plyer_model.id,

                                            home_Team_player_7_id_from_Plyer_model=one_home_team.Team_player_7_id_from_Plyer_model.id,
                                            home_Team_player_8_id_from_Plyer_model=one_home_team.Team_player_8_id_from_Plyer_model.id,
                                            home_Team_player_9_id_from_Plyer_model=one_home_team.Team_player_9_id_from_Plyer_model.id,
                                            home_Team_player_10_id_from_Plyer_model=one_home_team.Team_player_10_id_from_Plyer_model.id,
                                            home_Team_player_11_id_from_Plyer_model=one_home_team.Team_player_11_id_from_Plyer_model.id,
                                            home_Team_player_12_id_from_Plyer_model=one_home_team.Team_player_12_id_from_Plyer_model.id,
                                            home_Team_player_13_id_from_Plyer_model=one_home_team.Team_player_13_id_from_Plyer_model.id,
                                            home_Team_player_14_id_from_Plyer_model=one_home_team.Team_player_14_id_from_Plyer_model.id,
                                            home_Team_player_15_id_from_Plyer_model=one_home_team.Team_player_15_id_from_Plyer_model.id,home_Team_player_16_id_from_Plyer_model=one_home_team.Team_player_16_id_from_Plyer_model.id,home_Team_player_17_id_from_Plyer_model=one_home_team.Team_player_17_id_from_Plyer_model.id,home_Team_player_18_id_from_Plyer_model=one_home_team.Team_player_18_id_from_Plyer_model.id,
                                            home_Team_player_active_1_id_from_Plyer_model=one_home_team.Team_player_active_1_id_from_Plyer_model.id,
                                            home_Team_player_active_2_id_from_Plyer_model=one_home_team.Team_player_active_2_id_from_Plyer_model.id,
                                            home_Team_player_active_3_id_from_Plyer_model=one_home_team.Team_player_active_3_id_from_Plyer_model.id,
                                            home_Team_player_active_4_id_from_Plyer_model=one_home_team.Team_player_active_4_id_from_Plyer_model.id,
                                            home_Team_player_active_5_id_from_Plyer_model=one_home_team.Team_player_active_5_id_from_Plyer_model.id,
                                            home_Team_player_active_6_id_from_Plyer_model=one_home_team.Team_player_active_6_id_from_Plyer_model.id,
                                            home_Team_player_active_7_id_from_Plyer_model=one_home_team.Team_player_active_7_id_from_Plyer_model.id,
                                            home_Team_player_active_8_id_from_Plyer_model=one_home_team.Team_player_active_8_id_from_Plyer_model.id,
                                            home_Team_player_active_9_id_from_Plyer_model=one_home_team.Team_player_active_9_id_from_Plyer_model.id,
                                            home_Team_player_active_10_id_from_Plyer_model=one_home_team.Team_player_active_10_id_from_Plyer_model.id,
                                            home_Team_player_active_11_id_from_Plyer_model=one_home_team.Team_player_active_11_id_from_Plyer_model.id,
                                            home_Team_player_substitute_1_id_from_Plyer_model=one_home_team.Team_player_substitute_1_id_from_Plyer_model.id,
                                            home_Team_player_substitute_2_id_from_Plyer_model=one_home_team.Team_player_substitute_2_id_from_Plyer_model.id,
                                            home_Team_player_substitute_3_id_from_Plyer_model=one_home_team.Team_player_substitute_3_id_from_Plyer_model.id,
                                            home_Team_player_substitute_4_id_from_Plyer_model=one_home_team.Team_player_substitute_4_id_from_Plyer_model.id,
                                            home_Team_player_substitute_5_id_from_Plyer_model=one_home_team.Team_player_substitute_5_id_from_Plyer_model.id,home_Team_player_substitute_6_id_from_Plyer_model=one_home_team.Team_player_substitute_6_id_from_Plyer_model.id,home_Team_player_substitute_7_id_from_Plyer_model=one_home_team.Team_player_substitute_7_id_from_Plyer_model.id,
                                            way_Team_name=one_way_team.Team_Name,
                                            way_Team_manager_name=one_way_team.Manager.User_Name,
                                            way_Team_player_1_id_from_Plyer_model=one_way_team.Team_player_1_id_from_Plyer_model.id,
                                            way_Team_player_2_id_from_Plyer_model=one_way_team.Team_player_2_id_from_Plyer_model.id,
                                            way_Team_player_3_id_from_Plyer_model=one_way_team.Team_player_3_id_from_Plyer_model.id,
                                            way_Team_player_4_id_from_Plyer_model=one_way_team.Team_player_4_id_from_Plyer_model.id,
                                            way_Team_player_5_id_from_Plyer_model=one_way_team.Team_player_5_id_from_Plyer_model.id,
                                            way_Team_player_6_id_from_Plyer_model=one_way_team.Team_player_6_id_from_Plyer_model.id,
                                            way_Team_player_7_id_from_Plyer_model=one_way_team.Team_player_7_id_from_Plyer_model.id,
                                            way_Team_player_8_id_from_Plyer_model=one_way_team.Team_player_8_id_from_Plyer_model.id,
                                            way_Team_player_9_id_from_Plyer_model=one_way_team.Team_player_9_id_from_Plyer_model.id,
                                            way_Team_player_10_id_from_Plyer_model=one_way_team.Team_player_10_id_from_Plyer_model.id,
                                            way_Team_player_11_id_from_Plyer_model=one_way_team.Team_player_11_id_from_Plyer_model.id,
                                            way_Team_player_12_id_from_Plyer_model=one_way_team.Team_player_12_id_from_Plyer_model.id,
                                            way_Team_player_13_id_from_Plyer_model=one_way_team.Team_player_13_id_from_Plyer_model.id,
                                            way_Team_player_14_id_from_Plyer_model=one_way_team.Team_player_14_id_from_Plyer_model.id,
                                            way_Team_player_15_id_from_Plyer_model=one_way_team.Team_player_15_id_from_Plyer_model.id,way_Team_player_16_id_from_Plyer_model=one_way_team.Team_player_16_id_from_Plyer_model.id,way_Team_player_17_id_from_Plyer_model=one_way_team.Team_player_17_id_from_Plyer_model.id,way_Team_player_18_id_from_Plyer_model=one_way_team.Team_player_18_id_from_Plyer_model.id,
                                            way_Team_player_active_1_id_from_Plyer_model=one_way_team.Team_player_active_1_id_from_Plyer_model.id,
                                            way_Team_player_active_2_id_from_Plyer_model=one_way_team.Team_player_active_2_id_from_Plyer_model.id,
                                            way_Team_player_active_3_id_from_Plyer_model=one_way_team.Team_player_active_3_id_from_Plyer_model.id,
                                            way_Team_player_active_4_id_from_Plyer_model=one_way_team.Team_player_active_4_id_from_Plyer_model.id,
                                            way_Team_player_active_5_id_from_Plyer_model=one_way_team.Team_player_active_5_id_from_Plyer_model.id,
                                            way_Team_player_active_6_id_from_Plyer_model=one_way_team.Team_player_active_6_id_from_Plyer_model.id,
                                            way_Team_player_active_7_id_from_Plyer_model=one_way_team.Team_player_active_7_id_from_Plyer_model.id,
                                            way_Team_player_active_8_id_from_Plyer_model=one_way_team.Team_player_active_8_id_from_Plyer_model.id,
                                            way_Team_player_active_9_id_from_Plyer_model=one_way_team.Team_player_active_9_id_from_Plyer_model.id,
                                            way_Team_player_active_10_id_from_Plyer_model=one_way_team.Team_player_active_10_id_from_Plyer_model.id,
                                            way_Team_player_active_11_id_from_Plyer_model=one_way_team.Team_player_active_11_id_from_Plyer_model.id,
                                            way_Team_player_substitute_1_id_from_Plyer_model=one_way_team.Team_player_substitute_1_id_from_Plyer_model.id,
                                            way_Team_player_substitute_2_id_from_Plyer_model=one_way_team.Team_player_substitute_2_id_from_Plyer_model.id,
                                            way_Team_player_substitute_3_id_from_Plyer_model=one_way_team.Team_player_substitute_3_id_from_Plyer_model.id,
                                            way_Team_player_substitute_4_id_from_Plyer_model=one_way_team.Team_player_substitute_4_id_from_Plyer_model.id,way_Team_player_substitute_5_id_from_Plyer_model=one_way_team.Team_player_substitute_5_id_from_Plyer_model.id,way_Team_player_substitute_6_id_from_Plyer_model=one_way_team.Team_player_substitute_6_id_from_Plyer_model.id,way_Team_player_substitute_7_id_from_Plyer_model=one_way_team.Team_player_substitute_7_id_from_Plyer_model.id, is_game_finished="running")
                                        create_new_game.save()
                                        one_enevt.is_game_finished = "running"
                                        one_enevt.save()

                                        # ...........................








                                        if scorer_name and assist_name:
                                            if home_team_goal_count_total and home_team_goal_count_total !=0:
                                                goal_create = Goal_Model(Event_for_goal=one_enevt, Home_Team_Goal_Count_In_1 = '1', Scorer_Name=scorer_name, Goal_Assist_Name=assist_name)
                                                goal_create.save()
                                            if way_team_goal_count_total and way_team_goal_count_total != 0:
                                                goal_create = Goal_Model(Event_for_goal=one_enevt, way_team_goal_count_total='1', Scorer_Name=scorer_name, Goal_Assist_Name=assist_name)
                                                goal_create.save()

                                            if scorer_id:
                                                d = Player_Model.objects.filter(id=scorer_id)
                                                if d:
                                                    d2 = Player_Model.objects.get(id=scorer_id)
                                                    previous_goal = d2.Total_goal_count
                                                    d2.Total_goal_count = previous_goal + 1
                                                    d2.save()

                                            if assist_id:
                                                dw = Player_Model.objects.filter(id=assist_id)
                                                if dw:
                                                    dw2 = Player_Model.objects.get(id=assist_id)
                                                    previous_assist = dw2.Total_assist_count
                                                    dw2.Total_assist_count = previous_assist + 1
                                                    dw2.save()



                                        if player and substitute_player and substitute_team_Home_or_way:
                                            Substituiton_create = Substituitons_Model(Event_for_goal=one_enevt, PLayer_Name=player, Substituitons_Name=substitute_player, substitute_team_Home_or_way=substitute_team_Home_or_way)
                                            Substituiton_create.save()

                                        mag = {'massage': 'Data is Created'}
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




