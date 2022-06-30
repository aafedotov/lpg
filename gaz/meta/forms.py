from django import forms
from .models import Memory


class MemoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MemoryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Memory
        fields = ['name', 'dob', 'dod', 'bio', 'portrait']
        labels = {
            'name': 'Фамилия Имя Отчество:',
            'dob': 'Дата рождения:',
            'dod': 'Дата смерти:',
            'bio': 'Краткая биография:',
            'portrait': 'Портрет'
        }

    name = forms.CharField(required=True)
    dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    dod = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    bio = forms.CharField(widget=forms.Textarea, required=False)
    portrait = forms.ImageField(required=False)
