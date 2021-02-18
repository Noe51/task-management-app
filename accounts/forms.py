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
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column('title', css_class='form-group col-md-12 mb-2'),
                    css_class='form-row'
                ),
                Row(
                    Column('periodicity', css_class='form-group col-md-2 mb-2'),
                    Column('current_advancement', css_class='form-group col-md-2 mb-2'),
                    Column('time_to_complete', css_class='form-group col-md-2 mb-2'),
                    Column('fund', css_class='form-group col-md-2 mb-2'),
                    Column('client', css_class='form-group col-md-2 mb-2'),
                    Column('reporter', css_class='form-group col-md-2 mb-2'),
                    css_class='form-row'
                ),
                Submit('update', 'Create task', css_class='btn btn-block btn-sm btn-primary'),

            ) 


    class Meta:
        model = Task
        fields= '__all__'
        exclude = ['assignee']

        widgets = {
                'title' : forms.TextInput(attrs={'class':"form-control", 'placeholder':"enter the task" }),
                'fund' : forms.Select(attrs={'class': 'form-control'}),
                'client' : forms.Select(attrs={'class': 'form-control'}),
                'periodicity' : forms.TextInput(attrs={'class': 'form-control'}),
                'time_to_complete' : forms.TextInput(attrs={'class': 'form-control'}),
                'current_advancement' : forms.TextInput(attrs={'class': 'form-control'}),
                'assignee' : forms.Select(attrs={'class': 'form-control'}),
                'reporter' : forms.Select(attrs={'class': 'form-control'}),
            }

        
class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(

                Row(
                    Column('name', css_class='form-group col-md-6 mb-2'),
                    Column('category', css_class='form-group col-md-6 mb-2'),
                    css_class='form-row'
                ),
                Submit('update', 'Create client', css_class='btn btn-block btn-sm btn-primary'),

            ) 

    class Meta:
        model = Client
        fields= '__all__'

class FundForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(

                Row(
                    Column('name', css_class='form-group col-md-4 mb-2'),
                    Column('category', css_class='form-group col-md-4 mb-2'),
                    Column('client', css_class='form-group col-md-4 mb-2'),
                    css_class='form-row'
                ),
                Submit('update', 'Create fund', css_class='btn btn-block btn-sm btn-primary'),

            ) 

    class Meta:
        model = Fund
        fields= '__all__'