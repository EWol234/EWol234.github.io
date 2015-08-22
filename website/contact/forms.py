from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import FormActions, PrependedText, InlineCheckboxes

class EmailForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=1000)
    message = forms.CharField(widget=forms.Textarea)
    cc = forms.BooleanField(required=False, label='CC Yourself?')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_action = '/contact/'
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('sender', css_class='form-control', placeholder='example@exapmle.com'),
        Field('subject', css_class='form-control'),
        Field('message', css_class='form-control', rows=10),
        # Field('cc', css_class='form-control checkbox-primary'),
        PrependedText('cc', ''),
        FormActions(Submit('submit', 'Send', css_class='btn-primary'))
    )
