from django.db import models


# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(upload_to='about/')
    bithday = models.DateField()
    site = models.CharField(max_length=202)
    phone_number = models.CharField(max_length=202)
    city = models.CharField(max_length=202)
    bot = models.CharField(max_length=202)
    degree = models.CharField(max_length=202)
    email = models.EmailField()
    freelance = models.CharField(max_length=202)
    happy_cleints = models.CharField(max_length=202)
    site_project = models.CharField(max_length=202)
    bot_project = models.CharField(max_length=202)
    students = models.CharField(max_length=202)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=202)
    year = models.CharField(max_length=202)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Professional(models.Model):
    title = models.CharField(max_length=202)
    year = models.CharField(max_length=202)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=202)
    icon = models.CharField(max_length=202)
    title = models.CharField(max_length=202)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Advantage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='advantage')
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.service.name


class Friend(models.Model):
    full_name = models.CharField(max_length=202)
    image = models.ImageField(upload_to='friend/')
    contact = models.CharField(max_length=202)
    job = models.CharField(max_length=202)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Contact_me(models.Model):
    phone = models.CharField(max_length=202)
    location = models.CharField(max_length=303)

    def __str__(self):
        return self.phone


class Contact(models.Model):
    name = models.CharField(max_length=202)
    username = models.CharField(max_length=202)
    phone = models.CharField(max_length=202)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
