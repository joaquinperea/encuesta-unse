"""Forms for the encuesta app."""

from django import forms
from .models import Survey, Question
from .services import insert_question_at


class InsertQuestionForm(forms.Form):
    """Form to insert a question in a survey at a specific position."""
    survey = forms.ModelChoiceField(queryset=Survey.objects.all(), required=True)
    new_question_text = forms.CharField(max_length=255, required=True, label="Texto de la pregunta")
    position = forms.IntegerField(min_value=1, required=True, label="Posición")

    def save(self):
        """Insert a question at a specific position in a survey."""
        survey = self.cleaned_data['survey']
        new_question_text = self.cleaned_data['new_question_text']
        position = self.cleaned_data['position']

        new_question = Question.objects.create(text=new_question_text)

        insert_question_at(survey.id, new_question, position)
