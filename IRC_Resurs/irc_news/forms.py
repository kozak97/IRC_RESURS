from django import forms
from django.contrib.auth.forms import AuthenticationForm
from unidecode import unidecode

from .models import *



class addPostForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model=News
        fields = ['title', 'slug', 'content', 'photo','is_published', 'categorie', 'file','link', 'author']
        widgets={
            'title': forms.TextInput(attrs={'class':'input_text'}),
            'slug': forms.TextInput(attrs={'class':'input_text'}),
            'content':forms.Textarea(attrs={'cols':60, 'rows':10, 'class':'title_text-news'}),
            'photo':forms.FileInput(attrs={'class':'file_news'}),
            'file':forms.FileInput(attrs={'class':'file_news'}),
            'link': forms.URLInput(attrs={'class':'input_text'}),
            'categorie': forms.Select(attrs={'class': 'select_categorie'}),
            'author': forms.Select(attrs={'class': 'select_categorie'})
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not self.cleaned_data['slug']:
            slug_text = unidecode(self.cleaned_data['title'])
            instance.slug = slugify(slug_text)
        if commit:
            instance.save()
        return instance




class PicturesForm(forms.ModelForm):

    class Meta:
        model = Pictures
        fields = ['pictures', 'news']

        widgets = {
            'news': forms.Select(attrs={'class': 'select_categorie'}),
            'pictures': forms.FileInput(attrs={'class': 'file_news', 'multiple': 'multiple'}),
        }

class ComentForm(forms.ModelForm):
    class Meta:
        model=Comentari
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class':'coment__name', 'placeholder': "Ваше імя:"}),
            'content': forms.Textarea(attrs={'cols':60, 'rows':10, 'class':'coment__text', 'placeholder': "Коментар:"}),
        }


class ProIrcForm(forms.ModelForm):
    class Meta:
        model=ProIrc
        fields = ['title', 'content','photo','link','contact','email']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_text'}),
            'content':forms.Textarea(attrs={'cols':60, 'rows':10, 'class':'title_text-news'}),
            'photo': forms.FileInput(attrs={'class':'file_news'}),
            'link': forms.URLInput(attrs={'class':'input_text'}),
            'contact':forms.TextInput(attrs={'class': 'input_text'}),
            'email': forms.EmailInput(attrs={'class': 'input_text'}),
        }
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'input_text'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input_text'}))

class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input_text'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input_text'}))


class RegistrationFormFull(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'pobatkovi', 'birth_day', 'posada', 'info','photo', 'user']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input_text'}),
            'last_name': forms.TextInput(attrs={'class': 'input_text'}),
            'pobatkovi': forms.TextInput(attrs={'class': 'input_text'}),
            'birth_day': forms.TextInput(attrs={'class': 'input_text'}),
            'posada': forms.TextInput(attrs={'class': 'input_text'}),
            'info': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'title_text-news'}),
            'photo': forms.FileInput(attrs={'class': 'file_news'}),
            'user': forms.Select(attrs={'class': 'select_categorie'})
        }




