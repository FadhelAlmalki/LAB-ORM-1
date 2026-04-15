from django.urls import path
from . import views


app_name = 'posts'

urlpatterns =[
    path('create/', views.create_post_view, name='create_post_view'),
    path('detail/<int:post_id>/', views.post_detail_view, name='post_detail_view'),
    path('update/<int:post_id>/', views.update_post_view, name='update_post_view'),
    path('delete/<int:post_id>/', views.delete_post_view, name='delete_post_view'),
]