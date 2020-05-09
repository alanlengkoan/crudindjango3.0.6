from django.db import models

# Create your models here.
class Tampil(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(null=True)

    def __str__(self):
        return "{}".format(self.title)
