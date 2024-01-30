from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Profile, Services, Project
from django.shortcuts import get_object_or_404
def Home(request):
    profile = Profile.objects.all().first()
    services = Services.objects.all()


    context = {
            'profile': profile,
            'services': services,

    }
    
    return render(request, 'index.html', context)

def singl_service(request, slug):
    services = Services.objects.all()
    service = Services.objects.get(slug=slug)
    projects = service.project_set.all()
    context = {
        'service': service,
        'projects': projects,
        'services': services,
    }
    return render(request, 'service_details.html', context)

def project_details(request, slug):
    project = get_object_or_404(Project,slug=slug)
    context = {
        'project':project
    }
    return render(request, 'project_details.html', context)