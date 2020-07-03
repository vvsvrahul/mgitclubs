from django import forms
from django.forms import ModelForm
from website.models import *
from django.contrib.auth.models import User

# class BlogForm(forms.ModelForm):
#     class Meta():
#         model = 'BlogContent'
#         fields = ('Title','content')


class authenticateform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields =('username','email','password')

class BlogContent1Form(forms.ModelForm):
    class Meta():
        model = BlogContent11
        fields = ('title','story')


class CommentForms(forms.ModelForm):
    class Meta():
        model = CommentUser
        fields = ('comment',)


class MgitForms(forms.ModelForm):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta():
        model = Mgituser
        fields = ('Roll_number',)
