from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import Post, Author, Comment

# Create your views here.

def home(request):
	context = RequestContext(request)
	return render_to_response("base.html",context)

def index(request):
    context = RequestContext(request)
    return render_to_response("index.html",context)

@login_required(login_url="/admin/")
def blog(request):
    if 'POST' in request.method:
        #autho = request.POST['author']
        content = request.POST['content']
        title = request.POST['title']
        user =Author.objects.get(name=request.user)
        post = Post(author=user,content=content,title=title)
        post.save()

    out = [7,8,9,10,11]
    context = RequestContext(request)
    posts = Post.objects.all().exclude(id__in=out)
    context['posts'] = posts
    return render_to_response("blog.html",context)

def post(request, id_post):
    post = Post.objects.get(pk=id_post)
    if 'POST' in request.method:
        content=request.POST['content']
        author = request.POST['author']
        comment = Comment(author=author,contenido=content,post=post)
        comment.save()

    comentario = Comment.objects.filter(post=post)
    context = RequestContext(request)
    context['comments']= comentario
    context['post']=post
    return render_to_response("post.html",context)

def calc(request):
    post = Post.objects.get(pk=7)
    if 'POST' in request.method:
        content=request.POST['content']
        author = request.POST['author']
        comment = Comment(author=author,contenido=content,post=post)
        comment.save()

    comentario = Comment.objects.filter(post=post)
    context = RequestContext(request)
    context['comments'] = comentario
    context['post']=post
    return render_to_response('calc.html',context)

def divisas(request):
    post = Post.objects.get(pk=8)
    if 'POST' in request.method:
        content=request.POST['content']
        author = request.POST['author']
        comment = Comment(author=author,contenido=content,post=post)
        comment.save()

    comentario = Comment.objects.filter(post=post)
    context = RequestContext(request)
    context['comments'] = comentario
    context['post']=post
    return render_to_response('divisas.html',context)

def cron(request):
    post = Post.objects.get(pk=9)
    if 'POST' in request.method:
        content=request.POST['content']
        author = request.POST['author']
        comment = Comment(author=author,contenido=content,post=post)
        comment.save()

    comentario = Comment.objects.filter(post=post)
    context = RequestContext(request)
    context['comments'] = comentario
    context['post']=post
    return render_to_response('cron.html',context)

def gallery(request):
    post = Post.objects.get(pk=10)
    if 'POST' in request.method:
        content=request.POST['content']
        author = request.POST['author']
        comment = Comment(author=author,contenido=content,post=post)
        comment.save()

    comentario = Comment.objects.filter(post=post)
    context = RequestContext(request)
    context['comments'] = comentario
    context['post']=post
    return render_to_response('gallery.html',context)

def formulario(request):
    post = Post.objects.get(pk=11)
    if 'POST' in request.method:
        content=request.POST['content']
        author = request.POST['author']
        comment = Comment(author=author,contenido=content,post=post)
        comment.save()

    comentario = Comment.objects.filter(post=post)
    context = RequestContext(request)
    context['comments'] = comentario
    context['post']=post
    return render_to_response('formulario.html',context)
