from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
import itertools

STATUS_CHOICES = (
        ('PRO', 'Proposed'),
        ('ACC', 'Accepted'),
        ('RES', 'Resolved'),
        ('CLO', 'Senior'),
    )


class Task(models):
    task_id = models.AutoField(primary_key=True)
    task_description = models.TextField
    task_status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PRO',)
    task_assignee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task')


class Story(models.Model):
    story_id = models.AutoField(primary_key=True)
    story_name = models.CharField(max_length=27, unique=True)
    story_description = models.TextField
    story_assignee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task')
    story_priority = models.IntegerField(max_length=3, validators=[MaxValueValidator(100), MinValueValidator(0)])
    story_size = models.IntegerField(max_length=2, validators=[MaxValueValidator(22), MinValueValidator(0)])
    story_task = models.ForeignKey(Task, related_name='story', on_delete=models.CASCADE)
    story_acceptance_criteria = models.TextField
    story_status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PRO',)



class Backlog(models.Model):
    backlog_id = models.AutoField(primary_key=True)
    backlog_creation_date = models.DateField(auto_now_add=True)
    backlog_stories = models.ForeignKey(Story, related_name='backlog', on_delete=models.CASCADE)

class Epic(models.Model):
    epic_id = models.AutoField(primary_key=True)
    epic_name = models.CharField(max_length=27, unique=True)
    epic_priority = models.IntegerField(max_length=3, validators=[MaxValueValidator(100), MinValueValidator(0)])
    epic_backlog = models.OneToOneField(related_name='epic', on_delete=models.CASCADE)


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=27, unique=True)


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=75, unique=True)
    project_creation_date = models.DateField(auto_now_add=True, editable=False)
    project_code_repo = models.CharField(max_length=75, unique=True)
    project_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='project')
    project_team = models.ForeignKey(Team, related_name='team', on_delete=models.CASCADE)
    project_epic = models.ForeignKey(Epic, related_name='epic', on_delete=models.CASCADE)














