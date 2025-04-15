from django.shortcuts import render, redirect # type: ignore

# Create your views here.

from django.http import HttpResponse # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth import authenticate, login # type: ignore

def index(request):
    return HttpResponse("K E S H A R___B H A V A N I")

def home(request):
    return render(request, 'Home.html')

def master(request):
    return render(request, 'master.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

from django.shortcuts import render # type: ignore
from .models import Contact, Std_form, crud

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save data to the database
        Contact.objects.create(name=name, email=email, message=message)

        # Provide feedback to the user (optional)
        return render(request, 'contact.html', {"success": True})

    return render(request, 'contact.html')


def ecommerce(request):
    return render(request, 'ecommerce.html')


def registration(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        username = request.POST.get("userName")
        password = request.POST.get("password")
    
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already taken choose another.")
            return redirect('/registration/')

        if first_name and last_name and username and password:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
            )
            user.set_password(password)
            user.save()
            messages.success(request,"Thankyou for registration")
            return redirect('/registration/')
    return render(request, 'registration.html')

def login(request):
    #return redirect('/login/')
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def index(request):
    return render(request, 'index.html')


def std_form(request):
    if request.method =="POST":
        studentName =request.POST.get("studentName")
        studentAge =request.POST.get("studentAge")
        gender =request.POST.get("gender")
        enrollmentNumber =request.POST.get("enrollmentNumber")
        contact =request.POST.get("contact")
        course =request.POST.get("course")
        Std_form.objects.create(studentName=studentName,studentAge=studentAge,gender=gender,enrollmentNumber=enrollmentNumber,contact=contact,course=course)
        
        studentAge =request.POST.get("studentAge")
    return render(request,'std_form.html')

def Crud(request):
    return render(request, 'crud.html')

def crud_input(request):
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        age = request.POST.get('age')
        photo = request.FILES.get('photo')

        crud.objects.create(
            name=name,
            city=city,
            age=age,
            photo=photo
        ) 
        # return redirect('crud_input')
    queryset = crud.objects.all()
    context = {'crud_input':queryset}

    return render(request, 'crud_input.html',context)

def delete_id(request, id):
    queryset = crud.objects.get(id = id)
    queryset.delete()
    return redirect('/crud_input')



#ip address

# from django.http import HttpResponse

# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0].strip()
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

# def show_ip(request):
#     ip = get_client_ip(request)
#     return HttpResponse(f"Your IP address is: {ip}")
