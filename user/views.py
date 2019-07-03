from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import get_user, authenticate, login, logout
from .models import profile
from django.views.decorators.csrf import csrf_protect
from django.template import Context, Template, loader
from . import templates
from django import template
@csrf_protect


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully registered")
    else:
        form = RegistrationForm()

    return render(request, "signup.html", {'form': form})

@csrf_protect           
def loginp(request):
    
    if request.method == 'POST':
        f = LoginForm(request.POST)
        
        if f.is_valid:
            un = request.POST["username"]
            ps = request.POST["Password"]
            pob = profile.objects.all()
            li = []
            for each in pob:
                li.append(each.username)
            if un not in li:
                return HttpResponse("User with this username doesnot exist")
            num_results = profile.objects.get(username = un )
            
            if num_results is not None:
                
                if ps == num_results.password:
                    login(request, num_results)
                    
                    request.session['member_id'] =  num_results.pk
                    
                    
                    
                    
                    return render(request, "home.html")  
                else:
                    return HttpResponse("password mismatch")                  
            else:
                
                return HttpResponse("you are not a valid user")
    else:
        f = LoginForm()
    return render(request, "login.html", {'form':f})
# Create your views here.

@csrf_protect
def logout_view(request):
    
    if request.session['member_id'] is not None:
        
        del request.session['member_id']
        request.session.modified = True
        logout(request)
        return HttpResponse("Logged out")
    

   
    
    


    