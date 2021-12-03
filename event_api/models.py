from django.db import models
from django.utils.text import slugify


def upload_to(instance, filename):
    return f'posts/{filename}' 


class Event(models.Model):

    options = (
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField("Image", upload_to=upload_to, default='posts/default.jpg')
    categories = models.CharField(max_length=10, choices=options)
    published = models.BooleanField()
    paid = models.BooleanField()
    slug = models.SlugField(max_length=30, blank=True, editable=False)#



    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title   