from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    return render(request, 'App/Home.html')


def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('Home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'App/Register.html', context)


def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = AuthenticationForm()
    return render(request, 'App/Login.html', context={'form': form})


def LogOut(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Home')

@login_required
def Admin(request):
    return render(request, 'App/Admin.html')
