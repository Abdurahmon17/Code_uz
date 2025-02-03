from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    def __str__(self):
        return self.title


