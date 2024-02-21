from django import forms

from main.models import Doctors


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DoctorForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Doctors
        # fields = '__all__'
        fields = ('name', 'description', 'price', 'image', 'category')
        # exclude = ('date_start',)
