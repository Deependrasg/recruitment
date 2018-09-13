from django import forms
from .models import Candidate,Attempts

class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'date', 'college', 'degree', 'contact_no')

class CandidateRating(forms.ModelForm):

    class Meta:
        model = Attempts
        fields = ('candidate', 'question', 'ratings')