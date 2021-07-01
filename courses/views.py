from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from courses.models import Course

# Create your views here.


class OwnerMixin(object):
    def get_queryset(self):
        qs = super() .get_queryset()
        return qs.filter(owner=self.requst.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super() .form_valid(form)


class OwnerCourseMixin(OwnerMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_cource_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = "courses/manage/form.html"


class ManageCourseListView(OwnerCourseMixin, ListView):
    template_name = "courses/manage/list.html"

class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass


class CourseCreateView(OwnerCourseEditMixin, UpdateView):
    pass



class CourseDeleteView(DeleteView):
    template_name = "courses/manage/delete.html"
