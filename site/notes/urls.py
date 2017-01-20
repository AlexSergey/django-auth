from django.conf.urls import url
from views import Notes

urlpatterns = [
    url(r'^index/', Notes.as_view(), name="index")
]
