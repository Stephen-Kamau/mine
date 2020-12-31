from django.shortcuts import render

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.core.mail import send_mail , EmailMessage
from django.conf import settings
import smtplib
from django.conf import settings
sender = settings.EMAIL_HOST_USER
def index(request):
    return render(request , 'index.html')



def send_email(request):
    print(request.method)
    if request.method == 'POST':
        # execute
        email = request.POST['email']
        text = request.POST['text']
        name = request.POST['name']
        receiver = 'stiveckamash@gmail.com'
        # sender = 'stephen.kamau@attorn.tech'
        print(name)

        try:
            msg = f"""
            <p>Hi Its <p> <h2>{name} \n</h2><br>
            <p>Email : {email}  \n<br></p>
            <p>Message : {text} \n<br></p>"""
            message = EmailMessage(
            "Hi there Its me passing here<br>" ,
            msg,
            sender,
            [receiver],
            )
            message.content_subtype = 'html'
            message.send(fail_silently=False)
            print("successs")
        except Exception as e:
            print("errrorroror" , e)

        else:
            return render(request , 'index.html')






    return render(request , 'index.html')
