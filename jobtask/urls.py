
from django.urls import path
from .views import job_list, job_create

urlpatterns = [
    path("job_list/", job_list, name="job_list"),
    path("job_create/", job_create, name="job_create"),
]
