from django.db import models
from django.utils import timezone

# Create your models here.
class toDoItem(models.Model):
    textField = models.CharField(max_length=200)
    dateTimeField = models.DateTimeField(default=timezone.now())
    ##123
    def post(self):
        self.dateTimeField = timezone.now()
        self.save()

    def __str__(self):
        return self.textField
