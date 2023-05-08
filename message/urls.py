from django.urls import path, include
from . import views

urlpatterns = [
    path('send/', views.message_view),
    path('', include('applift.urls')),
]