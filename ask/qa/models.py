from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):                                                   
    objects = QuestionManager() 
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='question_like_user', blank=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    objects = models.Manager()
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
