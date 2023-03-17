from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *



class blogPostModel(models.Model):
    title = models.CharField(max_length=500)
    description = FroalaField(max_length=2000)
    slug = models.SlugField(max_length=1000, null=True, blank=True,)
    image = models.ImageField(upload_to='blogPost')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(blogPostModel, self).save(*args, **kwargs)


