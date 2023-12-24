from django.urls import path
from .views import course_list, course_detail, create_course, edit_course, delete_course, materi_list, create_materi, edit_materi, delete_materi

urlpatterns = [
    path('', course_list, name='course_list'),
    path('courses/<int:course_id>/', course_detail, name='course_detail'),
    path('courses/create/', create_course, name='create_course'),
    path('courses//edit/<int:course_id>', edit_course, name='edit_course'),
    path('courses/delete/<int:course_id>/', delete_course, name='delete_course'),
    
    path('materi/', materi_list, name='materi'),
    path('materi/<int:course_id>/create_materi/', create_materi, name='create_materi'),
    path('materi/edit_materi/<int:materi_id>/', edit_materi, name='edit_materi'),
    path('materi/delete_materi/<int:materi_id>/', delete_materi, name='delete_materi'),
]
