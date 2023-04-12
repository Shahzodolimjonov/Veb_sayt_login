from django.contrib import messages
from django.shortcuts import render,redirect
from .models import News,Category
from django.contrib.auth.forms import UserCreationForm

from .forms import NewsForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    news= News.objects.all()
    categories=Category.objects.all()
    content={
        'news':news,
        'categories':categories,
    }
    return render(request,'news/index.html', context=content)

def category(request, pk):
    news = News.objects.filter(category=pk)
    categories = Category.objects.all()
    content = {
        'news': news,
        'categories': categories
    }
    return render(request, 'news/category.html', context=content)

def detail(request, pk):
    news = News.objects.get(pk=pk)
    categories = Category.objects.all()
    content = {
        "news": news,
        "categories": categories
    }
    return render(request, 'news/detail.html', context=content)

def n_del(request, pk):
    news = News.objects.get(pk=pk)
    news.delete()
    return redirect('home')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect('login')
    content = {
        'form':form,
    }
    return render(request, 'news/register.html',context=content)


def loginPase(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    content = {}
    return render(request, 'news/login.html', context=content)

def logoutUser(request):
    return redirect('login')




