from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required


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
            return redirect('list')
        else:
            return redirect('login')
    return render(request,'login.html')
        # Return an 'invalid login' error message.

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request , 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request,pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request,'detail.html',{'object':object})
    
def goodfunc(request,pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')

def readfunc(request,pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')
