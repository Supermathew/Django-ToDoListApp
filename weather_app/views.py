from django.shortcuts import render ,redirect
from django.http import HttpResponse
from weather_app.models import Todolist,Contact
from weather_app.forms import Taskform,Contactform
from django.contrib import messages
from weather_app.forms import Taskform
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
           instance=form.save(commit=False)
           instance.manage=request.user
           instance.save()
           messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:
        alltask= Todolist.objects.filter(manage=request.user)
        paginator = Paginator(alltask,5)
        page=request.GET.get('pg')
        alltask= paginator.get_page(page)
        return render(request,'home.html',{'alltask':alltask})

@login_required
def contact(request):
    if request.method == "POST":
       print("happyaman")
       usercontactform =Contactform(request.POST or None)
       if usercontactform.is_valid():
          instance=usercontactform.save(commit=False)
          instance.manage=request.user
          instance.save()
          print("happywala")
          messages.success(request,("Message Send Successfully!"))
       else:
          print("happywalaaaaa")
          for field, errors in usercontactform.errors.items():
              mess='{}-:{}'.format(field, ','.join(errors))
              
              messages.error(request,mess)

       return redirect('contact')
    else:
        return render(request,'contact.html',{})
    

def about(request):
    # context={'about':"welcome to about page",}
    return render(request,'about.html', {})

@login_required
def taskupdate(request,task_id):
    if request.method == "POST":
        taskwala = Todolist.objects.get(pk=task_id)
        taskmill = Taskform(request.POST or None,instance=taskwala)
        print(taskmill)
        if taskmill.is_valid():
           taskmill.save()
           messages.success(request,("Task Updated Successfully!"))
        return redirect('todolist')

@login_required
def taskfalse(request, task_id):
    tasktrue = Todolist.objects.get(pk=task_id)
    tasktrue.done=True
    tasktrue.save()
    return redirect('todolist')

@login_required
def tasktrue(request, task_id):
    tasktrueo = Todolist.objects.get(pk=task_id)
    tasktrueo.done=False
    tasktrueo.save()
    return redirect('todolist')

@login_required
def deletetask(request, task_id):
    tasktrueo = Todolist.objects.get(pk=task_id)
    tasktrueo.delete()
    return redirect('todolist')

def indexpage(request):
    context={'welcome to home index page'}

    return render(request,'index.html',{'context': context})

# def message(request):
#     print("happymathew")
#     if request.method == "POST":
#        print("happyaman")
#        usercontactform =Contactform(request.POST or None)
#        if usercontactform.is_valid():
#           usercontactform.save()
#           print("happywala")
#           messages.success(request,("Message Send Successfully!"))
#        else:
#           print("happywalaaaaa")
#           print(usercontactform.errors)

#     return redirect('contact')


def save_contact(request):
    # Extract the contact details from the request object
    name = request.POST.get('form_name')
    email = request.POST.get('form_lastname')
    message = request.POST.get('form_email')
    formneed = request.POST.get('form_need')
    message = request.POST.get('form_message')

    
    
    
    # Create a new Contact object and save it to the database
    contact = Contact(name=name, email=email, message=message)
    contact.save()
    
    # Return a JSON response indicating success
    return JsonResponse({'success': True})
    

