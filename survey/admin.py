from django.contrib import admin
from survey.models import *

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)