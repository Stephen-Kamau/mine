from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.core.mail import send_mail , EmailMessage
from django.conf import settings
import smtplib
from django.conf import settings
from django.http import JsonResponse
sender = settings.EMAIL_HOST_USER


def index(request):
    return render(request , 'index.html')



@csrf_exempt
def send_email(request):
    if request.method == "POST":
        email = request.POST['email']
        text = request.POST['text']
        name = request.POST['name']
        phone = request.POST['phone']
        receiver = 'stiveckamash@gmail.com'
        sender = 'stephen.kamau@attorn.tech'

        try:
            msg = f"""
            <h2>YOu Have Received an Email From Website Contack Form \n
            Here are the Senders Details</h2>
            <h3>Name  : {name}<br />
            Email : {email}  <br /></p>
            Message : {text} <br /></h3>
            """

            message = EmailMessage(
            "Hello PortFolio Contact Form Message" ,
            msg,
            sender,
            [receiver],
            )
            message.content_subtype = 'html'
            message.send(fail_silently=False)
            print("successs")
        except Exception as e:
            JsonResponse({"msg":'Failed to send the email' ,"status":0 })

        else:
            return JsonResponse({"msg":'Message Send Successfully' ,"status":1 })

    return JsonResponse({"msg":'Failed to send the email' ,"status":0 })
