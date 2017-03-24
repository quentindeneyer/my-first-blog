# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Organizer(models.Model):
    administrator = models.ForeignKey('auth.User', default=0)
    name = models.CharField(max_length=75)
    contact_email = models.EmailField(max_length=100, default='')
    contact_phone = models.BigIntegerField(default=0)
    url_logo = models.URLField(max_length=1000, default = '')
    def __str__(self):
        return self.name
    def publish(self):
        self.save()

class Workshop(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=44, default='')
    desc = models.TextField(max_length=185,default='')
    contact_email = models.EmailField(max_length=75, default='', null=True, blank=True)
    contact_phone = models.BigIntegerField(default=0)
    workshop_start_date = models.DateField(
            blank=True, null=True)
    registration_limit_date = models.DateField(
            blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)    
    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=100)
    price = models.IntegerField(default=0)
    price_is_for = models.CharField(max_length=30,default='',blank=True,null=True)
    url_information = models.URLField(max_length=1000,blank=True,null=True)
    def string_or_link(message,request):
        if request.user.is_authenticated():
            return "<a href=\"{%  url 'workshop_edit' pk=workshop.pk %}\">{ { "+message+"  } }</a>"
        else:
            return message
    def spanish_3_letters_month(self):
        a=['ENE','FEB','MAR','ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC']
        return a[self.workshop_start_date.month-1]
    def publish(self):
        self.created_date = timezone.now()
        self.contact_email = organizer.contact_email
        self.contact_phone = organizer.contact_phone
        self.save()
    def __str__(self):
        return self.title


# class Workshop(models.Model):
#     organizer = models.ForeignKey(Organizer)
#     title = models.CharField(max_length=60)
#     desc = models.TextField(max_length=200)
#     contact_email = models.EmailField(max_lenght=100)
#     contact_phone = models.BigIntegerField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     workshop_start_date = models.DateTimeField(
#             blank=True, null=True)
#     registration_limit_date = models.DateTimeField(
#             blank=True, null=True)
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#     def __str__(self):
#         return self.title    
