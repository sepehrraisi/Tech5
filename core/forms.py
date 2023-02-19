from django import forms

from core.models import TeammateRequest, Activity, GymRequest, CoachRequest


class TeammateRequestForm(forms.ModelForm):
    activities = forms.ModelMultipleChoiceField(
        queryset=Activity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = TeammateRequest
        fields = ('gender', 'location', 'activities', 'user', 'description')
        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 4, 'cols': 15, 'placeholder': 'میزان مهارت خود در فعالیت های انتخاب شده را وارد کنید'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False


class GymRequestForm(forms.ModelForm):
    activities = forms.ModelMultipleChoiceField(
        queryset=Activity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = GymRequest
        fields = ('gender', 'location', 'activities', 'user', 'files', 'description')
        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 4, 'cols': 15, 'placeholder': 'جنسیت، رده سنی و زمان بندی هر فعالیت را وارد کنید.'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False


class CoachRequestForm(forms.ModelForm):
    activities = forms.ModelMultipleChoiceField(
        queryset=Activity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = CoachRequest
        fields = ('type_of_training', 'location', 'activities', 'user', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].required = False
