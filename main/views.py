
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    context = {

    }
    return render( request , 'index.html'  )




def signinpage(request):

    return render(request , 'signinpage.html')



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
