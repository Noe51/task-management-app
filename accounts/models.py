from django.db import models
from django.utils import timezone
from django.conf import settings
import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ClientCategory(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)

class Client(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    category = models.ForeignKey(ClientCategory, on_delete=models.PROTECT, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def getfunds(self):
        funds = Fund.objects.get(client=self)
        return funds
    
    def __str__(self):
        return str(self.name)

class FundCategory(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return str(self.name)

class Fund(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    category = models.ForeignKey(FundCategory, on_delete=models.PROTECT, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.name)

class Analyst(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    is_manager = models.BooleanField(default=False)
    max_workload = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def workload(self):
        workload = Task.objects.filter(assignee=self.pk).current_advancement
        return workload

    def freetime(self):
        workload = self.workload()
        freetime = self.max_workload - workload
        return freetime

    def __str__(self):
        return str(self.id)

class Task(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, blank=True, null=True)
    fund = models.ForeignKey(Fund, on_delete=models.PROTECT, blank=True, null=True)
    # description = models.TextField(max_length=1000, blank=True, null=True)
    periodicity = models.CharField(max_length=1000, blank=True, null=True)
    time_to_complete = models.FloatField()
    current_advancement = models.FloatField()
    assignee = models.ForeignKey(Analyst, blank=True, null=True, on_delete=models.PROTECT, related_name='%(class)s_tasks_assigned')
    reporter = models.ForeignKey(Analyst, blank=True, null=True, on_delete=models.PROTECT, related_name='%(class)s_tasks_reported')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def progress(self):
        progress = self.current_advancement / self.time_to_complete *100
        return progress

    def __str__(self):
        return str(self.id)
