from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def careers(request):
    return render(request, 'careers.html')


def why_us(request):
    return render(request, 'why_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')

def gallery(request):
    return render(request,'gallery.html')
