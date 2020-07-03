from django.urls import path
from .views import *

urlpatterns = [
    path('', surveyList, name='survey-list'),
    path('<int:id>/', survey, name='single-survey'),
]