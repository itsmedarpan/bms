from django.forms import ModelForm
from .models import Request, Donate

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

class DonateForm(ModelForm):
    class Meta:
        model = Donate
        fields = '__all__'