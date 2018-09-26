from django.db import models

# we are substituting a custom user model

# base of the user model and adding permissions to our User Models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager)

class UserProfileManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('User must have an e-mail address')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          last_name = last_name,
                          first_name = first_name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff     = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represent a user profile inside our system
    """

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name']

    def get_full_name(self):
        """
        Used to get a users full name
        """
        return self.last_name + self.first_name

    def get_short_name(self):
        """
           Used to get a users short name
        """
        return self.last_name


    def __str__(self):
        return self.email



class ProfileFeedItem(models.Model):

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}...'.format(self.status_text[:50])