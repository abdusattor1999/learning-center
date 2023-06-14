from django.shortcuts import render, redirect
from .models import *
from django import forms
from django.core.mail import send_mail
from django.conf import settings

# send mail 
def sendSimpleEmail( title, name:str, msg :str, contact:str, reciever):
    subject = title
    message = f"Yuboruvchi : {name.title()}\nAloqa : {contact}\n\nKurs turi : \n{msg}"
    email_from = settings.EMAIL_HOST_USER
    recipient = [reciever]
    ms = send_mail(subject, message, email_from, recipient)
    print("Message Sent", ms)
    return True
# end send mail

class ArizaForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15)
    course = forms.CharField(max_length=50)

def home(request):
    courses = Course.objects.filter(active=True)
    teachers = Teacher.objects.all()
    categories = Category.objects.all()

    return render(request, 'home.html', locals())



def course_details(request, pk=None):
    if request.method == 'POST':
        form = ArizaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            sendSimpleEmail('Kurs uchun yangi ariza !', data['name'], data['course'], data['phone'],"abdusattor.work@gmail.com" )
            return redirect('courses:home')
    
    course = Course.objects.filter(id=pk, active=True).last()
    return render(request, 'courses/course_details.html', {'course':course})


def teacher(request, pk=None):
    teachers = Teacher.objects.all()
    # if pk:
    #     teacher = Teacher.objects.filter(id=pk)
    #     return render(request, 'courses/teacher_details.html', {'teacher':teacher})
    return render(request, 'courses/teachers.html', {'teachers':teachers})

