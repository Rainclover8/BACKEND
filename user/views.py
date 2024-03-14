from django.contrib.auth import authenticate, login as _, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def update_password(request):
    
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
           form = changePasswordForm(current_user, request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, 'Şifreniz değiştirilmiştir lütfen tekrar giriniz..')
            #    login(current_user)
               return redirect('login')
           else:
                messages.warning(request, 'Hatalı veya eksik girdiniz')
                return redirect('update_password')
           
                
        else:
            form = changePasswordForm(current_user)
            context={
                'form':form
            }
            return render(request, 'updateUserPass.html', context)
    else:
        messages.warning(request, 'Giriş yapmış olamanız gerekmekte lütfen giriş yapınız...')
        return redirect('login')
        
    


def register(request):
    
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Hesap Oluşturuldu! Giriş yapınız')
            return redirect('login')
        else:
            messages.warning(request, 'Eksik veya hatalı girdiniz')
    else:
        form = registerForm()
        
    
    return render(request, 'register.html',{'form':form})

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            _(request, user)  
            messages.success(request, 'Giriş başarılı')
            return redirect('index') 
        else:
            messages.warning(request, 'Yanlış bilgi girdiniz')
            return redirect('login')  
    else:
        return render(request, 'login.html')
    
    
    
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, 'Çıkış Yapıldı!')
    return redirect('index')