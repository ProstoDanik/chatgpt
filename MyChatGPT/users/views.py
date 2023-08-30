from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate



# Create your views here.
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/login.html', {'form': AuthenticationForm(), 'error': 'Имя пользователя и пароль не совпадают'})
        else:
            login(request, user)
            return redirect('home')



