
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email

from .models import Tache

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'description', 'responsable', 'statut']



class SignUpForm(UserCreationForm):
    username = forms.CharField(
                    max_length=30,
                    required=True,
                    label="Nom d'utilisateur",
                    help_text="Moins de 30 caractères, sans caractères spéciaux sauf '_'"
     )
    email =  forms.EmailField(
                    max_length=255,
                    required=True,
                    label="Adresse",
                     help_text="Adresse mail valide"
    )
    password1 = forms.CharField(
                    label="Mot de passe",
                    strip=False,
                     widget=forms.PasswordInput,
                    help_text="Au moins 8 caractères, avec au moins un chiffre, et caractère spécial"
    )
    password2 = forms.CharField(
                    label="Confirmez le mot de passe",
                    widget=forms.PasswordInput,
                    strip=False,
                    help_text="Entrez à nouveau votre mot de passe"
    )
    is_chef_projet = forms.BooleanField(
                    required=False,
                    label="Devenir Chef de Projet",
                    help_text="Cochez si vous souhaitez être Chef de Projet."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_chef_projet']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        check1 = checkPW(password1)
        if(check1 != ""):
            raise forms.ValidationError(check1)
        check2 = checkPW_Confirm(password1, password2)
        if(check2 != ""):
            raise forms.ValidationError(check2)

        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')

        check = checkName(username)
        if(check != ""):
            raise forms.ValidationError(check)

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        checkDuplicate = checkMail(email)
        if(checkDuplicate != ""):
            raise forms.ValidationError(checkDuplicate)


        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError("Adresse email invalide.")

        return email



def checkName(username):
    if User.objects.filter(username=username).exists():
        return("Ce nom d'utilisateur est déjà pris.")

    if username[0].isdigit():
        return("Le nom d'utilisateur ne peut pas commencer par un chiffre.")
    return ""

def checkMail(email):
    if User.objects.filter(email=email).exists():
        return "Cette adresse email est déjà utilisée."
    return ""


def checkPW(password):
    if len(password) < 8:
        return("Le mot de passe doit contenir au moins 8 caractères.")
    return ""


def checkPW_Confirm(password1,password2):
    if password1 and password2 and password1 != password2:
        return("Les mots de passe ne correspondent pas.")
    return ""
