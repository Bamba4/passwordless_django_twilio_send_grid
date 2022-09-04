import uuid
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .verify import SendOTP
from .check_code import CheckOTP

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        phone_number = form.cleaned_data.get("phone_number")
        new_user = User.objects.create_user(username, email, phone_number, password=None)
        return redirect("/login")
    return render(request, "auth/register.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
    "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        try:
            new = User.objects.get(email=email)
            print(new, "NEW_YORK_TIMEZONE")
            ## if user exists
            ##first: send otp to the user 
            SendOTP.send_code(email)
            print("Bonjour tout le monde")
            ##second:redirect to the page to enter otp 
            temp = uuid.uuid4()
            return redirect("/otp/{}/{}".format(new.pk, temp))
        except Exception as e:
            messages.error(request, f"No such user exists! {e}") 
    
    return render(request, "auth/login.html", context)

def generate_otp(request, pk, uuid):
    return render(request, 'otp.html')


def check_otp(request):
    otp =request.POST.get("secret")
    email = request.POST.get("email")
    otp_status= CheckOTP.check_otp(email, otp) 
    if otp_status == "approved":
        user = authenticate(request, email=email) 
      
        if user is not None:
           login(request, user, backend='verification.auth_backend.PasswordlessAuthBackend')
           return redirect("/home")
        else:
            messages.error(request, "Wrong OTP!") 

    print("otp via form: {}".format(otp))
    return render(request, "otp.html")

def home_page(request):
    return render(request, "home_page.html")