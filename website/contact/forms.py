from django import forms

class EmailForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(max_length=1000)
    message = forms.CharField(widget=forms.Textarea)
    cc = forms.BooleanField(required=False)
