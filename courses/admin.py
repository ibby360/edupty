from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from courses.models import Course, Subject, Module

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    '''Admin View for Subject'''

    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created',]
    list_filter = ['subject', 'created',]
    search_fields = ['title', 'overview',]
    prepopulated_fields = {'slug': ('title', )}
    inlines = [ModuleInline]
