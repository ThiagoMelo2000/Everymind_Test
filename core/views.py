from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views import View


class Access(View):

    template_name = 'access.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form  = request.POST
        user = authenticate(request, username=form['username'], password=form['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'error':'Credenciais inválidas'})

@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')