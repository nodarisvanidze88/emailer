from django.urls import path
from .views import status_ok, email_sender
urlpatterns = [
    path('', status_ok, name='status_ok'),
    path('send-email/', email_sender, name='email_sender'),
    # Define your URL patterns here
    # Example:
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]