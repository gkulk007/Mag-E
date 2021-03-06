from django.db import models


class Club(models.Model):
    club_name = models.CharField(max_length=255, null=True, blank=True)
    club_desc = models.TextField(max_length=600, null=True, blank=True)
    club_logo = models.TextField(max_length=600, null=True, blank=True)
    youtube_channel = models.CharField(max_length=300, null=True, blank=True)
    website = models.CharField(max_length=300, null=True, blank=True)
    facebook = models.CharField(max_length=400, null=True, blank=True)
    instagram = models.CharField(max_length=300, null=True, blank=True)
    discord = models.CharField(max_length=300, null=True, blank=True)
    linkedin = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return self.club_name


class Events(models.Model):
    event_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=255, null=True, blank=True)
    event_bio = models.TextField(max_length=600, null=True, blank=True)
    register = models.TextField(max_length=600, null=True, blank=True)
    feedback = models.TextField(max_length=600, null=True, blank=True)
    event_date = models.DateTimeField(null=True, blank=True)
    yt_link = models.CharField(max_length=255, null=True, blank=True)
    recording = models.TextField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.event_title


class Members(models.Model):
    member = models.ForeignKey(Club, on_delete=models.CASCADE)
    member_name = models.CharField(max_length=255)

    def __str__(self):
        return self.member_name


class Wanna_Add(models.Model):
    activity_title = models.CharField(max_length=300, null=True, blank=True)
    activity_club = models.CharField(max_length=300, null=True, blank=True)
    activity_date = models.DateField(null=True, blank=True)
    activity_time = models.TimeField(null=True, blank=True)
    activity_details = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.activity_title
