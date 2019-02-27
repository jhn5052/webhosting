from django.shortcuts import render, redirect
from django.contrib.auth.models import User #user에 대한 클래스
from django.contrib import auth #user에 대한 권한


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) #회원명단 확인
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html', {'error' : 'username or password is incorrect!'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password']) #쿼리셋 기본 함수 create_user(username, userpassword)
            auth.login(request, user) #자동적으로 로그인 하는 함수
            return redirect('home') #로그인 성공하면 home
    return render(request, 'signup.html') #로그인 실패하면 signup에 머물러있기

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')