
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def home(request):
    context = {

    }
    return render( request , 'index.html'  )



''' This function is for the all the param for the logging user'''

def signinpage(request):
    if request.method == 'POST' :
        username = request.POST['user']
        password1 = request.POST['pass']

        user = auth.authenticate(username = username , password = password1)
        if user is not None :
            auth.login(request , user)
            return redirect('dashboard')
        else:
            return redirect('login')

    else:
        return render(request , 'signinpage.html')


''' This function is for the all the param for the registering user'''
def register(request):
    if request.method == 'POST' :
        username = request.POST['user']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        email = request.POST['email']


        if password1 == password2 :
            if User.objects.filter(username = username):
                return redirect('register')

            else :
                user = User.objects.create_user(username = username , password = password1 , email = email)
                user.save()
                return redirect('/')
        else:
            return redirect('register')
    return render(request , 'register.html')








@login_required(login_url='login')
def dashboard(request):

    return render(request , 'dashboard.html')