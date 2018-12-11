from django.db import models

# Create your models here.
class Books(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    detail = models.TextField()

    def shortSum(self):
        return self.detail[:100]+"..."

    def __str__(self):
        return self.title
