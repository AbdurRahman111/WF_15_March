from django.shortcuts import render, HttpResponse
from .models import Player_Model
from . serializers import Player_Model_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

@csrf_exempt
def find_all_player(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        spacific_news_id = request.POST.get('spacific_news_id')

        if Process == 'see_all_player':
            get_spacific_info = Player_Model.objects.all()
            serializer_var = Player_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')

        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def find_one_player(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        spacific_news_id = request.POST.get('spacific_player_id')
        print('Process')
        print(Process)
        print(spacific_news_id)

        if Process == 'see_one_player' and spacific_news_id:
            print('11111')
            get_spacific = Player_Model.objects.filter(id=spacific_news_id)
            if get_spacific:
                print('2222')
                get_spacific_info = Player_Model.objects.get(id=spacific_news_id)
                serializer_var = Player_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')
            else:
                HttpResponse('NOT VALID')

        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')






@csrf_exempt
def player_delete(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        deleted_player_id = request.POST.get('deleted_player_id')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'delete' and get_user_info.User_Roll == 'Admin' and deleted_player_id:
                        get_spacific_info = Player_Model.objects.filter(id=deleted_player_id)
                        if get_spacific_info:
                            one_get_spacific_info = Player_Model.objects.get(id=deleted_player_id)
                            one_get_spacific_info.delete()


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
def player_update(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        update_player_id = request.POST.get('update_player_id')

        PLayer_Name = request.POST.get('PLayer_Name')
        PLayer_Jersey = request.POST.get('PLayer_Jersey')
        PLayer_Position = request.POST.get('PLayer_Position')
        PLayer_Age = request.POST.get('PLayer_Age')
        PLayer_Photo = request.FILES.get('PLayer_Photo')
        Base_price = request.POST.get('Base_price')
        Sell_price = request.POST.get('Sell_price')

        Description = request.POST.get('Description')

        player_local_or_foreign = request.POST.get('player_local_or_foreign')


        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'update' and get_user_info.User_Roll == 'Admin' and update_player_id:
                        get_spacific_info = Player_Model.objects.filter(id=update_player_id)
                        if get_spacific_info:
                            one_get_spacific_info = Player_Model.objects.get(id=update_player_id)
                            if PLayer_Name:
                                one_get_spacific_info.PLayer_Name=PLayer_Name
                            if PLayer_Jersey:
                                one_get_spacific_info.PLayer_Jersey = PLayer_Jersey
                            if PLayer_Position:
                                one_get_spacific_info.PLayer_Position = PLayer_Position

                            if PLayer_Age:
                                one_get_spacific_info.PLayer_Age = PLayer_Age

                            if PLayer_Photo:
                                one_get_spacific_info.PLayer_Photo = PLayer_Photo
                            if Base_price:
                                one_get_spacific_info.Base_price = Base_price
                            if Sell_price:
                                one_get_spacific_info.Sell_price = Sell_price
                            if Description:
                                one_get_spacific_info.Description = Description
                            if player_local_or_foreign:
                                one_get_spacific_info.player_local_or_foreign = player_local_or_foreign

                            one_get_spacific_info.save()


                        mag = {'massage': 'Data is Updated'}
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
def create_player(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        PLayer_Name = request.POST.get('PLayer_Name')
        PLayer_Jersey = request.POST.get('PLayer_Jersey')
        PLayer_Position = request.POST.get('PLayer_Position')
        PLayer_Age = request.POST.get('PLayer_Age')
        PLayer_Photo = request.FILES.get('PLayer_Photo')
        Base_price = request.POST.get('Base_price')
        Sell_price = request.POST.get('Sell_price')

        Description = request.POST.get('Description')

        player_local_or_foreign = request.POST.get('player_local_or_foreign')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):


                    if Process == 'create' and get_user_info.User_Roll =='Admin' and PLayer_Name and PLayer_Jersey and PLayer_Position:

                        get_spacific_info = Player_Model(PLayer_Name=PLayer_Name, PLayer_Jersey=PLayer_Jersey, PLayer_Position=PLayer_Position, PLayer_Age=PLayer_Age, PLayer_Photo=PLayer_Photo, Base_price=Base_price, Sell_price=Sell_price, Description=Description, player_local_or_foreign=player_local_or_foreign)
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
