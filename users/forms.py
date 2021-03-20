from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        help_text='Никакого спама',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

class UserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Введите новый пароль',
        required=False,
        help_text='Придумай что нибудь сложненькое',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'минимум 8 символов'})
    )
    username = forms.CharField(
        label='Введите новый логин',
        required=False,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1']

class ProfileSlugForm(forms.ModelForm):
    slug = forms.SlugField(
        label='Придумай коротокое название',
        required=True,
        widget=forms.TextInput
    )

    long_link = forms.CharField(
        label='Вставь длинную ссылку',
        required=True,
    )

    title = forms.CharField(
        label='Придумай коротое описание',
        required=False,
        max_length=150,
        widget=forms.TextInput,
        )

    class Meta:
        model = Profile
        fields = ['title', 'long_link', 'slug']
