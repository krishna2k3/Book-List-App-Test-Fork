from django.db import models
from django.utils.text import slugify

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    publication_date = models.DateField()
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    cover_page = models.ImageField(upload_to='cover_page', null=True, blank='True')
    pdf = models.FileField(upload_to='books')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title