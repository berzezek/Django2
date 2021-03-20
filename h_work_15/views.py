from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News, Comment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def home(request):
    return render(request, 'users/user.html')

def uslugi(request):
    return render(request, 'h_work_15/uslugi.html')

def about(request):
    return render(request, 'h_work_15/about.html')

class ShowNewsView(ListView):
    model = News
    template_name = 'h_work_15/news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 2

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Новости'
        return ctx

class NewsDetailView(DetailView):
    model = News
    template_name = 'h_work_15/news_detail.html'
    # context_object_name = 'post'
    paginate_by = 1

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name='h_work_15/news_form.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'h_work_15/news_form.html'
    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True

        return False

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'h_work_15/news_delete.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True

        return False

class UserAllNewsView(ListView):
    model = News
    template_name = 'h_work_15/user_news.html'
    context_object_name = 'news'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(autor=user).order_by('-date')


    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)

        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
        return ctx

class CreateComment(CreateView):
    model = Comment
    template_name='h_work_15/comment.html'
    fields = ['post', 'email', 'body']

    def form_valid(self, form):
        subject = "Коммент"
        plain_message = "Был получен новый комментарий"
        from_email = "From zakritie.nds6@gmail.com"
        to = "wknduz@gmail.com"
        send_mail(subject, plain_message, from_email, [to])
        return super().form_valid(form)


class ShowComment(ListView):
    model = Comment
    template_name = 'h_work_15/news_comment.html'
    context_object_name = 'comment'
    paginate_by = 5
    ordering = ['-date']

    # def get_context_data(self, **kwards):
    #     ctx = super(ShowComment, self).get_context_data(**kwards)
    #
    #     ctx['prov'] = form.instance.email
    #     return ctx
