from django import forms
from django.contrib.contenttypes import fields
from django.forms import widgets
from courses.models import Course, Subject

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('subject', 'title', 'slug', 'overview', )

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Course Title*'
        self.fields['slug'].widget.attrs['placeholder'] = 'Course Slug*'
        self.fields['overview'].widget.attrs['placeholder'] = 'Course Overview*'
   