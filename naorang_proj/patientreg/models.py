from django.db import models
#from django.contrib.auth.models import User
from staff.models import User
from django.urls import reverse
from PIL import Image


from django.utils import timezone


class FemaleManager(models.Manager):
    """docstring for PublishedManager"""

    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(sex="female")


class PnameManager(models.Manager):
    """docstring for PublishedManager"""

    def get_queryset(self):
        return super(PnameManager, self).get_queryset().filter('pname')


class PatientName(models.Model):

    objects = models.Manager()  # not required
    female = FemaleManager()

    INDIAN = 'INDIAN'
    NRI = 'NRI'

    ADULT = 'ADULT'
    CHILD = 'CHILD'

    MR = 'Mr'
    MRS = 'Mrs'
    MS = 'Ms'
    DR = 'Dr'

    male = 'male'
    female = 'female'

    TITLE_CHOICES = (

        (MR, 'Mr'),
        (MS, 'Ms'),
        (MRS, 'Mrs'),
        (DR, 'Dr'),
    )

    A_C_CHOICES = (

        (ADULT, 'ADULT'),
        (CHILD, 'CHILD'),

    )

    FOREIGNER_NRI_CHOICES = (

        (INDIAN, 'INDIAN'),
        (NRI, 'NRI'),

    )

    SEX_CHOICES = (

        (male, 'male'),
        (female, 'female'),

    )
    patient_id = models.AutoField(primary_key=True)

    pname = models.CharField(max_length=255, null=True, blank=False)
    title_n = models.CharField(max_length=10, choices=TITLE_CHOICES, default='', null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    age = models.DecimalField(max_digits=5, decimal_places=2)
    addult_child = models.CharField(max_length=10, choices=A_C_CHOICES, default='', null=True, blank=True)
    p_h_g_name = models.CharField(max_length=255, null=True, blank=True)
    staff = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sex = models.CharField(max_length=7, choices=SEX_CHOICES, default='', null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    contact_no = models.DecimalField(max_digits=15, decimal_places=0)
    foreigner_NRI = models.CharField(max_length=50, choices=FOREIGNER_NRI_CHOICES, default='INDIAN', null=True, blank=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    passport_no = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    passport_of_country = models.CharField(max_length=255, null=True, blank=True)

    image = models.ImageField(default='defaultf.jpg', upload_to='patient_pics')

    # Create your models here.

    # def __str__(self):
    #   return f'{self.pname} Picture'

    def __str__(self):
        return self.pname

    # def female(self):
     #   return

    def save(self, *args, **kwargs):  # this was a prob here
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def get_patient_id(self):
        return f'NHC-{self.patient_id:04}'

    @property
    def get_patient_age(self):
        if self.age.is_integer():
            return f'{self.age} Years old '
        else:
            return f'{self.age:.2} Years old '

    def get_absolute_url(self):
        return reverse('staff-home',)
