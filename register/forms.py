from django import forms
from captcha.fields import CaptchaField

class Registerform(forms.Form):

    check=CaptchaField(label='Check if you are a robot')

class UserInforform(forms.Form):
    manorwoman = (('male', 'male'), ('female', 'female'))

    gender=forms.ChoiceField(label='sex',choices=manorwoman)
    check=CaptchaField(label='Check if you are a robot')
