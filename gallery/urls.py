from django.urls import path
from .views import Groups

urlpatterns = [
    path('', Groups.as_view()),
]
