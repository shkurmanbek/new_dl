from django.db import models

# Create your models here.
class Research(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    models.User
    def __str__(self):
        return self.title
