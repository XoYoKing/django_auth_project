from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	nickname = models.CharField(max_length=50,blank=True)

	# AbstractUser.Mata 必须继承这个元类,已有的属性.
	class Meta(AbstractUser.Meta):
		pass
