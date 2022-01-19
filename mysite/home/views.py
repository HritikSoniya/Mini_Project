from django.shortcuts import render,HttpResponse

# Create your views here.
import requests
# import threading
import sys
import re
import shutil
from bs4 import BeautifulSoup as soup

im = ['https://www.drivespark.com/images/80x20xyt_logo_rgb_dark.png.pagespeed.ic.SGLlBkgVSt.png', 'https://images.oneindia.com/notification/images/addr-bar.png','https://www.drivespark.com/wallimg/360x80/photos/2019-seat-cupra-ateca/seat-cupra-ateca-suv-01.jpg', 'https://images.oneindia.com/notification/images/arrow1.png']
def index(request):
    # return HttpResponse("this is home page")}
    context={
        "variable1":'https://www.drivespark.com/images/80x20xyt_logo_rgb_dark.png.pagespeed.ic.SGLlBkgVSt.png',
        "variable2":'https://images.oneindia.com/notification/images/addr-bar.png',
        "variable3":'https://www.drivespark.com/wallimg/360x80/photos/2019-seat-cupra-ateca/seat-cupra-ateca-suv-01.jpg'
    }
    return render(request,"index.html",context)

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contect(request):
    return render(request,"contect.html")






