from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EmailForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            cc = form.cleaned_data['cc']
            to = ['eyobwebsite@gmail.com']
            if cc:
                to = [sender]
                send_mail(subject, message, sender, to, fail_silently=False)
                to = ['eyobwebsite@gmail.com']
                message += "\n%s" % sender
                send_mail(subject, message, sender, to, fail_silently=False)
            else:
                message += "\n%s" % sender
                send_mail(subject, message, sender, to, fail_silently=False)

            return HttpResponseRedirect('/contact/')

    else:
        form = EmailForm()

    return render(request, 'contact/contact.html', {'form': form})
