from django.conf.urls import url


app_name = "my_view"
from . import views

urlpatterns = [
  url('^$' , views.index , name  = 'index'),
  url('sendEmail/' , views.send_email , name  = 'send_email')
]
