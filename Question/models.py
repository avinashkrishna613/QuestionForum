from django.db import models

from user.models import profile
from simple_history.models import HistoricalRecords

class Ques(models.Model):
    
    name = models.CharField("person's name", max_length=20, null = False)
    ques = models.CharField(max_length = 150)
    # history = HistoricalRecords()

    @classmethod
    def create(self, n, q):
        self.name = n
        self.ques = q
    class Meta:
        ordering = ['pk']

# # class Ans(models.Model):

class Ans(models.Model):
    ques_id = models.ForeignKey(Ques, on_delete = 'CASCADE')
    
    ans = models.CharField(max_length = 1000)
    by = models.CharField(max_length = 20)
    # history = HistoricalRecords()





    