from django.db import models

# Create your models here.
class Colaborador(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome: ")
    sobrenome = models.CharField(max_length=50, verbose_name="Sobrenome: ")
    rg = models.CharField(max_length=30, verbose_name="RG: ")
    cpf = models.CharField(max_length=30, verbose_name="CPF: ")
    cargo = models.CharField(max_length=50, verbose_name="Cargo: ")
    email = models.EmailField(max_length=30, verbose_name="Email: ")
    conta_bancaria = models.CharField(max_length=15, verbose_name="Conta Bancária: ")
    agencia_bancaria = models.CharField(max_length=15, verbose_name="Agência Bancária: ")
    tipo_conta = models.CharField(max_length=20, verbose_name="Tipo da Conta: ")
    descricao_banco = models.CharField(max_length=50, verbose_name="Banco: ")
    codigo_banco = models.IntegerField(null=True, blank=True, verbose_name="Código do Banco: (opcional)")
    dv_banco = models.IntegerField(null=True, blank=True, verbose_name="Dígito Verificador do Banco (opcional): ")
    dv_conta = models.IntegerField(null=True, blank=True, verbose_name="Dígito Verificador da Conta (opcional): ")
    operacao_conta = models.IntegerField(null=True, blank=True, verbose_name="Operador da Conta (opcional): ")
    feedback = models.TextField(max_length=300, null=True, blank=True, verbose_name="Feedback (opcional): ")

    # def __str__(self):
    #     return f'{nome} {sobrenome}'



