from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    STATUS = (
        ('sent', 'Sent'),
        ('unread', 'Unread'),
        ('read', 'Read'),
        ('replied', 'Replied'),
    )

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados',verbose_name='Sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos',verbose_name='Recipient')
    subject = models.CharField(max_length=255,verbose_name='Subjet')
    content = models.TextField(verbose_name='Content')
    date_sent = models.DateTimeField(auto_now_add=True,verbose_name='Date')
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas',verbose_name='Reply to')
    status = models.CharField(max_length=10, choices=STATUS, default='sent',verbose_name='Status')

    def __str__(self):
        return f'Mensaje de {self.sender} a {self.recipient} en {self.date_sent}'


class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    readers = models.ManyToManyField(User, related_name='read_chats', blank=True)






