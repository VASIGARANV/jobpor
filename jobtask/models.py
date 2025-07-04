from django.db import models

# Create your models here.
# jobs/models.py
from django.db import models

JOB_TYPES = [
    ("Full-time", "Full-time"),
    ("Part-time", "Part-time"),
    ("Contract", "Contract"),
    ("Internship", "Internship"),
]

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_logo = models.URLField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=JOB_TYPES)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
