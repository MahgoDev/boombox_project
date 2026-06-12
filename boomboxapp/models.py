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
