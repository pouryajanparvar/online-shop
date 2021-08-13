from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
# Create your models here.


class User(AbstractBaseUser):
    email      = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    is_active  = models.BooleanField(default=True)
    is_admin   = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']


    def __str__(self):
        return self.email

    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True


    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # کاربرانی که حق دسترسی به مدل ها را دارند
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        # کاربرانی که حق دسترسی به پنل ادمین جنگو را دارند
        return self.is_admin
    