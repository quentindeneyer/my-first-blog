# -*- coding: utf-8 -*-
from django import forms

from .models import Workshop

class WorkshopForm(forms.ModelForm):
    workshop_start_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',),label='Fecha limite de inscripción')
    registration_limit_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'),
                                 input_formats=('%d/%m/%Y',),label='Fecha (inicio) del taller (si corresponde)')
    class Meta:
        model = Workshop
        fields = ('organizer','title','desc','workshop_start_date','registration_limit_date','min_age','max_age','price','price_is_for','url_information','contact_email','contact_phone')
        labels = {
            'organizer': ('Organizador'),
            'title': ('Título del taller'),
            'desc': ('Descripción breve'),
            'workshop_start_date': ('Fecha (inicio) del taller (si corresponde)'),
            'registration_limit_date': ('Fecha limite de inscripción'),
            'min_age': ('Edad mínima'),
            'max_age': ('Edad máxima'),
            'price': ('Precio'),
            'price_is_for': ('(opcional) El valor es por'),
            'url_information': ('(recomendado) Link a información detallada'),
            'contact_phone': ('Teléfono de contacto'),
            'contact_email': ('Email de contacto'),
        }
        help_texts = {
            'title': ('Hazlo convincing'),
        }
        error_messages = {
            'title': {
                'max_length': ("Nombre demasiado largo"),
            },
        }