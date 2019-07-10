from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send email notification when an order is succesfully placed.
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have succesfully placed an order. Your order id is {}.'.format('Suren',order.id)
    mail_sent = send_mail(subject,message,'suren.abrahamyan89@gmail.com',[order.email])
    print("ORDER MESSAGE + ",message)
    return mail_sent