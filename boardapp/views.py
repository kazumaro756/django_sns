from django.shortcuts import render
from django.contrib.auth.models import User

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