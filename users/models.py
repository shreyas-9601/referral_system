from django.db import models
import random
import string

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=10, unique=True, blank=True, null=True)
    password = models.CharField(max_length=255)
    referrer = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def generate_referral_code(self):
        """Generate a unique referral code."""
        length = 6
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = self.generate_referral_code()
        super(User, self).save(*args, **kwargs)
