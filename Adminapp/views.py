from django.shortcuts import render
import os
import requests
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
def track_page(request):
    return render(request, "track_page.html")


def track_result(request):
    cn_number = request.GET.get("cn")

    if not cn_number:
        return render(request, "track_page.html", {"error": "Enter CN number"})

    aws_url = f"https://ceejaycourier.mysmeclabs.com/staff/api/track/{cn_number}/"

    response = requests.get(
        aws_url,
        headers={
            "X-API-KEY": os.environ.get("TRACKING_API_KEY")
        }
    )

    if response.status_code == 200:
        data = response.json()
        return render(request, "track_result.html", {"data": data})
    else:
        return render(request, "track_page.html", {"error": "Consignment Not Found"})