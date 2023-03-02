from django.db import models


# Create your models here.

class Specialities(models.Model):
    specialitie = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.specialitie)


class Doctor(models.Model):
    docname = models.CharField(max_length=100, default="")
    specialitie = models.ForeignKey(Specialities, on_delete=models.CASCADE)
    twt = models.CharField(max_length=100, default="")
    fb = models.CharField(max_length=100, default="")
    lkin = models.CharField(max_length=100, default="")
    insta = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=12, default="")
    city = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.docname)


class Appointment(models.Model):
    patientName = models.CharField(max_length=100, default="")
    service = models.ForeignKey(Specialities, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, default="")
    doctName = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    status = models.BooleanField(default="False")
    date = models.CharField(max_length=10, default="")
    time = models.CharField(max_length=10, default="")

    def __str__(self):
        return str(self.patientName)


class SiteReview(models.Model):
    email = models.CharField(max_length=30, default="")
    review = models.CharField(max_length=150, default="")


class Contact(models.Model):
    email = models.CharField(max_length=30, default="")
    message = models.CharField(max_length=150, default="")
