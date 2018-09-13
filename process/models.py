from django.db import models
from django.contrib.postgres.fields import JSONField
import json
from django.db.models import Sum, Avg, F, FloatField, Count

class Technology(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Questions(models.Model):

    class DIFFICULTY:
        EASY = 1
        MEDIUM = 2
        HARD = 3

    LEVEL = (
        (DIFFICULTY.EASY, 'Easy'),
        (DIFFICULTY.MEDIUM, 'Medium'),
        (DIFFICULTY.HARD, 'Hard'),
    )
    question = models.CharField(max_length=100)
    answer = models.TextField()
    difficulty = models.IntegerField(max_length=6, choices=LEVEL)
    technology = models.ForeignKey(Technology, related_name='technology')

    def __str__(self):
        return self.question

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=12)


    def __str__(self):
        return self.name

class Attempts(models.Model):
    candidate = models.ForeignKey(Candidate, related_name='attempt_candidate', on_delete=models.CASCADE,)
    question = models.ForeignKey(Questions, related_name='attempt_question', on_delete=models.CASCADE,)
    ratings = models.IntegerField()

    def __str__(self):
        return '{0} :: {1} :: {2}'.format(self.question, self.ratings, self.question.difficulty)

class Result(models.Model):
    candidate = models.OneToOneField(Candidate, related_name='result', on_delete=models.CASCADE,)
    total_ratting = models.FloatField()
    questions = JSONField(blank=True, null=True)

    def calculation(user):
        candidate = Candidate.objects.get(id=user)
        technology = Technology.objects.all()
        percentage = []
        ratings = []

        for tech in technology:
            total = Attempts.objects.filter(candidate=candidate, question__technology=tech.id).aggregate(total=Sum(F('ratings') * F('question__difficulty'), output_field=FloatField()))

            sud = Attempts.objects.filter(candidate=candidate, question__technology=tech.id).count()
            t = (total['total'],sud)

            ratings.append(total['total'])

            percentage.append({tech.name:t})

        total_ratings = sum(ratings)
        data= json.dumps(percentage)
        res = Result.objects.create(candidate=Candidate.objects.get(id=user),total_ratting=total_ratings, questions=data)

    def __str__(self):
        return str(self.candidate)