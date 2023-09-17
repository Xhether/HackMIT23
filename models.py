from django.db import models

# Create your models here.


class Question(models.Model):
    questionText = models.CharField(max_length=200)


class Profile(models.Model):
    learningStyle = models.CharField(max_length=200)
    interests = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
