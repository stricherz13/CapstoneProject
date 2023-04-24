from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == "POST":
        form_contact_name = request.POST['form-contact-name']
        form_contact_email = request.POST['form-contact-email']
        form_contact_message = request.POST['form-contact-message']

        #send an email
        send_mail(
            f'Website contact form - {form_contact_email}',
            form_contact_message,
            form_contact_email,
            ['stltaxauctionmap@gmail.com'],
        )

        return render(request, 'pages/contact.html', {'form_contact_name': form_contact_name})
    else:
        return render(request, 'pages/contact.html')


def donate(request):
    return render(request, 'pages/donate.html')


def faq(request):
    return render(request, 'pages/faq.html')


def terms(request):
    return render(request, 'pages/terms.html')
