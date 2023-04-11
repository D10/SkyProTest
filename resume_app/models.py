from django.db import models


class Resume(models.Model):
    status = models.CharField(max_length=64)
    grade = models.CharField(max_length=64)
    speciality = models.CharField(max_length=64)
    salary = models.FloatField()
    education = models.CharField(max_length=64)
    experience = models.TextField()
    portfolio = models.URLField()
    title = models.CharField(max_length=64)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
