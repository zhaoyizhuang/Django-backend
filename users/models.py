from django.utils.translation import gettext_lazy as _
from django.db import models
from .constants import constants


# Create your models here.
class User(models.Model):
    """
    This is the person model which represents each user of the team.
    """

    # user roles
    class personRole(models.TextChoices):
        """
        This class represents all roles a user can possibly be.
        """
        ADMIN = "admin", _('Administrator')
        REGULAR = 'regular', _('Regular')

    first_name = models.CharField(max_length=constants.MAX_NAME_LENGTH)
    last_name = models.CharField(max_length=constants.MAX_NAME_LENGTH)
    phone_number = models.CharField(max_length=constants.MAX_PHONE_NUM_LENGTH)
    email = models.CharField(max_length=constants.MAX_EMAIL_LENGTH)
    role = models.CharField(
        max_length=constants.MAX_ROLE_LENGTH,
        choices=personRole.choices,
        default=personRole.REGULAR,
    )
