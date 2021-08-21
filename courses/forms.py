from django import forms
from django.contrib.contenttypes import fields
from django.forms import widgets
from django.forms.models import inlineformset_factory
from courses.models import Course, Module

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('subject', 'title', 'slug', 'overview', )

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Course Title*'
        self.fields['slug'].widget.attrs['placeholder'] = 'Course Slug*'
        self.fields['overview'].widget.attrs['placeholder'] = 'Course Overview*'
   

ModuleFormSet = inlineformset_factory(Course, Module, fields=['title', 'description'],
                                      extra=2, can_delete=True
                                      )
