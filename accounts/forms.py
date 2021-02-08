from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column
from django.contrib.auth import get_user_model
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Task
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