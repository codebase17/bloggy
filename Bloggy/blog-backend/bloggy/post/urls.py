import imp
from django.urls import path
from post import views

urlpatterns=[
    path('post/addPost/',views.addPost)
    # path('post/updatePost/$',views.updatePost),
    # path('post/deletePost',views.deletePost),
    # path('post/getPost',views.getPost)
]