from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class StudentMessaging(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    thread_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    is_read = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='message_attachments/', null=True, blank=True)
    is_draft = models.BooleanField(default=False)
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')

    class Meta:
        db_table = 'student_messages'
        verbose_name_plural = 'student_messages'

    def __str__(self) -> str:
        return self.user.full_name