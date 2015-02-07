from django.db import models
from django.core import validators
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from apps.subscribe.models import Subscriptor


class MyUserManager(BaseUserManager):

    def create_user(self, email, first_name="", last_name="",
                    password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            raw_password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    subscriptor = models.ForeignKey(
        Subscriptor,
        null=True,
    )
    email = models.EmailField(
        verbose_name="email address",
        max_length=50,
        unique=True,
    )
    username = models.CharField(
        max_length=50,
        blank=True,
    )
    first_name = models.CharField(
        max_length=50,
        blank=True,
        validators=[
            validators.RegexValidator(
                r"^[a-zA-Z ]",
                "Invalid name."
            ),
        ],
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        validators=[
            validators.RegexValidator(
                r"^[a-zA-Z ]",
                "Invalid name."
            ),
        ],
    )
    is_admin = models.BooleanField(
        default=False,
    )
    was_registered = models.BooleanField(
        default=False,
    )
    raw_password = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


from .signals import update_user
