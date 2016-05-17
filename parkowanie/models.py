from django.db import models
from django.utils import timezone


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        s = "Tytul: " + self.title + " (id=" + str(self.id) + ")\n"
        s += "tresc: " + str(self.text) + "\n"
        s += "data utworzenia: " + str(self.created_date) + "\n"
        s += "data publikacji: " + str(self.published_date) + "\n"
        s += "autor: " + str(self.author) + "\n"
        return s


class RegisterModel(models.Model):
    login = models.CharField( max_length=30)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    passw = models.CharField(max_length=30)
    passw2 = models.CharField(max_length=30)

    def __str__(self):
        s = self.login + ' ' + self.name + ' ' + self.surname + ' ' + self.email + ' ' + self.passw
        return s


class LoginModel(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        s = self.login + ' ' + self.password
        return s

class Park(models.Model):
    name = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=30, null=False)
    street = models.CharField(max_length=30, null=False)
    street_nr = models.IntegerField(null=False)
    spacing = models.IntegerField(null=False)
    length = models.IntegerField(null=False)
    width = models.IntegerField(null=False)
    free = models.IntegerField(null=False)
    data = models.TextField(max_length=10000)

    def __str__(self):
        s = "Nazwa: " + self.name + " (id=" + str(self.id) + ")\n"
        s += "Miasto: " + str(self.city) + "\n"
        s += "Ulica: " + str(self.street) + " " + str(self.street_nr) + "\n"
        s += "Miejsca parkingowe: " + str(self.spacing) + "\n"
        s += "Miejsca wolne: " + str(self.free) + "\n"
        return s
