from django.db import models

# Create your models here.
class DailySearchMetadata(models.Model):
    '''
    A model providing the number of searches for a given day.

    Parameters:
    ----------
    date : The day in question, relative to UTC
    number_of_searches : The number of searches in that day
    '''
    date = models.DateField()
    number_of_searches = models.PositiveIntegerField()

    def increment_searches(self):
        self.number_of_searches = self.number_of_searches + 1
