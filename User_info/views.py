from django.shortcuts import render, HttpResponse
from . models import User_information
from . serializers import User_information_serializer

from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q

# Create your views here.
def index(request):
    l = User_information.objects.get(id=1)
    print(l)

    serializer_var =User_information_serializer(l, many=False)

    # json_data = JSONRenderer.render(serializer_var.data)
    json_data = JSONRenderer().render(serializer_var.data)


    return HttpResponse(json_data, content_type='application/json')



@csrf_exempt
def find_user(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        print(user_name)
        print(password)

        if user_name and password:

            user_info = User_information.objects.filter(User_Name=user_name)
            if user_info:
                print('11111')
                get_user_info = User_information.objects.get(User_Name=user_name)
                if check_password(password, get_user_info.User_Password):
                    print('22222')

                    if Process == 'see':
                        mag = {'massage': get_user_info.User_Roll}
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
def create_user(request):
    if request.method == "POST":

        Process = request.POST.get('Process')

        admin_user_name = request.POST.get('admin_user_name')
        admin_password = request.POST.get('admin_password')

        User_Roll = request.POST.get('User_Roll')
        User_Name = request.POST.get('User_Name')
        User_Password = request.POST.get('User_Password')
        User_Email = request.POST.get('User_Email')
        User_Phone = request.POST.get('User_Phone')


        if admin_user_name and admin_password:
            print('11111')

            user_info = User_information.objects.filter(User_Name=admin_user_name)
            if user_info:

                get_user_info = User_information.objects.get(User_Name=admin_user_name)
                if check_password(admin_password, get_user_info.User_Password):

                    if Process == 'create' and get_user_info.User_Roll == 'Admin' and User_Roll and User_Roll != 'Admin' and User_Name and User_Password and User_Email and User_Phone:

                        get_spacific_info = User_information(User_Roll=User_Roll, User_Name=User_Name, User_Password=User_Password, User_Email=User_Email, User_Phone=User_Phone)
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
