from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class Hostel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    hostel_name = models.CharField(max_length=100)
    hostel_room_number = models.CharField(max_length=100)
    hostel_entry = models.DateTimeField()
    hostel_exit = models.DateTimeField()


    class Meta:
        db_table = 'hostel'
        verbose_name_plural = 'hostels'

    def __str__(self) -> str:
        return f'{self.user.full_name}-{self.hostel_room_number}'

