import django_filters
from django_filters import ModelChoiceFilter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Task, Client, ClientCategory, Fund, Analyst, FundCategory


class ClientFilter(django_filters.FilterSet):
    name = ModelChoiceFilter(queryset=Client.objects.all())
    category = ModelChoiceFilter(queryset=ClientCategory.objects.all())
    class Meta:
        model = Client
        fields = ['name', 'category', ]
        exclude = []

class FundFilter(django_filters.FilterSet):
    name = ModelChoiceFilter(queryset=Fund.objects.all())
    category = ModelChoiceFilter(queryset=FundCategory.objects.all())
    class Meta:
        model = Fund
        fields = ['name', 'category', 'client']
        exclude = []

class TaskFilter(django_filters.FilterSet):
    # def __init__(self, *args, **kwargs):
    #         super(TaskFilter,self).__init__(*args, **kwargs)
    #         self.helper = FormHelper()
    #         self.helper.layout = Layout(
    #             Row(
    #                 Column('fund', css_class='form-group col-md-2 mb-0'),
    #                 Column('client', css_class='form-group col-md-2 mb-0'),
    #                 Column('reporter', css_class='form-group col-md-2 mb-0'),
    #                 css_class='form-row'
    #             ),

    #         )
    assignee = ModelChoiceFilter(queryset=Analyst.objects.all())
    client = ModelChoiceFilter(queryset=Client.objects.all())
    # fund = ModelChoiceFilter(queryset= Fund.objects.filter(client=client))
    reporter = ModelChoiceFilter(queryset=Analyst.objects.all())
    class Meta:
        model = Task
        fields = ['client', 'fund', 'assignee', 'reporter', ]
        exclude = []