from django.db import models

from authentication.views import User

# Create your models here.

class StudentTicket(models.Model):
    ticket_code = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    message = models.TextField()
    is_sorted = models.IntegerField(default=0)

    class Meta:
        db_table = 'student_tickets'
        

    def __str__(self) -> str:
        return self.user.email