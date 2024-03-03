from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from hashlib import sha256
from .models import Activation


def validate_password(request, password, confirm_password):
    if password != confirm_password:
        messages.add_message(request, constants.ERROR, 'As senhas não são iguais.')
        return False
    return True

    
def send_email(username, email, token):
    ## Pega o conteúdo do HTML que vai ser enviado
    context = {
        'name': username,
        'activation_link': f'http://127.0.0.1:8000/account/activate_account/{token}/'
    }
    html_content = render_to_string('emails/confirmed_registration.html', context)
    ## Converte o HTML para TXT
    text_content = strip_tags(html_content)
    ## Assunto / Conteúdo / Remetente / Destinatário
    email = EmailMultiAlternatives('Confirmação de cadastro', text_content, settings.EMAIL_HOST_USER, [email,])
    ## Envio do email - Conteúdo / Formato
    email.attach_alternative(html_content, 'text/html')
    email.send()
    return True
    
    
def create_token(user, email):
    ## O Token e ativação do usuário será a concatenação entre o nome de usuário e email
    ## O sha256 precisa que essa string esteja em binário, por isso o encode()
    ## O sha256 retorna um método (um endereço de memória) que precisa ser convertido para hexadecimal, por isso o hexdigest
    token = sha256(f'{user.username}{email}'.encode()).hexdigest()
    activation = Activation(token=token, user=user)
    activation.save()  

    return token