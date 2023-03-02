import random

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Doctor, Specialities, Appointment,Contact,SiteReview


# Create your views here.
def home(request, ):
    specialities = Specialities.objects.all()
    docts = Doctor.objects.all()
    context = {'docts': docts, 'specialities': specialities}

    return render(request, 'home.html', context)


def loadDoct(request):
    service = request.GET.get('service')
    docts = Doctor.objects.filter(specialitie=service)


def appointment(request):
    age = request.POST['age']
    service = request.POST['service']
    doct = request.POST['doct']
    patient = request.POST['patient']
    email = request.POST['email']
    appointdate = request.POST['appointdate']
    appointtime = request.POST['appointtime']

    serv = Specialities.objects.filter(id=service)
    docts = Doctor.objects.filter(id=doct)
    id = random.randint(100000, 999999)
    b = Appointment(id=id, patientName=patient, service=serv[0], doctName=docts[0], date=appointdate, time=appointtime,
                    email=email)
    b.save()
    print("###########")
    print(b.save())
    print("###########")
    return appointmentView(request, id)
    # return HttpResponse(service + " " + doct + " " + patient + " " + email + " " + appointdate + " " + appointtime)


def appointmentView(request, submited=None):
    serviceid = request.POST['service']
    docts = Doctor.objects.filter(specialitie=serviceid)
    print(submited)
    context = {'docts': docts, 'service': serviceid, 'submited': submited}
    return render(request, 'appointment.html', context)


def trackappointment(request):
    return render(request, 'track-appointment.html')


def track(request):
    trackrId = request.POST['trackrId']
    appointment = Appointment.objects.filter(id=trackrId)
    context = {'appointment': appointment}
    return render(request, 'track-appointment.html', context)


def priceView(request):
    specialities = Specialities.objects.all()
    context = {'specialities': specialities}
    return render(request, 'pricing.html', context)


def aboutView(request):
    return render(request, 'about.html')


def serviceView(request):
    return render(request, 'service.html')


def doctProfileView(request,slug):
    doct = Doctor.objects.filter(id=slug)
    context = {'doct':doct}
    return render(request, 'docprofile.html',context)

def contactDoct(request):
    return render(request,"contact.html")

def btnappoint(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/#appointment')


def findDoct(request):
    date = request.POST['date']
    time = request.POST['time']
    serviceid = request.POST['service']
    appointment = Appointment.objects.filter(service=serviceid, date=date, time=time)
    print("###########")
    aptDoctList = []
    for i in appointment:
        aptDoctList.append(i.doctName.id)
    aptDoctList = set(aptDoctList)
    # print(aptDoctList)
    allDoct = Doctor.objects.filter(specialitie=serviceid)
    ablDoct = []
    for i in allDoct:
        if not (i.id in aptDoctList):
            ablDoct.append(i)
    print(ablDoct)
    context = {'ablDoct': ablDoct}
    print("###########")
    return render(request, "available-doctor.html", context)

def contactForm(request):
    email = request.POST['email']
    message = request.POST['message']
    b = Contact(message= message,email=email)
    b.save()
    submited = True
    context = {'submited':submited}
    # return HttpResponse(email)
    return render(request,"contact.html",context)

def reviewForm(request):
    email = request.POST['email']
    message = request.POST['message']
    b = Contact(message= message,email=email)
    b.save()
    submitedReview = True
    context = {'submited':submitedReview}
    # return HttpResponse(email)
    return render(request,"contact.html",context)

