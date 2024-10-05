# for low level
from django.http import HttpResponse
from django.template import loader

# for high level
from django.shortcuts import render

from .models import Bb

# low level access
# def index(request):
#     template = loader.get_template('bboard/index.html')
#     bbs = Bb.objects.order_by("-published")
#     context = {'bbs': bbs}
#     return HttpResponse(template.render(context, request))

# high level access
def index(request):
    bbs = Bb.objects.all()
    return render(request=request, template_name='bboard/index.html', context={'bbs': bbs})
