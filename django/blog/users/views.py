from django.shortcuts import render
from .models import *

def main(request):
    # projects = Project.objects.all().order_by('-id')
    # context = {'projects': projects}
    #
    # return render(
    #     request=request,
    #     template_name='home.html',
    #     context=context
    # )
    return render(
        request=request,
        template_name='home.html',
    )

def project(request):
    projects = Project.objects.all().order_by('-id')
    context = {'projects': projects}

    return render(
        request=request,
        template_name='project.html',
        context=context
    )