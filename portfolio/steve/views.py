from django.shortcuts import render
# from django.core.mail import send_mail
# from django.conf import settings
import smtplib

def index(request):
    return render(request , 'index.html')


def send_email(request):
    print(request.method)
    if request.method == 'POST':
        # execute
        email = request.POST['email']
        text = request.POST['text']
        name = request.POST['name']
        print(name)

        try:
            msg = """ Hi Its {name}  email {email}  and message  {text}"""
            s = smtplib.SMTP('smtp.gmail.com' , 587)
            s.login('stephenkamau714@gmail.com' , '0705698768')
            s.sendmail('stephenkamau714@gmail.com' ,'stiveckamash@gmail.com', msg)
            # send_mail(
            # "Response" ,
            # msg,
            # 'stephenkamau714@gmail.com',
            # ['stiveckamash@gmail.com'],
            # fail_silently=False,)
            print("successs")
        except Exception as e:
            print("errrorroror" , e)

        else:
            return render(request , 'index.html')





    return render(request , 'index.html')
