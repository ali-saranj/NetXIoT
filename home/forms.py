from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    interests = forms.CharField(max_length=255, required=True)  # اطمینان از وجود این خط
    message = forms.CharField(widget=forms.Textarea, required=True)
