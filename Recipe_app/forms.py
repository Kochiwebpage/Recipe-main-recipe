from django import forms
from .models import UserFeedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['name', 'email', 'feedback']