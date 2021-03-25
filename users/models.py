from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='profile') # Nome Completo, Senha, Username, Email
    sex = models.CharField(max_length=14)
    image = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField(to='self')

    @staticmethod
    def create_profile(username, password, first_name, last_name, email, sex, birth_date = None, image = ''):

        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        if user is not None:
            profile = Profile(user=user, sex=sex, birth_date=birth_date, image=image)
            profile.save()
            return profile
        else:
            return False
