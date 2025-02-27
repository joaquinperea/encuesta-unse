"""Administration panel."""

from django.contrib import admin
from .models import Survey, Question, Answer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """Survey admin."""
    list_display = ('name', 'description', 'created_at', 'updated_at')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question admin."""
    list_display = ('text', 'survey', 'order')
    list_filter = ('survey',)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Answer admin."""
    list_display = ('text', 'question')
