from django.db import models

"""
# Project CASs - Data Model Management Guide

## Adding Fields to Existing Tables
---------------------------------
1. Add the field definition in the appropriate model class in `models.py`
2. Update the corresponding serializer's `fields` tuple to include your new field in `serializers.py`

OPTIONNAL. For relationship fields (ForeignKey, ManyToMany, etc.):
   - Ensure the `related_name` attribute is properly defined in the model
   - Create a nested serializer field with the same name as the `related_name`
   - Use the appropriate serializer for the related model with `many=True` for collections

## Creating New Tables
-------------------
1. Define the new model class in `models.py` with all required fields
2. Create a new serializer class in `serializers.py` that inherits from `BaseSerializer`, each desired fields are detailed in the parameters of the class.

OPTIONNAL. For relationship between table, like foreign key :
    - Ensure that the serializer of the table that contains the key is define before the serializer of the table pointed at by the foreign key.

"""

class Session(models.Model):
    '''
    A training session that contains multiples exercises.
    '''

    # Details
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    # Timestamp
    duration = models.DurationField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%Y-%m-%d')}"

class Exercise(models.Model):
    '''
    An exercise, that contains multiples series.
    '''

    # Foreign key to session
    relative_session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="exercises")

    # Details
    name = models.CharField(max_length=100)

    # Timestamp
    duration = models.DurationField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} from session {self.relative_session.name}"

class Serie(models.Model):
    '''
    A serie of one exercise, containing details about the serie.
    '''

    # Foreign key to exercise
    relative_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="series")
    
    # Details
    repetitions = models.PositiveIntegerField()
    weight = models.FloatField(null=True, blank=True)
    break_time = models.PositiveIntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.repetitions} reps @ {self.weight} kg for {self.relative_exercise.name}"