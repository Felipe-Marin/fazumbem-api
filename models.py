from webapp import db
import enum
from datetime import datetime

class TipoPessoa(enum.Enum):
    PF = 'PF'
    PJ = 'PJ'

class TipoAjuda(enum.Enum):
    RECEBE = 'RECEBE'
    FORNECE = 'FORNECE'

class FormaAjuda(enum.Enum):
    DINHEIRO = 'DINHEIRO'
    MATERIAL = 'MATERIAL'

class TipoBeneficiado(enum.Enum):
    PJ = 'PJ'

class Entidade(db.Model):
    __tablename__ = 'entidades'

    entidade_id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(), nullable=False)
    tipo_pessoa = db.Column(db.Enum(TipoPessoa))
    url_entidade = db.Column(db.String())
    descricao = db.Column(db.String())

    def __init__(self, nome, tipo_pessoa, url_entidade, descricao):
        self.nome = nome
        self.tipo_pessoa = tipo_pessoa
        self.url_entidade = url_entidade
        self.descricao = descricao

    def __repr__(self):
        return '<Entidade %r>' % self.nome

    def serialize(self):
        return{
            'entidade_id': self.entidade_id,
            'nome': self.nome,
            'tipo_pessoa': self.tipo_pessoa.value,
            'url_entidade': self.url_entidade,
            'descricao': self.descricao
        }

class Acao(db.Model):
    __tablename__ = 'acoes'

    acao_id = db.Column(db.Integer, primary_key=True)
    entidade_id = db.Column(db.Integer, db.ForeignKey('entidade.entidade_id'), nullable=False)
    nome_acao = db.Column(db.String(), nullable=False)
    imagem_acao = db.Column(db.LargeBinary())
    url_acao = db.Column(db.String())
    descricao = db.Column(db.String())
    contato = db.Column(db.String())
    tipo_ajuda = db.Column(db.Enum(TipoAjuda), nullable=False)
    forma_ajuda = db.Column(db.Enum(FormaAjuda), nullable=False)
    data_insercao = db.Column(db.DateTime())
    data_atualizacao = db.Column(db.DateTime())
    forma_verificacao = db.Column(db.String())
    resp_verificacao = db.Column(db.String())
    ativa = db.Column(db.Boolean())
    permanente = db.Column(db.Boolean())
    validade = db.Column(db.String())

    def __init__(self, entidade_id, nome_acao, imagem_acao, url_acao, descricao, contato, tipo_ajuda, forma_ajuda, forma_verificacao, resp_verificacao, ativa, permanente, validade):
        self.entidade_id = entidade_id
        self.nome_acao = nome_acao
        self.imagem_acao = imagem_acao
        self.url_acao = url_acao
        self.descricao = descricao
        self.contato = contato
        self.tipo_ajuda = tipo_ajuda
        self.forma_ajuda = forma_ajuda
        self.data_insercao = datetime.now()
        self.data_atualizacao = datetime.now()
        self.forma_verificacao = forma_verificacao
        self.resp_verificacao = resp_verificacao
        self.ativa = ativa
        self.permanente = permanente
        self.validade = validade

    def __repr__(self):
        return '<Acão %r>' % self.nome_acao

    def serialize(self):
        return{
            'acao_id': self.acao_id,
            'entidade_id': self.entidade_id,
            'nome_acao': self.nome_acao,
            'imagem_acao': self.imagem_acao,
            'url_acao': self.url_acao,
            'descricao': self.descricao,
            'contato': self.contato,
            'tipo_ajuda': self.tipo_ajuda.value,
            'forma_ajuda': self.forma_ajuda.value,
            'data_insercao': self.data_insercao,
            'data_atualizacao': self.data_atualizacao,
            'forma_verificacao': self.forma_verificacao,
            'resp_verificacao': self.resp_verificacao,
            'ativa': self.ativa,
            'permanente': self.permanente,
            'validade': self.validade
        }
