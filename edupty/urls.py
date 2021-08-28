import courses
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from edupty import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/login/', views.login_page, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls')),
    path('', views.HomeView.as_view(), name='home_view'),
    path('subject/<slug:subject>/', views.HomeView.as_view(), name='course_list_subject')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)