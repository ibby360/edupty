from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models.fields import PositiveIntegerField

# Create your models here.

class Subject(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.title

class Course(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_created')
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField (max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

class Module(models.Model):

    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = ("module")
        verbose_name_plural = ("modules")

    def __str__(self):
        return self.title


class Content(models.Model):
    """ 
    Module contains multiple contents, ForeignKey field is defined to point
    to the Module nodel. And generic relation to assocciate objects 
    from different models that present different types of content
    """

    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': (
                                         'text', 'file', 'image', 'video')}
                                     )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class BaseItem(models.Model):

    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField( auto_now_add=True)

    class Meta:
       abstract = True

    def __str__(self):
        return self.title

class Text(BaseItem):
    content = models.TextField()


class File(BaseItem):
    file = models.FileField(upload_to='files')


class Image(BaseItem):
    file = models.FileField(upload_to='images')


class Video(BaseItem):
    url = models.URLField()
