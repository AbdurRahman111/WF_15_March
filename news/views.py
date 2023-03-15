from django.shortcuts import render, HttpResponse
from .models import News_Model, News_catagory
from . serializers import News_Model_serializer, News_catagory_Model_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from Event.models import Event_Model

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

@csrf_exempt
def find_all_news(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        spacific_news_id = request.POST.get('spacific_news_id')

        if Process == 'see_all_news':
            get_spacific_info = News_Model.objects.all()
            serializer_var = News_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')

        elif Process == 'see_one_news' and spacific_news_id:
            get_spacific = News_Model.objects.filter(id=spacific_news_id)
            if get_spacific:
                get_spacific_info = News_Model.objects.get(id=spacific_news_id)
                serializer_var = News_Model_serializer(get_spacific_info, many=False)
                json_data = JSONRenderer().render(serializer_var.data)
                return HttpResponse(json_data, content_type='application/json')



        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def news_category(request):
    if request.method == "POST":
        Process = request.POST.get('Process')


        if Process == 'see_news_category':
            get_spacific_info = News_catagory.objects.all()
            serializer_var = News_catagory_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')


        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def news_category_delete(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        deleted_category_id = request.POST.get('deleted_category_id')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'delete' and get_user_info.User_Roll == 'Admin' and deleted_category_id:
                        get_spacific_info = News_catagory.objects.filter(id=deleted_category_id)
                        if get_spacific_info:
                            one_get_spacific_info = News_catagory.objects.get(id=deleted_category_id)
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
def news_delete(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        deleted_news_id = request.POST.get('deleted_news_id')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'delete' and get_user_info.User_Roll == 'Admin' and deleted_news_id:
                        get_spacific_info = News_Model.objects.filter(id=deleted_news_id)
                        if get_spacific_info:
                            one_get_spacific_info = News_Model.objects.get(id=deleted_news_id)
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
def news_update(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        update_news_id = request.POST.get('update_news_id')

        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        photo = request.FILES.get('photo')
        category = request.POST.get('category')
        Description = request.POST.get('Description')
        video_link = request.POST.get('video_link')


        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'update' and get_user_info.User_Roll == 'Admin' and update_news_id:
                        get_spacific_info = News_Model.objects.filter(id=update_news_id)
                        if get_spacific_info:
                            one_get_spacific_info = News_Model.objects.get(id=update_news_id)
                            if title:
                                one_get_spacific_info.title=title
                            if subtitle:
                                one_get_spacific_info.subtitle = subtitle
                            if photo:
                                one_get_spacific_info.photo = photo

                            if category:
                                cat = None
                                if category:
                                    j = News_catagory.objects.filter(Catagory=category)
                                    if j:
                                        try:
                                            cat = News_catagory.objects.get(Catagory=category)
                                        except:
                                            cat = News_catagory.objects.filter(Catagory=category).last()

                                one_get_spacific_info.category = cat
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
def news_category_create(request):
    if request.method == "POST":
        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        new_category = request.POST.get('new_category')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'create' and get_user_info.User_Roll == 'Admin' and new_category:

                        get_spacific_info = News_catagory(Catagory=new_category)
                        get_spacific_info.save()

                        mag = {'massage': 'Data is Created'}
                        json_data = JSONRenderer().render(mag)
                        return HttpResponse(json_data, content_type='application/json')

                    else:
                        HttpResponse('NOT VALID')
                else:
                    HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')



@csrf_exempt
def find_news_with_category(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        category = request.POST.get('category')

        if Process == 'find_news_with_category' and category:
            get_spacific_info = News_Model.objects.filter(category = category)
            serializer_var = News_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')


        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def create_specific_news(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        photo = request.FILES.get('photo')
        category = request.POST.get('category')
        Description = request.POST.get('Description')
        video_link = request.POST.get('video_link')

        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):


                    if Process == 'create' and get_user_info.User_Roll =='Admin' and title and photo and category:

                        cat=None
                        if category:
                            j = News_catagory.objects.filter(Catagory=category)
                            if j:
                                try:
                                    cat = News_catagory.objects.get(Catagory=category)
                                except:
                                    cat = News_catagory.objects.filter(Catagory=category).last()


                        if cat:
                            get_spacific_info = News_Model(title=title,  photo=photo, category=cat, Description=Description, video_link=video_link)
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
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')

