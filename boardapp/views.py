from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username_request=request.POST['username']
        password_request=request.POST['password']
        try:
            User.objects.get(username=username_request)
            return render(request,'signup.html',{'error':'このユーザーはすでに登録されています'})

        except:
            user = User.objects.create_user(username_request, '', password_request)
            return render(request,'signup.html',{'some':100})
    return render(request,'signup.html',{'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username_request=request.POST['username']
        password_request=request.POST['password']    
        user = authenticate(username=username_request, password=password_request)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('signup')
        else:
            return redirect('login')
    return render(request,'login.html')
        # Return an 'invalid login' error message.

def listfunc(request):
    return render(request , 'list.html')