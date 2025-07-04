from django.contrib import admin

# Register your models here.
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "type", "salary_min", "salary_max", "deadline")
    list_filter = ("type", "location")
    search_fields = ("title", "company")
