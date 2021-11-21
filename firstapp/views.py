from django.shortcuts import render,HttpResponse
from datetime import datetime
from firstapp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    #context={"variable":"this is sent","variable1":"beats audio"} in below also u have to add context afer index.html
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("About page")
def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is Services Page")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your massage has been sent !.')
    return render(request, 'contact.html')
    #return HttpResponse("Contact Us")
def team(request):
    return render(request, 'team.html')
    #return HttpResponse("Team Page")
def career(request):
    return render(request, 'career.html')
    #return HttpResponse("Career Page")