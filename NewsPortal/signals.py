from django.core.mail import mail_managers, EmailMultiAlternatives
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post



def post_for_subscribers(subscriber, title, short_text, subscribers, pk):
    html_content = render_to_string('posts/post_for_subscribers.html',
                                    {'text': short_text,
                                     "link": f'http://127.0.0.1:8000/post/{pk}',
                                     "user": subscriber})
    # for n in subscribers_email:
    message = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email='heavydawg.vio@gmail.com',
        to=subscribers
    )
    message.attach_alternative(html_content, "text/html")  # добавляем htm
    message.send()