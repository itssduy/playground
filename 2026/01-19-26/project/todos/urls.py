from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('python', views.hello_python_view, name='hello_python'),
    path('', views.hello_html_view, name='hello_html'),
    path('helloname/<str:name>', views.hello_path, name='hello_html'),
    path('helloquery', views.hello_query, name='helloquery'),
    path('special', views.special_view, name='special'),
    path('postendpoint', views.post_example, name='post_example'),
    path('submitexample', views.submit_example, name="submit_example"),
    path('submitdjango', views.submit_django_form, name="submit_django"),
    path('templates', views.template_view, name='template_view'),
    path('todos', views.todos_view, name='todos'),
]