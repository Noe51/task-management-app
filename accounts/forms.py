from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth import get_user_model

from .models import Task, Client, Fund
User = get_user_model()


from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields= '__all__'
        exclude = []

        widgets = {
                'title' : forms.TextInput(attrs={'class':"form-control", 'placeholder':"", 'aria-label':"Todo", 'aria-describedby':"add-btn" }),
                'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Décrivez la tâche'}),
                # 'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nom.prenom@gmail.com'}),
                # 'phone' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '06000000'}),
                # 'city' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paris'}),
                # 'department' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '75'}),
                # 'domain_of_knowledge' : forms.CheckboxSelectMultiple(),
                # 'speciality' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entreprise de BTP'}),
                # 'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dites en plus sur qui vous êtes ...'}),
                # 'company' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Superconsultant S.A.S'}),
            }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column('title', css_class='form-group col-md-6 mb-0'),
                    Column('description', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                'description',
                Row(
                    Column('domain_of_knowledge', css_class='form-group col-md-5 mb-0'),
                    Column('city', css_class='form-group col-md-5 mb-0'),
                    Column('department', css_class='form-group col-md-2 mb-0'),
                    css_class='form-row'
                ),
                Row(
                    Column('phone', css_class='form-group col-md-4 mb-0'),
                    Column('speciality', css_class='form-group col-md-4 mb-0'),
                    Column('company', css_class='form-group col-md-4 mb-0'),
                    css_class='form-row'
                ),
                Submit('submit', 'Rejoindre l&#39; espace membre '),
            ) 
class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields= '__all__'

class FundForm(forms.ModelForm):

    class Meta:
        model = Fund
        fields= '__all__'