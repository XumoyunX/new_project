from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['name', 'phone', 'email', 'image', 'password']

    def save(self, commit=True):
        user = User(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email']
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            user_profile = super().save(commit=False)
            user_profile.user = user
            if commit:
                user_profile.save()
        return user_profile