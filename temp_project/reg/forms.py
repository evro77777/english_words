from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=' Логин', widget=forms.TextInput(attrs={'class': 'input100'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input100'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input100'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AuthenticationUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input100'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input100'}))


class HomeForm(forms.Form):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self.CHOICES = ((self.obj['answer_options'][0], self.obj['answer_options'][0]),
                   (self.obj['answer_options'][1], self.obj['answer_options'][1]),
                   (self.obj['answer_options'][2], self.obj['answer_options'][2]),
                   (self.obj['answer_options'][3], self.obj['answer_options'][3]))
        self.english_word = self.obj['english_word']
        self.right_answer = self.obj['right_answer']
        self.choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=self.CHOICES)
        self.fields['choice_field'] = self.choice_field



