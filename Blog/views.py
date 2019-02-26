from django.shortcuts import render_to_response, render , get_object_or_404
from .models import Blog

# Create your views here.

def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render(request, 'blog_list.html', context=context)


def blog_detail(request, blog_pk):
    context={}
    context['blog'] = get_object_or_404(Blog, pk= blog_pk)
    return render(request, 'blog_detail',context=context)
