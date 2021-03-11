from django.core.mail import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from .forms import MessageForm
from .models import Project, Experience


def home(request):

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid:

            message_form.save()


            sender_name = request.POST.get('first_name', '') + " " + request.POST.get('last_name')
            sender_email = request.POST.get('email_address')
            message_content = request.POST.get('content', '')
            subject = "Received Message From " + sender_name
            message = "Captain,\n\nThe following message was received from your personal portfolio site (" \
                      "matthew-harrop.com):\n\nSender: " + sender_name + "\n\nContact: " +\
                      request.POST.get('email_address', '') + "\n\nMessage: " +\
                      request.POST.get('content', '') + "\n\nRegards,\n\nAdmin"
            if sender_name and sender_email and message_content:
                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER, ['osaintspreserveus@live.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
                # In reality we'd use a form class
                # to get proper validation errors.
                print("Something went wrong sending the email")
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    message_form = MessageForm()
    return render(request, 'portfolio/home.html', {
        'projects': projects,
        'experiences': experiences,
        'message_form': message_form})
