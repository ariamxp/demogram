#Django
from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'input'})
    )

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirm = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self): #Las validaciones de campos se hacen en funciones con clean_NOMBRECAMPO
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirm = data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirm') #pop saca los datos que no debemos enviar a la bd

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control', 'placeholder': self.snake_to_word(f)})

    @staticmethod
    def snake_to_word(word):
        """ Change snake case to word """
        return ' '.join(x.capitalize() or'_'for x in word.split('_'))

class ProfileForm(forms.Form):

    website = forms.URLField(max_length = 200, required = True)
    biograpgy = forms.CharField(max_length = 500, required = False)
    phone_number = forms.CharField(max_length = 30, required = False)
    picture = forms.ImageField()
