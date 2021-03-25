from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from users import models
from core.utils import check_profile

class Register(View):

    template_name  = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = request.POST
        if check_profile(form['username']):
            return render(request, self.template_name, {'error': 'Usuário já existe'})
        profile = models.Profile.create_profile(username=form['username'], password=form['password'], first_name=form['first_name'], last_name=form['last_name'], email=form['email'], sex=form['sex'], birth_date=form['birth_date'])
        if profile:
            login(request, profile.user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'error':'Ops! Ocorreu um erro, tente novamente!'})