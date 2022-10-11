from django.shortcuts import render

# Create your views here.
def home(request):
    page={'name':'home'}
    return render(request,'app/home.html',page)


def about(request):
    page={'name':'about'}
    return render(request,'app/about.html',page)