from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Creates a new user profile"""

        if not email:
            raise ValueError("user must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """creates a superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True 

        user.save(using=self._db)

        return user


#each model maps to a table in our database
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for profiles in the system"""

    #fields for the user profiles in our database system
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #it's normally 'username' but we override it
    REQUIRED_FIELDS = ['name']

#these are functions that django can use to interact with our custom user model
    def get_full_name(self):
        """retrieve the user's full name"""
        return self.name

    def get_short_name(self):
        """retrieve user's short name"""
        return self.name

    def __str__(self):
        """returns the string representation of a userprofle"""
        return self.email
