from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


GAME_CHOICES = [('Rock', 'Rock'), ('Paper', 'Paper'), ('Scissors', 'Scissors')]


class GameChoice(forms.Form):
    player_choice = forms.ChoiceField(choices=GAME_CHOICES, widget=forms.RadioSelect)
