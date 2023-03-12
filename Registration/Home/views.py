from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from . models import Registration
from django.contrib.auth import authenticate, login 
# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        role=request.POST.get('role')
        email=request.POST.get('email')
        country=request.POST.get('country')
        nationality=request.POST.get('nationality')
        phone_number=request.POST.get('phone_number')        
        
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken')
            return redirect('Registration:signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already taken')
            return redirect('Registration:signup')
        else:
            user=User.objects.create_user(username=username,email=email,password=password,)
            user.save()
            user_registration=Registration.objects.create(name=username,password=password,role=role,email=email,country=country,nationality=nationality,phone_number=phone_number)
            user_registration.save()
            return redirect('Registration:login')
    return render(request,'signup.html')

# function for login
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email).username
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            user_role = Registration.objects.get(email=email).role
            if user_role == '1':
                return redirect('Registration:student')
            elif user_role == '2':
                return redirect('Registration:staff')
            elif user_role == '3':
                return redirect('Registration:admin_view')
            elif user_role == '4':
                return redirect('Registration:editor')
        else:
            messages.error(request, 'Invalid Email or Password')
            return redirect('Registration:login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('Registration:signup')

def student(request):
    return render(request,'student.html')

def staff(request):
    return render(request,'staff.html')

def admin_view(request):
    return render(request,'admin.html')

def editor(request):
    return render(request,'editor.html')
