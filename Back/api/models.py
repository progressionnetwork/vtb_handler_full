import os

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Менеджер пользователя (Модель)
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        База создания пользователя
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Создание пользователя
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Создание суперпользователя
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Custom User Class
class User(AbstractUser):
    """
    Пользователь (Модель)
    """
    username = None
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


class ProcessingFile(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    file_object = models.FileField('Input File Object', upload_to='processed')
    result_file_object = models.TextField('Result File Object', default='', null=True, blank=True)
    file_name = models.CharField('File name', max_length=256, default='',null=True, blank=True)
    file_size = models.PositiveBigIntegerField('File bytes size' , default=0, null=True, blank=True)
    result_file_size = models.PositiveBigIntegerField('File bytes size' , default=0, null=True, blank=True)
    ready_status = models.BooleanField('Status', default=False)
    result_json = models.JSONField('JSON',null=True, blank=True)
    total_danger = models.IntegerField('Danger',  default=0,null=True, blank=True)
    total_files = models.IntegerField('Files',  default=0,null=True, blank=True)
    total_archives = models.IntegerField('Files',  default=0 ,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Обработка полей перед сохранением модели
        """
        if not self.pk:
            self.file_name = self.file_object.name
            self.file_size = self.file_object.size
            self.ready_status = False
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Processing file'
        verbose_name_plural = 'Processing files'

    def filename(self):
        return os.path.basename(self.file_object.name)
