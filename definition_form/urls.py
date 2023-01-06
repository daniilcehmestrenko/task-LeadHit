from django.urls import path

from .views import GetForm

urlpatterns = [
        path('', GetForm.as_view(), name='get_form'),
    ]
