
from django.shortcuts import render
from django.views import generic

class PostView(generic.View):
    def get(self, request):
        return HttpResponse('hello world')
