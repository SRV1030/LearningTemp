from django import forms
from learnapp.models import info,webs

class fm1(forms.ModelForm):

    class Meta():
        model = info
        fields = '__all__'

class fm2(forms.ModelForm):

    class Meta():
        model = webs
        fields = '__all__'
