# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from tlmshop.models.manufacturer import Manufacturer


admin.site.register(Manufacturer, admin.ModelAdmin)
