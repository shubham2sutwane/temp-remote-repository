from django.db import models


class ContactData(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    salary=models.IntegerField()
    email=models.EmailField(max_length=100)


class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateTimeField(max_length=100)
    feedback = models.TextField(max_length=500)