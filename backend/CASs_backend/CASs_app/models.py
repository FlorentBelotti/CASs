from django.db import models

# Create your models here.

class Session(models.Model):
    '''
    A training session.

    Fields :
    - Ses_date : Automaticly generated date and hour of the session.
    - Ses_name : type of session (pull, push, leg etc.)
    '''

    Ses_date = models.DateTimeField(auto_now_add=True)
    Ses_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Ses_name} - {self.Ses_date.strftime('%Y-%m-%d')}"

class Exercise(models.Model):
    '''
    An exercise, part of a training session.

    Fields :
    - (FK) Ex_session : Relative session.
    - Ex_name : Name of the exercise.
    '''

    Ex_session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="Ex")
    Ex_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Ex_name

class Serie(models.Model):
    '''
    Serie of exercise.

    Fields :
    - (FK) Ser_exercise : Relative exercise.
    - repetitions : Number of repetitions.
    - weight : Used weight for the repetition.
    - break : duration of the break.
    - Comment : about the serie.
    '''

    Ser_exercise = models.ForeignKey(Exercice, on_delete=models.CASCADE, related_name="series")
    Ser_repetitions = models.PositiveIntegerField()
    Ser_weight = models.FloatField(null=True, blank=True)
    Ser_breaktime = models.PositiveIntegerField(null=True, blank=True)
    Ser_comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.Ser_repetitions} reps @ {self.Ser_weight} kg"