from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogCreatForm
from .models import Blog 

def blog_create(request):
    if request.method == 'GET':
        return render(request, 'blog_create.html', {'form': BlogCreatForm})
    else:
        blog_create = BlogCreatForm(request.POST)
        blog_create.save()
        return redirect('blog_list')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs':blogs})

   
def blog_update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'GET':
        form = BlogCreatForm(instance=blog)
        return render(request, 'blog_update.html', {'blog':blog, 'form':form})
    else:
        form = BlogCreatForm(request.POST)
        form.save()
        return redirect('blog_list')

def delete(request, blog_id):
    blogs = Blog.objects.get(pk=blog_id)
    blogs.delete()
    return redirect('blog_list')