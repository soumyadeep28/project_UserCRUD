
from django.shortcuts import render

# Create your views here.

def home(request):
    context = {

    }
    return render( request , 'index.html'  )




def signinpage(request):

    return render(request , 'signinpage.html')



def register(request):

    return render(request , 'register.html')
