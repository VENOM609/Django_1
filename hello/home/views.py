from django.shortcuts import render, HttpResponse
from home.models import contact

# Create your views here.
def index(request):
    return render(request, 'index.html')
   # return HttpResponse("this is home page")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("we are nothing but everything")
def booking(request):
    return render(request, 'booking.html')
    #return HttpResponse("you can book here")
def contact(request):
    if request.method == "POST":
        
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        reasion = request.POST.get('reasion')
        Contact = contact(phone = phone, email = email, reasion = reasion)
        Contact.save()

    return render(request, 'contact.html')
    #return HttpResponse("message us for contact")