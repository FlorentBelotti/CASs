from .models import Session, Exercise, Serie
from rest_framework import serializers

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

class BaseSerializer(serializers.ModelSerializer):
    
    def __init_subclass__(base, *, model=None, fields=None, **kwargs):
        if model is not None and fields is not None:
            base.Meta = type('Meta', (), {'model': model, 'fields': fields})

class SerieSerializer(BaseSerializer, model=Serie, fields=('id', 'repetitions', 'weight', 'break_time', 'comment')):
    pass

class ExerciseSerializer(BaseSerializer, model=Exercise, fields=('id', 'name', 'duration', 'start', 'end', 'series')):
    series = SerieSerializer(many=True, read_only=True)

class SessionSerializer(BaseSerializer, model=Session, fields=('id', 'name', 'date', 'duration', 'start', 'end', 'exercises')):
    exercises = ExerciseSerializer(many=True, read_only=True)