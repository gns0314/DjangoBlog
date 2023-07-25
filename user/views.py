from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import RegisterForm, LoginForm
# Create your views here.


# 회원가입
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'user/user_register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')


# 로그인
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password) 
            
            if user:
                login(request, user)
                return redirect('blog:list')
            
        form.add_error(None, '아이디가 없습니다.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)
    
    
# 로그아웃
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')
    

# 비밀번호 변경
class ChangePassword(View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        context = {
            'form': form,
        }
        return render(request, 'user/change_password.html', context)
    
    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('user:logout', pk=request.user.pk)
        else:
            messages.error(request, '비밀번호 변경에 실패했습니다. 다시 시도해주세요.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/change_password.html', context)
