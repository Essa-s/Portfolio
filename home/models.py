from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import os

# Create your models here.


def service_files(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join("services", filename)


def project_files(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join("projects", filename)


def profile_files(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join("profile", filename)


class Profile(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    greeting = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    avatar = models.ImageField(
        upload_to=profile_files, height_field=None, width_field=None, max_length=None
    )
    home_image = models.ImageField(
        upload_to=profile_files, height_field=None, width_field=None, max_length=None
    )
    birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    block1_detail = models.CharField(max_length=50)
    block1_number = models.IntegerField()
    block2_detail = models.CharField(max_length=50)
    block2_number = models.IntegerField()
    block3_detail = models.CharField(max_length=50)
    block3_number = models.IntegerField()
    block4_detail = models.CharField(max_length=50)
    block4_number = models.IntegerField()

    @classmethod
    def object(cls):
        return cls._default_manager.all().first()  # Since only one item

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Services(models.Model):
    service = models.CharField(max_length=50)
    price = models.IntegerField()
    main_image = models.ImageField(
        upload_to=service_files, height_field=None, width_field=None, max_length=None
    )
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.service)
        super(Services, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Services"

    def __str__(self):
        return self.service


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    link = models.URLField(max_length=200)
    main_image = models.ImageField(upload_to=project_files)
    optional_image1 = models.ImageField(
        upload_to=project_files,
        blank=True,
        null=True,
    )
    optional_image2 = models.ImageField(upload_to=project_files, blank=True, null=True)
    optional_image3 = models.ImageField(upload_to=project_files, blank=True, null=True)
    category = models.ForeignKey(Services, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
