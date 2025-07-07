from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import QUESTION_CHOICES
from .utils.util import generate_token

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Choice(BaseModel):
    label = models.CharField(max_length=200)  # renamed from 'choice' to avoid conflict

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'
        db_table = 'choice'

class Question(BaseModel):
    text = models.CharField(max_length=100) 
    question_type = models.CharField(max_length=100, choices=QUESTION_CHOICES, default='text')
    required = models.BooleanField(default=False)
    choices = models.ManyToManyField('Choice', related_name='questions', blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        db_table = 'question'

class Form(BaseModel):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_forms')
    background_color = models.CharField(max_length=20, default="#496188")
    collect_email = models.BooleanField(default=False)
    questions = models.ManyToManyField('Question', related_name='forms', blank=True)

    def create_blank_form(user):
        form_token = generate_token()
        choices = Choice.objects.create(label='Option 1')
        question = Question.objects.create(
            text='Sample Question',
            question_type='multiple choice',
            required=True
        )
        question.choices.add(choices)
        form = Form(
            code=form_token,
            title='Sample Form',
            creator=user,
            background_color='#496188',
            collect_email=True
        )
        form.save()
        form.questions.add(question)
        return form

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'
        db_table = 'form'

class Answer(BaseModel):
    answer = models.CharField(max_length=200, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    response = models.ForeignKey('Response', on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField(blank=True, null=True)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='selected_answers', null=True, blank=True)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answer'

class Response(BaseModel):
    response_code = models.CharField(max_length=100, unique=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='responses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    responder_ip = models.GenericIPAddressField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = 'Response'
        verbose_name_plural = 'Responses'
        db_table = 'response'

