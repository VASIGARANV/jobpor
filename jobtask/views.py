from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm
from .filters import JobFilter

def job_list(request):
    f = JobFilter(request.GET, queryset=Job.objects.all())
    return render(request, "job_list.html", {"filter": f})

def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("job_list")
    else:
        form = JobForm()
    return render(request, "job_form.html", {"form": form})

