from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    def home(request):
        return HttpResponse('hello world')