"""Services for the survey app"""

from .models import Survey, Question


def insert_question_at(survey_id, new_question, position):
    """Insert a question at a specific position in a survey."""
    survey = Survey.objects.get(id=survey_id)
    questions = Question.objects.filter(survey=survey).order_by('order')

    for question in questions.filter(order__gte=position):
        question.order += 1
        question.save()

    new_question.survey = survey
    new_question.order = position
    new_question.save()
