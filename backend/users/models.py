from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number must be set')
        if not first_name:
            raise ValueError('The First Name must be set')

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, first_name, password=None, **extra_fields):
        user = self.create_user(
            phone_number=phone_number,
            first_name=first_name,
            password=password,
            **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    # email = models.EmailField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    username = None
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.phone_number
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_pics', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} Profile'
    

class OneTimeCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} {self.code}'
    
    def generate_unique_code(self):
        import random
        while True:
            # 6 xonali tasodifiy raqamli kod yaratish
            code = str(random.randint(100000, 999999))  # 6 xonali raqam
            # Kodning takrorlanmasligini tekshirish
            if not OneTimeCode.objects.filter(code=code).exists():
                break

        return str(code)
        

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        return super().save(*args, **kwargs)
