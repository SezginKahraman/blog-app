from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to="blogs"
    )  # fileField, can allow to upload different types of files than image
    is_active = models.BooleanField(default=True)
    is_homepage = models.BooleanField(default=False)
    description = RichTextField()
    slug = models.SlugField(
        null=False, blank=True, unique=True, db_index=True, editable=False
    )  # blank = True means that in the admin panel can be empty

    def __str__(self):  # admin panelinde gösterilen ismi de belirler
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)  # call the base save.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        null=False, blank=True, unique=True, db_index=True, editable=False
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)  # call the base save.
