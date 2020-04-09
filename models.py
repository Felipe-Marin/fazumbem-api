import app
import enum

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

class Entidade(app.db.Model):
    __tablename__ = 'entidades'

    entidade_id = app.db.Column(app.db.Integer, primary_key=True)
    nome = app.db.Column(app.db.String(), nullable=False)
    tipo_pessoa = app.db.Column(app.db.Enum(TipoPessoa))
    url_entidade = app.db.Column(app.db.String())
    descricao = app.db.Column(app.db.String())

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

class Acao(app.db.Model):
    __tablename__ = 'acoes'

    acao_id = app.db.Column(app.db.Integer, primary_key=True)
    entidade_id = app.db.Column(app.db.Integer, app.db.ForeignKey('entidade.entidade_id'), nullable=False)
    nome_acao = app.db.Column(app.db.String(), nullable=False)
    imagem_acao = app.db.Column(app.db.LargeBinary())
    url_acao = app.db.Column(app.db.String())
    descricao = app.db.Column(app.db.String())
    contato = app.db.Column(app.db.String())
    tipo_ajuda = app.db.Column(app.db.Enum(TipoAjuda), nullable=False)
    forma_ajuda = app.db.Column(app.db.Enum(FormaAjuda), nullable=False)
    data_insercao = app.db.Column(app.db.DateTime())
    data_atualizacao = app.db.Column(app.db.DateTime())
    forma_verificacao = app.db.Column(app.db.String())
    resp_verificacao = app.db.Column(app.db.String())
    ativa = app.db.Column(app.db.Boolean())
    permanente = app.db.Column(app.db.Boolean())
    validade = app.db.Column(app.db.String())

    def __init__(self, entidade_id, nome_acao, imagem_acao, url_acao, descricao, contato, tipo_ajuda, forma_ajuda, data_insercao, data_atualizacao, forma_verificacao, resp_verificacao, ativa, permanente, validade):
        self.entidade_id = entidade_id
        self.nome_acao = nome_acao
        self.imagem_acao = imagem_acao
        self.url_acao = url_acao
        self.descricao = descricao
        self.contato = contato
        self.tipo_ajuda = tipo_ajuda
        self.forma_ajuda = forma_ajuda
        self.data_insercao = data_insercao
        self.data_atualizacao = data_atualizacao
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
