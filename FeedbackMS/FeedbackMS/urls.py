from django.contrib import admin
from django.urls import path
from core.views import (
	home,
	feedback
	)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('feedback',feedback,name="feedback")
]
