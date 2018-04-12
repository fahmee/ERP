from django.conf.urls import url
from . import views

app_name = 'collage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^create_department/$', views.create_department, name='create_department'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<department_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<department_id>[0-9]+)/delete_department/$', views.delete_department, name='delete_department'),
    url(r'^(?P<department_id>[0-9]+)/create_student/$', views.create_student, name='create_student'),
    url(r'^personal_detail/$', views.personal_detail, name='personal_detail'),
   
    url(r'^(?P<department_id>[0-9]+)/delete_student/(?P<student_id>[0-9]+)/$', views.delete_student, name='delete_student'),
    ]