from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileSlugForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Profile







def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('profile')
    else:
        form = UserRegisterForm()

    return render(
    request,
     'users/registration.html',
     {
        'form': form
     }
     )


@login_required
# class CutLinkView(ListView):
#     model = Profile
#     template_name = 'users/user.html'
#     context_object_name = 'profile'
#     ordering = ['-pk']
#
#     def get_context_data(self, **kwards):
#         ctx = super(CutLinkView, self).get_context_data(**kwards)
#
#         ctx['title'] = 'Ссылки'
#         return ctx

def profile(request):
    if request.method == "POST":
        profileForm = ProfileSlugForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if profileForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!')
            return redirect('home')
    else:
        profileForm = ProfileSlugForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm
    }
    return render(request, 'users/profile.html', data)
