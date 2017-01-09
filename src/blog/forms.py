from logging import getLogger

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm, RegexField
from django.template import loader

from blog.models import Contact

logger = getLogger("blog")


class ContactForm(ModelForm):
    mobile = RegexField(regex=r'^\+?1?\d{9,15}$',
                        error_message=(
                            "Phone number must be entered in the format: '+919999999999'. Up to 15 digits allowed."))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Div('name', css_class='form-group col-xs-12 floating-label-form-group controls'),
            Div('email', css_class='form-group col-xs-12 floating-label-form-group controls'),
            Div('mobile', css_class='form-group col-xs-12 floating-label-form-group controls'),
            Div('message', css_class='form-group col-xs-12 floating-label-form-group controls'),
            FormActions(Submit("send", "Send", css_class="btn btn-primary"))
        )
        self.fields["name"].widget.attrs["placeholder"] = u"Name"
        self.fields["email"].widget.attrs["placeholder"] = u"Email Address"
        self.fields["mobile"].widget.attrs["placeholder"] = u"Mobile Number"
        self.fields["message"].widget.attrs["placeholder"] = u"Message"

    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile', 'message']

    def send_email(self):
        email_to = settings.EMAIL_TO
        template1 = loader.get_template("email/contact.html")
        template2 = loader.get_template("email/contact-success.html")
        html_message1 = template1.render({
            "name": self.cleaned_data["name"].title(),
            "email": self.cleaned_data["email"],
            "phone": self.cleaned_data["mobile"],
            "message": self.cleaned_data["message"]
        })
        html_message2 = template2.render({
            "name": self.cleaned_data["name"].title()
        })
        try:
            send_mail("Contact Notification",
                      "",
                      settings.EMAIL_FROM,
                      [email_to],
                      fail_silently=False,
                      html_message=html_message1)
            logger.info("An email was sent to [{}]".format(email_to))
            send_mail("Thank you",
                      "",
                      settings.EMAIL_FROM,
                      [self.cleaned_data["email"]],
                      fail_silently=False,
                      html_message=html_message2)
            logger.info("An email was sent to [{}]".format(self.cleaned_data["email"]))
        except Exception as e:
            logger.error("Error occurred while sending mail, [{}]".format(e))
