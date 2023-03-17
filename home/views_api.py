from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import blogPostModel


# Login API
class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'something went wrong'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'username not entered'
                raise Exception('key username not entered')
            
            if data.get('password') is None:
                response['message'] = 'password not entered'
                raise Exception('key password not entered')
            
            check_user = User.objects.filter(username =  data.get('username')).first()
            if check_user is None:
                response['message'] = 'invalid username'
                raise Exception('key username invalid')
            
            user_obj = authenticate(username = data.get('username'), password = data.get('password'))

            if user_obj:
                login(request, user_obj )
                response['status'] = 200
                response['message'] = 'Login Successful'
            else:
               response['message'] = 'invalid password'
               raise Exception('key password invalid') 
            
            
        except Exception as e:
            print(e)

        return Response(response)
    
LoginView = LoginView.as_view()




 
# Register API
class RegisterView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'something went wrong'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'username not entered'
                raise Exception('key username not entered')
            
            if data.get('password') is None:
                response['message'] = 'password not entered'
                raise Exception('key password not entered')
            
            check_user = User.objects.filter(username =  data.get('username')).first()
            if check_user:
                response['message'] = 'username already exists'
                raise Exception('key username already exists')
            
            user_obj = User.objects.create(username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()

            response['status'] = 200
            response['message'] = 'user created successfully'
            
        except Exception as e:
            print(e)

        return Response(response)

RegisterView = RegisterView.as_view()


