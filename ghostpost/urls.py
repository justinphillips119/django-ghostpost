"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ghostpost_app.views import index, new_post_view, boasts_view, roasts_view, votes_view, upvote_view, downvote_view

urlpatterns = [
    path("", index, name="homepage"),
    path("newpost/", new_post_view, name="newpost"),
    path("boasts/", boasts_view, name="boasts"),
    path("roasts/", roasts_view, name="roasts"),
    path("votes/", votes_view, name="votes"),
    path("upvote/<int:post_id>/", upvote_view, name='upvote'),
    path("downvote/<int:post_id>/", downvote_view, name="downvote"),
    path('admin/', admin.site.urls),
]
