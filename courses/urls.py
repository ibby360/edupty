from django.urls import path
from courses import views

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),

    # Create Course
    path('create/', views.CourseCreateView.as_view(), name='course_create'),

    # Module list
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(),
         name='module_content_list'),

    # Edit Course
    path('edit/<slug>', views.CourseUpdateView.as_view(), name='course_edit'),

    # Delete Course
    path('delete/<slug>', views.CourseDeleteView.as_view(), name='course_delete'),

    # Update Course Module
    path('module/<slug>/', views.CourseModuleUpdateView.as_view(),
         name='course_module_update'),

    # Module Content Create
    path('module/<int:module_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(), name='module_content_create'),

    # Update Module Content
    path('module/<int:module_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(), name='module_content_update'),

    # Delete Module Content
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(),
         name='module_content_delete'),

     # Module Order
     path('module/order', views.ModuleOrderView.as_view(), name='module_order'),

     # Content Order
     path('content/order', views.ContentOrderView.as_view(), name='content_order')
]
