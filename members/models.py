from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    join_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name