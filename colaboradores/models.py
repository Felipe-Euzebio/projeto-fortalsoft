from django.db import models

# Create your models here.
class Colaborador(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)
    rg = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    conta_bancaria = models.CharField(max_length=15)
    agencia_bancaria = models.CharField(max_length=15)
    descricao_banco = models.CharField(max_length=50)
    codigo_banco = models.IntegerField(null=True, blank=True)
    dv_banco = models.IntegerField(null=True, blank=True)
    dv_conta = models.IntegerField(null=True, blank=True)
    operacao_conta = models.IntegerField(null=True, blank=True)
    tipo_conta = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome



