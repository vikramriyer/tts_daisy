from django.db import models

# Create your models here.
class Upload(models.Model):

    text_id = models.AutoField(primary_key=True)
    text_data = models.TextField()

    def __str__(self):
        return self.text_data
