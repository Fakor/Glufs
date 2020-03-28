from django import forms

from main.models.dinner import Dinner
from main.models.label import Label


class EditMealForm(forms.ModelForm):
    class Meta:
        model = Dinner
        fields = ['name']

    def update_meal(self, meal):
        updated_meal = self.save(commit=False)
        meal.name = updated_meal.name
        meal.save()


class LabelPickerForm(forms.Form):

    def __init__(self, *args, **kwargs):
        labels = kwargs.pop('labels', None)
        super(LabelPickerForm, self).__init__(*args, **kwargs)
        for l in Label.objects.all():
            if labels:
                default=l in labels.all()
            else:
                default=False
            self.fields[l.text] = forms.BooleanField(required=False)
            self.fields[l.text].initial = default
            self.fields[l.text].label = l

    def update_meal_with_labels(self, meal):
        meal.labels.clear()
        for key, label in self.fields.items():
            if self.cleaned_data[key]:
                try:
                    meal.add_label(Label.objects.filter(text=key)[0])
                except:
                    pass


