from django.contrib.auth.models import User

def form_fomatter(POST,*args):
    exclude = ['csrfmiddlewaretoken']
    exclude.extend(args)
    form ={key:value for key, value in POST.items() if  key not in exclude}
    return form

def check_profile(username):
    user = User.objects.filter(username=username)
    return len(user) > 0