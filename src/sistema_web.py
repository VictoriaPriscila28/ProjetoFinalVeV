# src/sistema_web.py
class SistemaWeb:
    """
    Classe mock/simulada de um sistema web para gerenciamento de pessoas.
    Em um cenário real, isso interagiria com um banco de dados e renderizaria HTML.
    """
    _pessoas = {} # Dicionário para armazenar pessoas {email: {nome, idade, email}}
    _mensagens_sucesso = []
    _mensagens_erro = []
    _pagina_atual = ""
    _resultados_busca = []

    @classmethod
    def reset(cls):
        cls._pessoas = {}
        cls._mensagens_sucesso = []
        cls._mensagens_erro = []
        cls._pagina_atual = ""
        cls._resultados_busca = []

    @classmethod
    def acessar_pagina(cls, pagina):
        cls._pagina_atual = pagina
        cls._mensagens_sucesso = [] # Limpa mensagens ao mudar de página
        cls._mensagens_erro = []

    @classmethod
    def cadastrar_pessoa(cls, nome, idade, email):
        if not nome or not email:
            cls._mensagens_erro.append("Campo Nome e E-mail são obrigatórios.")
            return False
        if email in cls._pessoas:
            cls._mensagens_erro.append("E-mail já cadastrado.")
            return False
        cls._pessoas[email] = {"nome": nome, "idade": idade, "email": email}
        cls._mensagens_sucesso.append("Pessoa cadastrada com sucesso!")
        return True

    @classmethod
    def listar_pessoas(cls):
        cls.acessar_pagina("listagem")
        return list(cls._pessoas.values())

    @classmethod
    def buscar_pessoa_por_nome(cls, termo_busca):
        cls.acessar_pagina("busca")
        cls._resultados_busca = [
            p for p in cls._pessoas.values()
            if termo_busca.lower() in p["nome"].lower()
        ]
        if not cls._resultados_busca:
            cls._mensagens_erro.append("Nenhuma pessoa encontrada.")
        return cls._resultados_busca

    @classmethod
    def obter_pessoa_por_email(cls, email):
        return cls._pessoas.get(email)

    @classmethod
    def atualizar_pessoa(cls, email_original, nome, idade, email_novo):
        if not nome or not email_novo:
            cls._mensagens_erro.append("Campo Nome e E-mail são obrigatórios.")
            return False

        if email_original not in cls._pessoas:
            cls._mensagens_erro.append("Pessoa não encontrada para atualização.")
            return False

        if email_novo != email_original and email_novo in cls._pessoas:
            cls._mensagens_erro.append("Novo e-mail já cadastrado por outra pessoa.")
            return False

        pessoa_original = cls._pessoas.pop(email_original) # Remove a original
        cls._pessoas[email_novo] = {"nome": nome, "idade": idade, "email": email_novo} # Adiciona a nova
        cls._mensagens_sucesso.append("Pessoa atualizada com sucesso!")
        return True

    @classmethod
    def excluir_pessoa(cls, email):
        if email in cls._pessoas:
            del cls._pessoas[email]
            cls._mensagens_sucesso.append("Pessoa excluída com sucesso!")
            return True
        cls._mensagens_erro.append("Pessoa não encontrada para exclusão.")
        return False

    @classmethod
    def verificar_mensagem_sucesso(cls, mensagem):
        return mensagem in cls._mensagens_sucesso

    @classmethod
    def verificar_mensagem_erro(cls, mensagem):
        return mensagem in cls._mensagens_erro

    @classmethod
    def pessoa_existe_na_listagem(cls, nome_pessoa):
        return any(p['nome'] == nome_pessoa for p in cls.listar_pessoas())