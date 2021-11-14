from typing import Text
from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.


class Note(models.Model):
    user = CharField(max_length=50)
    title = CharField(max_length=50)
    note = TextField()


    def __str__(self):
        return self.user