from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('create/', views.create_event, name='create'),
    path('register/<int:event_id>/', views.register_event, name='register'),
    path('<int:event_id>/', views.event_detail, name='detail'),
]

