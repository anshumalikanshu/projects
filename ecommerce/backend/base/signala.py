import imp


from django.db.models.signals import pre_save

from django.contrib.auth.models import User


def user_update(sender, instance, **kwargs):

    user = instance
    if user.email != '':
        user.username = user.email

    print("update the username", user.email, " ", user.username)


pre_save.connect(user_update, sender=User)
