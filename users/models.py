from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.
class Person(models.Model):
    """
    This is the person model which represents each team member of the team.
    """
    # user roles
    class personRole(models.TextChoices):
        """
        This class represents all roles a user can possibly be.
        """
        ADMIN = "admin", _('Administrator')
        REGULAR = 'regular', _('Regular')

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    role = models.CharField(
        max_length=15,
        choices=personRole.choices,
        default=personRole.REGULAR,
    )
