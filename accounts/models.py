from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone
#############################################################################################
class CustomUserManager(BaseUserManager):

    def create_user(self,first_name,last_name,username,email,password,**other_fields):
        if not email:
            raise ValueError('The Email is mandatory')
        if not username:
            raise ValueError('The username is mandatory')

        user = self.model(
            email= self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,**other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,password,**other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_admin',True)
        # when the super user is created then also create the superadmin
        other_fields.setdefault('is_superadmin',True)
        
        #  this is and validation checkup while creation method
        if other_fields.get('is_staff') is not True:
            raise ValueError('Super user is_staff must be True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must set to True')
        if other_fields.get('is_active') is not True:
            raise ValueError('is_active must be set to True')
        if other_fields.get('is_admin') is not True:
            raise ValueError('is_admin must be set to True')
        if other_fields.get('is_superadmin') is not True:
            raise ValueError('is_superadmin must be set to True')

        return self.create_user(first_name,last_name,username,email,password,**other_fields)
    

class Account(AbstractBaseUser,PermissionsMixin):
    ''' This is the user models which created the help of abstract Base User , we need to 
    write every things from the scratch in this AbstractBaseUser '''
    # Choce fiedls creation
    ROLE = (
        ('admin','ADMIN'),
        ('user','USER')
        )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.CharField(max_length=20)
    #required 
    role = models.CharField(max_length=100,choices=ROLE,null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # custom permission
    is_superadmin = models.BooleanField(default=False)
    is_admins = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

    # Specified that all objects for the class come from the CustomUserManager
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return self.email