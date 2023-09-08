from django.urls import path
from applications.post.views import *

urlpatterns = [
    path("", ListPostView.as_view()),
    path("<int:pk>/", RetrievePostView.as_view()),
    path("create/", CreatePostView.as_view()),
    path("update/<int:pk>/", UpdatePostView.as_view()),
    path("delete/<int:pk>/", DeletePostView.as_view()),
]
