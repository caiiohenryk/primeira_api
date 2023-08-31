from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'Nome: {self.nome}'
    
class TodoList(models.Model):
    tarefa = models.CharField(max_length = 20)
    choices_status = [
        ('READY', 'Pronto'),
        ('RN', 'Em andamento'),
        ('PENDENT', 'Pendente'),
    ]
    status = models.CharField(choices=choices_status, max_length=12)
    pessoa = models.ForeignKey(
    Pessoa,
    max_length=20,
    on_delete=models.CASCADE
)