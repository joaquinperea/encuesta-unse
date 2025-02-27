"""Serializers for the models of the encuesta app."""

from rest_framework import serializers
from .models import Survey, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    """It will be used to serialize the answers of a question."""
    class Meta:
        """Meta class for the AnswerSerializer."""
        model = Answer
        fields = ['id', 'question', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    """It will be used to serialize the questions of a survey."""
    answers = AnswerSerializer(many=True)

    class Meta:
        """Meta class for the QuestionSerializer."""
        model = Question
        fields = ['id', 'survey', 'text', 'order', 'answers']


class SurveySerializer(serializers.ModelSerializer):
    """It will be used to serialize the surveys."""
    questions = QuestionSerializer(many=True)

    class Meta:
        """Meta class for the SurveySerializer."""
        model = Survey
        fields = ['id', 'name', 'description', 'questions']
