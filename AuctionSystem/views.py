from django.shortcuts import redirect, render
from .models import registration
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone_no')
        password = request.POST.get('password')
        user = registration.objects.create(f_name=f_name, l_name=l_name, email=email, phone_no=phone_no, password=password)
        user.save()
        print("User registered successfully!")
        return redirect('login')
    return render(request,'login.html')

def loginn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = registration.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            request.session['user_name'] = user.f_name
            print(f"Login successful for {user.f_name}!")
            return redirect('index')
        except registration.DoesNotExist:
            print("Invalid email or password.")
    return render(request,'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')