"""quizsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from quiz import views
urlpatterns = [
    url(r"^$", views.startpage),
    url(r"^quiz/[0-9]+/$",views.quiz),
    url(r"^quiz/[0-9]+/question/[0-9]+/$", views.question),
	url(r"^quiz/[0-9]+/completed/$", views.completed),
]
