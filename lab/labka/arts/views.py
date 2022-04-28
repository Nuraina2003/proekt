from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage, send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


def index(request):
    return render(request, 'arts/index.html')


def about(request):
    return render(request, 'arts/about.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Not found</h1>')


# def login(request):
# return HttpResponse("Сіз сәтті тіркелдіңіз!")

def show_post(request, post_slug):
    post = get_object_or_404(arts, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'arts/post.html', context=context)


def show_category(request, cat_id):
    posts = arts.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cat_selected': cat_id,
    }

    return render(request, 'arts/index.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'arts/register.html', {'form': form, 'title': 'registration'})


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'arts/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Login")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

def send_message(request):
    send_mail('django test mail', 'this is django test body',
              '200103126@stu.sdu.edu.kz',
              ['200103126@stu.sdu.edu.kz','n060103@mail.ru'],
              fail_silently=False, html_message="<b>Bold text</b><i> Italic text</i>")
    return render(request, 'art/successfull.html')

def send_message(request):
    email = EmailMessage(
        'Hello',
        'Body goes here',
        '200103126@stu.sdu.edu.kz',
        ['200103126@stu.sdu.edu.kz', 'n060103@mail.ru'],
        headers={'Message-ID': 'foo'},

    )
    email.attach_file('/Users/Привет/Pictures/Screenshots/2.png')
    email.send(fail_silently=False)
    return render(request, 'arts/successfull.html')
