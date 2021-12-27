from django import forms
from .models import STO, Action, Group


class STOForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(STOForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = STO
        fields = ['date', 'mileage', 'group', 'actions', 'price']
        labels = {
            'mileage': 'Текущий пробег:',
            'group': 'Тип ТО:',
            'price': 'Цена:',
            'actions': 'Спецификация:'
        }
    date = forms.DateField(widget=forms.SelectDateWidget(years=[2018, 2019, 2020, 2021]))
    mileage = forms.IntegerField()
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    price = forms.IntegerField()
    actions = forms.ModelMultipleChoiceField(
        queryset=Action.objects.all(),
        widget=forms.SelectMultiple
    )
