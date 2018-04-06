# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin


# Register your models here.


from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)







