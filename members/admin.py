# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Members

# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Members, MembersAdmin)

