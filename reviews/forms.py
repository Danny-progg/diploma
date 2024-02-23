from django import forms

from reviews.models import Version
from reviews.models import Review


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ReviewForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('name', 'title', 'review')
        # exclude = ('date_start',)


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        # fields = '__all__'
        fields = ('review', 'version_name', 'version_sign', 'version_number',)
        # exclude = ('date_start',)
