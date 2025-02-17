from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


from PIL import Image


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an e-mail address ")
        if not username:
            raise ValueError("Users must have a username ")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def get_queryset(self):
     #   return super(MyUserManager, self).get_queryset().filter("is_dr")

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # i added this

    is_dr = models.BooleanField(default=False)
    is_rec = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]  # check this "," might be a problem

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    #address = models.TextField(null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
# Create your models here.

    # def save(self, *args, **kwargs):  # this was a prob here
     #   super().save()

      #  img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #    output_size = (300, 300)
        #   img.thumbnail(output_size)
        #  img.save(self.image.path)


class Staff(models.Model):

    staff = models.OneToOneField(User, on_delete=models.CASCADE)
