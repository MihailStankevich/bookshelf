from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, default='author_avatar.png')
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.jpg')
    # authors = models.ForeignKey(Author, related_name='books', on_delete=models.SET_NULL, null=True)
    authors = models.ManyToManyField(Author, related_name='books')
    def __str__(self):
        return self.title
    
    # 