from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomRegisterForm





def register(request):
    if request.method=="POST":
       userform= CustomRegisterForm(request.POST)
       if userform.is_valid():
          instance=userform.save(commit=False)
          instance.manage=request.user
          instance.save()
          messages.success(request,"Registration done successfully please login")
          return redirect('register')
          
          
       else:
         
         for field, errors in userform.errors.items():
              messages.error(request,errors)
         print(userform.errors)
         return redirect('register')
    else:
        userform= CustomRegisterForm()
        return render(request,'register.html',{'userform':userform})




