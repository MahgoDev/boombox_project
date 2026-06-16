from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField()
    docnumber = models.CharField(max_length=11)
    password = models.CharField()
    creation_date = models.DateField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['docnumber'], name='account_docnumber_unique')
        ]

class Album(models.Model):
    album_name = models.CharField()
    creation_date = models.DateField()
    release_date = models.DateField()

class Rating(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    rating = models.IntegerField()
    creation_date = models.DateField()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account', 'album'], name='rating_account_album_unique')
        ]
