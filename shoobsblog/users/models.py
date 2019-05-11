from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ForeignKey
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from agilestoryboard.models import Team


class User(AbstractUser):
    ROLE_CHOICES = (
        ('DEV', 'Developer'),
        ('OWN', 'Owner'),
        ('MAS', 'Master'),
    )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    user_role = CharField(max_length=3, choices=ROLE_CHOICES,)
    user_team = ForeignKey(Team, related_name='team',)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
