from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import registrationform 

# Create your views here.
def register(request):
    if request.method=='POST':
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # password1 = form.cleaned_data.get('password1')
            # user = auth.authenticate(username=username,password=password1)
            # auth.login(request, user)
            messages.info(request, f'Hello {username}, You are Successfully Registered!!') 
            return render(request, 'success.html',)
            form = registrationform()
    else:
        form = registrationform()
    return render(request, 'register.html', {'form':form})

