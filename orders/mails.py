from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from facilito_store import settings
from django.urls import reverse # Esta función nos retorna un String

class Mail:
    
    @staticmethod
    def get_absolute_url(url):
        if settings.DEBUG: # En modo desarrollo
            return 'http://localhost:8000{}'.format(
                reverse(url)
            )
    
    
    
       
    @staticmethod
    def send_complete_order(order, user):
        subject = 'Tu pedido ha sido enviado'
        template = get_template('orders/mails/complete.html')
        
        content = template.render({
            'user': user,
            'next_url': Mail.get_absolute_url('orders:completeds')
            
        })
        
        message = EmailMultiAlternatives(subject, 'Mensaje Importante', settings.EMAIL_HOST_USER,
                                         [user.email])
        message.attach_alternative(content, 'text/html')
        message.send()