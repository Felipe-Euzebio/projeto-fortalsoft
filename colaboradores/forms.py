from django.forms import ModelForm
from .models import Colaborador

class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = [
            'nome',
            'sobrenome',
            'rg',
            'cpf',
            'cargo',
            'email',
            'conta_bancaria',
            'agencia_bancaria',
            'descricao_banco',
            'codigo_banco',
            'dv_banco',
            'dv_conta',
            'operacao_conta',
            'tipo_conta'
        ]