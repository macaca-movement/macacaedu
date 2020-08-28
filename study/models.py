from django.db import models


class StudyMedia(models.Model):
    name = models.CharField(max_length=140)
    video = models.FileField(upload_to='study-media/')
    description = models.TextField(max_length=900)

    def __str__(self):
        return self.name


class ActivityItem(models.Model):
    name = models.CharField(max_length=140)
    medias = models.ManyToManyField('StudyMedia')

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=140)
    instructions = models.TextField(max_length=3000)
    items = models.ManyToManyField('ActivityItem')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"
