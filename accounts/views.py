from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()

    return render(request,'accounts/sign_up.html',{'form':form})




def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:article_list')
    else:
        form = AuthenticationForm()
    
    return render(request,'accounts/sign_in.html',{'form':form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:article_list')