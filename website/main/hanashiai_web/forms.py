from django import forms
from .models import  Comments, Post,  User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('image', 'title', 'author', 'date', 'body' )

        widgets = {

            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control', 'calue':'', 'id':'author', 'type':'hidden'}),
            #'author':forms.Select(attrs={'class': 'form-control'}),
            'date':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }



class Comments(forms.ModelForm):
    class Meta:
        model = Comments 
        fields = ( 'author','date', 'body' )

        widgets = {

            'date':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'comments', 'type':'hidden'}),
            

        }

##class RegisterForm(forms.ModelForm):
#    password1 = forms.CharField(
#        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#        label='Password'
#    )
#    password2 = forms.CharField(
#        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
#        label='Password confirmation'
#    )
#
#    class Meta:
#        model = User 
#        fields = ('password1', 'password2','gender', 'age', 'email', 'profile_pic' )
#        
#
#        widgets = {
#
#            'title':forms.TextInput(attrs={'class': 'form-control'}),
#            'author':forms.TextInput(attrs={'class': 'form-control', 'calue':'', 'id':'author', 'type':'hidden'}),
#            #'author':forms.Select(attrs={'class': 'form-control'}),
#            'date':forms.TextInput(attrs={'class': 'form-control'}),
#            'body':forms.Textarea(attrs={'class': 'form-control'}),
#        }




