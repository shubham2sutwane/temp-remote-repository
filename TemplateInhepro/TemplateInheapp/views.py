from django.shortcuts import render
from .forms import Contactform
from .models import ContactData
from .forms import FeedbackForm
from .models import FeedbackData
import datetime
from django.http.response import HttpResponse


def home_page_view(request):
    return render(request, 'Home.html')


def contact_page_view(request):
    if request.method == "POST":
        cform = Contactform(request.POST)
        if cform.is_valid():
            name1 = request.POST.get('name','')
            loc1 = request.POST.get('location','')
            sal1 = request.POST.get('salary','')
            email = request.POST.get('email','')
            a = ContactData(name=name1,
                          location=loc1,
                          salary=sal1,
                          email=email)
            a.save()
            cform = Contactform()
            return render(request, 'Register.html', {'abcd': cform})
        else:
            return HttpResponse("Invalid Data")
    else:
        cform = Contactform()
        return render(request, 'Register.html', {'abcd': cform})


def visitors_page_view(request):
    data = ContactData.objects.all()
    return render(request, 'Visitors.html', {'data': data})


date1 = datetime.datetime.now()


def feedback_page_view(request):
    if request.method == "POST":
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('rating')
            feedback1 = request.POST.get('feedback')
            a = FeedbackData(
                name=name1,
                rating=rating1,
                feedback=feedback1,
                date=date1
            )
            a.save()
            fform = FeedbackForm()
            fdb = FeedbackData.objects.all()
            return render(request, 'Feedback.html', {'fform': fform, 'fdb': fdb})
        else:
            return HttpResponse("User Invalid Data")
    else:
        fform = FeedbackForm()
        fdb = FeedbackData.objects.all()
        return render(request, 'Feedback.html', {'fform': fform, 'fdb': fdb})



