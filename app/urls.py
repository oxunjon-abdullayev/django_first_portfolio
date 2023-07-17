from django.urls import path

from app.views import index_view, blog_list, blog_details, contact_view

urlpatterns = [
    path('', index_view, name='index'),
    path('blog-list/', blog_list, name='blog_list'),
    path('blog-details/<int:blog_id>', blog_details, name='blog_details') ,
    path('contact/', contact_view, name='contact')
]