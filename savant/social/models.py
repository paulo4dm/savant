from django.db import models
from django.utils import timezone

class Connection(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Ativa', 'Ativa'),
        ('Inativa', 'Inativa'),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pendente',
    )    
    area_interesse = models.ForeignKey('Area')
    tutor = models.ForeignKey('auth.User', related_name='tutor')
    educando = models.ForeignKey('auth.User', related_name='educando')
    data_solicitacao = models.DateTimeField(
            default=timezone.now)
    
    def __str__(self):
   		return str(self.tutor.username) + ' X ' + str(self.educando.username)

class Area(models.Model):
    area = models.CharField(max_length=200, null=True)
    
    def __str__(self):
   		return self.area