from django import forms

from .models import Viaje, Destino
import datetime
from django.forms.extras.widgets import *
from django.forms import ModelForm, Form
from django.contrib.admin import widgets
from bootstrap3_datepicker import *
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.db import models


class ViajeForm(forms.ModelForm):


    class Meta:
        model = Viaje
        #start_date = forms.DateField(widget=SelectDateWidget)

        fields = '__all__'


        widgets = {
        #NOT Use localization and set a default format
        'start_date': DateTimeWidget(usel10n=True, bootstrap_version=3),
        'end_date'  : DateTimeWidget(usel10n=True, bootstrap_version=3)
        }


class DestinoForm(forms.ModelForm):

    class Meta:
        model = Destino
        fields = '__all__'

        widgets = {
        #NOT Use localization and set a default format
        'start_date': DateWidget(usel10n=True, bootstrap_version=3),
        'end_date'  : DateWidget(usel10n=True, bootstrap_version=3)
        }

    def clean(self):
        cleaned_data=super(DestinoForm,self).clean

        startdate = self.cleaned_data['start_date']
        enddate = self.cleaned_data['end_date']

        if startdate is None:
            raise forms.ValidationError("Fecha de inicio incompleta.")
        if enddate is None:
            raise forms.ValidationError("Fecha de fin incompleta.")
        else:
            if enddate < startdate:
                raise forms.ValidationError("Fecha de fin debe ser mayor a fecha de inicio")








