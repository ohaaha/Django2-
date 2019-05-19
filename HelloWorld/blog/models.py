from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10, default="title")
    content = models.TextField(null=True)
    public_date = models.DateField(default="2016-02-28")

    def __str__(self):
        return self.title