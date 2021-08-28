from django.db.models.query_utils import check_rel_lookup_compatibility
from django.views.generic.base import TemplateResponseMixin, View
from courses.models import Course, Subject
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


class HomeView(TemplateResponseMixin, View):
    model = Course
    template_name = 'index.html'

    def get(self, request, subject=None):
        subjects = Subject.objects.annotate(total_courses=Count('courses'))
        courses = Course.objects.annotate(total_modules=Count('modules'))

        if subject:
            subject = get_object_or_404(Subject, slug=subject)
            courses = Course.objects.filter(subject=subject).order_by('-created')
        return self.render_to_response({'subject': subject, 'subjects': subjects, 'courses': courses})