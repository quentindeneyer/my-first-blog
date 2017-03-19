# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Workshop
from .models import Organizer

admin.site.register(Workshop)
admin.site.register(Organizer)