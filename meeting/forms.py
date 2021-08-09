from django import forms
from .models import Agenda, Member
import bootstrap_datepicker_plus as datetimepicker  #追加


class CreateAgendaForm(forms.ModelForm):

    class Meta:
        model = Agenda
        fields = ['title', 'contents', 'date', 'members']
        widgets = {
            'contents': forms.Textarea(attrs={'rows':4, 'cols':35}),
            #ここから下を追加
            'date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            #ここまでを追加
        }

    members = forms.ModelMultipleChoiceField(
        queryset=Member.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
