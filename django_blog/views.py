from django.shortcuts import redirect,render

def Homepage(request):
    return render(request,'homepage.html')