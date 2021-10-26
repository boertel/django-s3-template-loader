from django.shortcuts import render
from django.conf import settings


def index(request):
    directory = settings.S3_TEMPLATE_LOADER_BUILD_DIRECTORY
    return render(request, "{}/index.html".format(directory))
