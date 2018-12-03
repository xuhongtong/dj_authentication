import time

from celery import shared_task
from django.core.mail import send_mail

from dj_authentication import settings


@shared_task
def sendmail(content):
    # content = loader.render_to_string('email.html',request=request)
    time.sleep(10)
    return send_mail(subject='邮件激活',
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['1422633402@qq.com']
              )
    # return render(request,'msg.html')