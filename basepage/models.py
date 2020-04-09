from django.db import models

# Create your models here.

class description(models.Model):
    whoAmI = models.TextField()

    def __str__(self):
        return self.whoAmI
