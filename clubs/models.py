from django.db import models


class Club(models.Model):
    club_name = models.CharField(max_length=255)
    club_desc = models.TextField(max_length=600)
    youtube_channel = models.CharField(max_length=300)
    website = models.CharField(max_length=300)
    facebook = models.CharField(max_length=400)
    instagram = models.CharField(max_length=300)


class Events(models.Model):
    event = models.ForeignKey(Club, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    yt_link = models.CharField(max_length=255)


class Members(models.Model):
    member = models.ForeignKey(Club, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=255)
