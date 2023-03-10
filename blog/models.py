from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
import datetime
import uuid
from django.db import models
from django.utils import timezone

def upload_location(instance, filename, *args, **kwargs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
    )
    return file_path

class BlogPost(models.Model):
    title = models.CharField(null=False, max_length=50, blank=False)
    body = models.TextField(null=False, max_length=5000, blank=False)
    image = models.ImageField(upload_to=upload_location, null=False, max_length=5000, blank=False)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, default=uuid.uuid1)
    visits = models.IntegerField(default=0)
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + '-' + instance.title)

pre_save.connect(pre_save_blog_post_reciever, sender=BlogPost)
