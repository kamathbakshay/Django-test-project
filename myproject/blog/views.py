from django.shortcuts import render
from django.template import loader
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
