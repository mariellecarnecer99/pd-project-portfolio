# contact/views.py

from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            inquiry = form.cleaned_data['inquiry']
            how_did_you_hear = form.cleaned_data['how_did_you_hear']
            message = form.cleaned_data['message']

            # Manually map choices to labels
            inquiry_choices = {
                'website_design': 'Website Design',
                'graphic_design': 'Graphic Design',
                'branding': 'Branding',
                'development': 'Development'
            }

            how_did_you_hear_choices = {
                'google_search': 'Google Search',
                'referral': 'Referral',
                'social_media': 'Social Media'
            }

            # Get the human-readable labels for inquiry and how_did_you_hear
            inquiry_label = inquiry_choices.get(inquiry)
            how_did_you_hear_label = how_did_you_hear_choices.get(how_did_you_hear)

            # Prepare the subject and content of the email
            subject = 'Contact Form Submission from {}'.format(first_name + ' ' + last_name)
            body = f"""
            Phone: {phone}

            Message: {message}

            Inquiry: {inquiry_label}
            
            How did you hear about us: {how_did_you_hear_label}
            """

            # Create the email
            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=email,  # Sender email
                to=['mcarnecer@startechup.com'],  # Recipient email list
                reply_to=[email]  # Reply-to email from the form input
            )

            # Send the email
            email_message.send()

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
  return render(request, 'contact/success.html', {'message': 'Thank you for contacting us!'})