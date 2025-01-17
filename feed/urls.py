from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('createpost/', views.create_post, name='post'),
    path('<int:id>/', views.post_view, name='post_view'),
    path('<int:id>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<int:id>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
