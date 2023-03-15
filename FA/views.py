from django.shortcuts import render, HttpResponse
from .models import FA_Model
from . serializers import FA_Model_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from Event.models import Event_Model

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

@csrf_exempt
def find_all_FA(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        spacific_news_id = request.POST.get('spacific_news_id')
        category_value = request.POST.get('category_value')
        print('category_value')
        print(category_value)

        if Process == 'see_all_FA':
            # .order_by('-id')
            get_spacific_info = FA_Model.objects.all()
            serializer_var = FA_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')

        elif Process == 'see_one_FA' and spacific_news_id:
            get_spacific = FA_Model.objects.filter(id=spacific_news_id)
            if get_spacific:
                get_spacific_info = FA_Model.objects.get(id=spacific_news_id)
                serializer_var = FA_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')


        elif Process == 'find_with_category_FA' and category_value:
            get_spacific = FA_Model.objects.filter(category=category_value)
            if get_spacific:
                get_spacific_info = FA_Model.objects.filter(category=category_value)
                serializer_var = FA_Model_serializer(get_spacific_info, many=True)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')



        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')



@csrf_exempt
def find_all_FA_with_category_subcategory(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        category_value = request.POST.get('category_value')
        subcategory_value = request.POST.get('subcategory_value')
        print('category_value')
        print(category_value)


        if Process == 'find_with_category_and_subcategory_FA' and category_value and subcategory_value:
            get_spacific = FA_Model.objects.filter(category=category_value).filter(subcategory=subcategory_value)
            if get_spacific:
                get_spacific_info = FA_Model.objects.filter(category=category_value).filter(subcategory=subcategory_value)
                serializer_var = FA_Model_serializer(get_spacific_info, many=True)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')



        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')






@csrf_exempt
def FA_delete(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        deleted_FA_id = request.POST.get('deleted_FA_id')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'delete' and get_user_info.User_Roll == 'Admin' and deleted_FA_id:
                        get_spacific_info = FA_Model.objects.filter(id=deleted_FA_id)
                        if get_spacific_info:
                            one_get_spacific_info = FA_Model.objects.get(id=deleted_FA_id)
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
def FA_update(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        update_FA_id = request.POST.get('update_FA_id')

        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        photo = request.FILES.get('photo')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        Description = request.POST.get('Description')
        video_link = request.POST.get('video_link')


        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'update' and get_user_info.User_Roll == 'Admin' and update_FA_id:
                        get_spacific_info = FA_Model.objects.filter(id=update_FA_id)
                        if get_spacific_info:
                            one_get_spacific_info = FA_Model.objects.get(id=update_FA_id)
                            if title:
                                one_get_spacific_info.title=title
                            if subtitle:
                                one_get_spacific_info.subtitle = subtitle
                            if photo:
                                one_get_spacific_info.photo = photo

                            if category:
                                one_get_spacific_info.category = category

                            if subcategory:
                                one_get_spacific_info.subcategory = subcategory

                            if Description:
                                one_get_spacific_info.Description = Description
                            if video_link:
                                one_get_spacific_info.video_link = video_link

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
def create_specific_FA(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        photo = request.FILES.get('photo')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        Description = request.POST.get('Description')
        video_link = request.POST.get('video_link')


        print(title)
        print(subtitle)
        print(photo)
        print(category)
        print(subcategory)
        print(Description)
        print(video_link)

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    print('34343434')
                    if Process == 'create' and get_user_info.User_Roll =='Admin' and title and subtitle and photo and category:
                        print('22222')

                        get_spacific_info = FA_Model(title=title, subtitle=subtitle,subcategory=subcategory, photo=photo, category=category, Description=Description, video_link=video_link)
                        get_spacific_info.save()
                        print('33333')

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
