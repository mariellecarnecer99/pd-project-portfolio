from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)

    # Adding the "Project/Service Inquiry" select field
    inquiry = forms.ChoiceField(
        choices=[
            ('', 'Choose...'),
            ('website_design', 'Website Design'),
            ('graphic_design', 'Graphic Design'),
            ('branding', 'Branding'),
            ('development', 'Development')
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # "How did you hear about us?" field
    how_did_you_hear = forms.ChoiceField(
        choices=[
            ('', 'Choose...'),
            ('google_search', 'Google Search'),
            ('referral', 'Referral'),
            ('social_media', 'Social Media'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )