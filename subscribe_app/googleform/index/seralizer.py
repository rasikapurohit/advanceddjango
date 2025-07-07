from rest_framework import serializers
from .models import (Form, Question, Choice, Answer, Response)

class FormSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'creator_id']

class QuestionSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


class ChoiceSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


class AnswerSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


class ResponseSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        exclude = ['created_at', 'updated_at']

