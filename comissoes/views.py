from django.utils.translation import ugettext_lazy as _

from .models import (TipoComissao, Comissao, Periodo, CargoComissao)
from sapl.crud import build_crud


cargo_crud = build_crud(
    CargoComissao,

    [_('Período de composição de Comissão'),
     [('nome', 10), ('unico', 2)]],
)

periodo_composicao_crud = build_crud(
    Periodo,

    [_('Cargo de Comissão'),
     [('data_inicio', 6), ('data_fim', 6)]],
)

tipo_comissao_crud = build_crud(
    TipoComissao,

    [_('Tipo Comissão'),
     [('nome', 9), ('sigla', 3)],
     [('dispositivo_regimental', 9), ('natureza', 3)]],
)

comissao_crud = build_crud(
    Comissao,

    [_('Dados Básicos'),
     [('nome', 9), ('sigla', 3)],
     [('tipo', 3),
      ('data_criacao', 3),
      ('unidade_deliberativa', 3),
      ('data_extincao', 3)]],

    [_('Dados Complementares'),
     [('local_reuniao', 4),
      ('agenda_reuniao', 4),
      ('telefone_reuniao', 4)],
     [('endereco_secretaria', 4),
      ('telefone_secretaria', 4),
      ('fax_secretaria', 4)],
     [('secretario', 4), ('email', 8)],
     [('finalidade', 12)]],

    [_('Temporária'),
     [('apelido_temp', 8),
      ('data_instalacao_temp', 4)],
     [('data_final_prevista_temp', 4),
      ('data_prorrogada_temp', 4),
      ('data_fim_comissao', 4)]],
)


class ComposicaoListView(comissao_crud.CrudDetailView):
    template_name = 'comissoes/composicao.html'


class MateriasListView(comissao_crud.CrudDetailView):
    template_name = 'comissoes/materias.html'


class ReunioesListView(comissao_crud.CrudDetailView):
    template_name = 'comissoes/reunioes.html'
