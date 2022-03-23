from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, FormView
from reg.forms import *
from .utils import word_and_answer_options
from .models import *


class AddQuery(TemplateView):
    template_name = 'reg/home.html'
    form = None
    english_word = None
    num_attempts = 10
    num_right_ans = 0
    result = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(AddQuery, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            AddQuery.form = HomeForm(word_and_answer_options())
            AddQuery.english_word = AddQuery.form.english_word
        else:
            AddQuery.num_attempts -= 1
            if AddQuery.num_attempts != 0:
                if self.request.POST['choice_field'] == AddQuery.form.right_answer:
                    AddQuery.form = HomeForm(word_and_answer_options())
                    AddQuery.english_word = AddQuery.form.english_word
                    AddQuery.num_right_ans += 1
                else:
                    AddQuery.form = HomeForm(word_and_answer_options())
                    AddQuery.english_word = AddQuery.form.english_word
            else:
                Statistics.objects.create(user=self.request.user,
                                          ratio=AddQuery.num_right_ans)
                AddQuery.result = f'Количество правильных ответов {AddQuery.num_right_ans} из 10'
                AddQuery.num_attempts = 10
                AddQuery.num_right_ans = 0
        context['form'] = AddQuery.form
        context['english_word'] = AddQuery.english_word
        context['result'] = AddQuery.result
        AddQuery.result = None
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'reg/reg_login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Registration'
        context['state'] = 'reg'
        return context


class LoginUser(LoginView):
    form_class = AuthenticationUserForm
    template_name = 'reg/reg_login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Log in'
        context['state'] = 'login'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
