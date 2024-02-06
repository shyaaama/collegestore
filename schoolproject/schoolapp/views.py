from multiprocessing import context
from typing import Self
from django.contrib.auth import logout
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from . forms import LoginForm,PersonCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .models import Person,Course

from django.views import View
from django.urls import reverse_lazy
def base(request):
    return render(request,'base.html')
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    return redirect('schoolapp:new_page')
                else:
                    return HttpResponse('disabled')
            else:
                return HttpResponse('invalid')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
                
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('schoolapp:login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
def new_page(request): 
     return render(request,'new_page.html') 
def confirm_view(request): 
     return render(request,'confirm_page.html')
# yourapp/views.py
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            return redirect('schoolapp:person_add')
    return render(request, 'home.html', {'form': form})
def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    #return render(request, 'schoolapp:courses.html', {'courses': courses})
    return JsonResponse(list(courses.values('id', 'name')), safe=False)




def logout_view(request):
    logout(request)
    # Optionally, you can redirect the user to a specific page after logout
    return redirect('/')


    

