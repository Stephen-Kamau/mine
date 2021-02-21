from django.conf.urls import url
from django.urls import path
app_name = "my_view"
from . import views

urlpatterns = [
  path('' , views.index , name  = 'index'),
  path('email/' , views.send_email , name='email')
]
