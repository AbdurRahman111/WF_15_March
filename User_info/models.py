from django.db import models
from datetime import datetime
# Create your models here.

# for making password hash
from django.contrib.auth.hashers import make_password


class User_information(models.Model):
    class Meta:
        verbose_name_plural = 'User information'

    User_Roll_CHOICES = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Operations', 'Operations'),
        ('Normal User', 'Normal User'),
    )
    User_Roll = models.CharField(max_length=256, choices=User_Roll_CHOICES, blank=True, null=True)

    User_Name = models.CharField(max_length=256, blank=True, null=True)
    User_Password = models.CharField(max_length=256, blank=True, null=True)
    # changed_password = models.BooleanField(blank=True, null=True)
    User_Email = models.CharField(max_length=256, blank=True, null=True)
    User_Phone = models.CharField(max_length=256, blank=True, null=True)
    User_Joing_Date_Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.User_Name


    def save(self, *args, **kwargs):
        # print('args')
        # print(self.changed_password)
        # if self.changed_password == True:
        self.User_Password = make_password(self.User_Password)
        super(User_information, self).save(*args, **kwargs)


