from django.db import models
from django.core.validators import RegexValidator

class Message(models.Model):
    last_name = models.CharField(max_length=355, blank=False)
    first_name = models.CharField(max_length=255, blank=False)
    phone_regex = RegexValidator(
        regex=r'^\+32\s\d{2}\s\d{3}\s\d{2}\s\d{2}$',
        message="Phone number must be in the format '+32 XX XXX XX XX'"
    )
    telephone = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    email = models.EmailField(blank=False)
    adress_start = models.CharField(max_length=300, blank=False)
    stage_start = models.CharField(max_length=110, blank=False)
    adress_arrived = models.CharField(max_length=300, blank=True)
    stage_arrived = models.CharField(max_length=110, blank=True)
    message = models.TextField(max_length=1500, blank=False)