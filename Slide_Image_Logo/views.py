from django.shortcuts import render, HttpResponse
from .models import Slide_Model, Logo_Model
from . serializers import Slide_Model_Model_serializer, Logo_Model_Model_serializer
from User_info.models import User_information
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from Event.models import Event_Model

from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

@csrf_exempt
def find_all_Slide_logo(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        if Process == 'see_slide':
            get_spacific_info = Slide_Model.objects.all()
            serializer_var = Slide_Model_Model_serializer(get_spacific_info, many=True)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')
    
    
    
    
    
@csrf_exempt
def delete_Slide_logo_with_id(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        id = request.POST.get('id')
        
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        
        
        
        
        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'delete_slide' and get_user_info.User_Roll == 'Admin':
                        get_spacific_info = Slide_Model.objects.filter(id=id)
                        
                        if get_spacific_info:
                            get_spacific_info = Slide_Model.objects.get(id=id)
                            get_spacific_info.delete()
                            
                            mag = {'massage': 'Data is Deleted'}
                            json_data = JSONRenderer().render(mag)
                            return HttpResponse(json_data, content_type='application/json')
                        else:
                            mag = {'massage': 'Data is Not Present'}
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
def create_Slider(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        Slider_image = request.FILES.get('Slider_image')
        Slider_title = request.POST.get('Slider_title')
        
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'create' and get_user_info.User_Roll == 'Admin':
                        
                        get_spacific_info = Slide_Model(Slide_title=Slider_title, Slide_Image=Slider_image)
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
def find_last_main_logo(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        if Process == 'see_slide':
            get_spacific_info = Logo_Model.objects.last()
            serializer_var = Logo_Model_Model_serializer(get_spacific_info, many=False)
            json_data = JSONRenderer().render(serializer_var.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            HttpResponse('NOT VALID')

    return HttpResponse('NO GET METHOD ALLOWED')


@csrf_exempt
def create_main_logo(request):
    if request.method == "POST":
        Process = request.POST.get('Process')
        logo_image = request.FILES.get('logo_image')
        
        
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        if user_name and password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):

                    if Process == 'create' and get_user_info.User_Roll == 'Admin' and logo_image:
                        get_spacific_info = Logo_Model(Logo_Image=logo_image)
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