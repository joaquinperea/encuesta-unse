"""Models for the encuesta app."""

from django.db import models


class Survey(models.Model):
    """Survey model. Each survey can have multiple questions."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Question model. Each survey can have multiple questions."""
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    order = models.IntegerField(unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class for the Question model."""
        ordering = ['order']

    def __str__(self):
        return f"Question: {self.text}"

    def save(self, *args, **kwargs):
        """Aseguramos que el orden se actualice correctamente al mover una pregunta."""
        if self.order is None:
            # Asignar el orden más alto disponible para preguntas nuevas
            self.order = Question.objects.filter(survey=self.survey).count() + 1
        super().save(*args, **kwargs)


class Answer(models.Model):
    """Answer model. For each question, there can be multiple answers."""
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer: {self.text}"
