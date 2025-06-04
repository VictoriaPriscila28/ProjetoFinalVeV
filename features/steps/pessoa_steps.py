# features/steps/pessoa_steps.py
from behave import given, when, then, step_matcher
from src.sistema_web import SistemaWeb

# Define o matcher de passos como "re" (expressão regular)
step_matcher("re")

# --- GIVENS ---
# Padrões para given genéricos:
@given('que estou na página de cadastro de pessoas')
def step_impl(context):
    SistemaWeb.acessar_pagina("cadastro")
    context.form_data = {} # Limpa dados do formulário para o cenário

@given('que a pessoa "(?P<email>.*)" já está cadastrada')
def step_impl(context, email):
    SistemaWeb.cadastrar_pessoa(f"Usuario Existente {email.split('@')[0]}", 99, email)
    SistemaWeb.acessar_pagina("cadastro")
    context.form_data = {}

# CORREÇÃO CRUCIAL AQUI: Ajuste da regex para dado com tabela
# O Behave, com step_matcher("re"), espera que você defina a regex exata para a frase.
# O ': ' (dois pontos e espaço) no final do Gherkin é importante.
@given('que as seguintes pessoas estão cadastradas:')
def step_impl(context):
    for row in context.table:
        SistemaWeb.cadastrar_pessoa(row['nome'], int(row['idade']), row['email'])

# CORREÇÃO CRUCIAL AQUI: Ajuste da regex para given sem parâmetro
@given('que eu acesso a página de busca de pessoas')
def step_impl(context):
    SistemaWeb.acessar_pagina("busca")
    context.form_data = {}

# CORREÇÃO CRUCIAL AQUI: Ajuste da regex para given sem parâmetro
@given('que eu acesso a página de listagem de pessoas')
def step_impl(context):
    SistemaWeb.acessar_pagina("listagem")

@given('que a pessoa "(?P<email>.*)" com nome "(?P<nome>.*)" e idade "(?P<idade>\d+)" está cadastrada')
def step_impl(context, email, nome, idade):
    SistemaWeb.cadastrar_pessoa(nome, int(idade), email)


# --- WHENS ---
# Este passo já deve funcionar com strings vazias porque '.*' captura qualquer caractere 0 ou mais vezes
@when('eu preencho o campo "(?P<campo>.*)" com "(?P<valor>.*)"')
def step_impl(context, campo, valor):
    if not hasattr(context, 'form_data'):
        context.form_data = {}
    context.form_data[campo] = valor

@when('eu clico no botão "([^"]+)"') # Este já estava correto para botões simples
def step_impl(context, botao_nome):
    if botao_nome == "Salvar":
        SistemaWeb.cadastrar_pessoa(
            context.form_data.get("nome"),
            int(context.form_data.get("idade")) if context.form_data.get("idade") else None,
            context.form_data.get("email")
        )
    elif botao_nome == "Salvar Alterações":
        SistemaWeb.atualizar_pessoa(
            context.pessoa_email_original,
            context.form_data.get("nome"),
            int(context.form_data.get("idade")) if context.form_data.get("idade") else None,
            context.form_data.get("email")
        )
    elif botao_nome == "Buscar":
        SistemaWeb.buscar_pessoa_por_nome(context.form_data.get("termo de busca"))
    else:
        raise NotImplementedError(f'Botão "{botao_nome}" não implementado neste passo ou é ambíguo. Verifique os cenários ou defina um passo mais específico no .feature.')


# Este passo já estava correto, é um 'when' que também define uma página.
@when('eu acesso a página de listagem de pessoas')
def step_impl(context):
    SistemaWeb.acessar_pagina("listagem")

@when('eu acesso a página de edição da pessoa "(?P<nome_pessoa>.*)"')
def step_impl(context, nome_pessoa):
    pessoa = next((p for p in SistemaWeb.listar_pessoas() if p['nome'] == nome_pessoa), None)
    if pessoa:
        SistemaWeb.acessar_pagina("edicao")
        context.pessoa_email_original = pessoa['email']
        context.form_data = {"nome": pessoa['nome'], "idade": str(pessoa['idade']), "email": pessoa['email']}
    else:
        raise Exception(f"Pessoa '{nome_pessoa}' não encontrada para edição.")

@when('eu clico no botão "Excluir" para a pessoa "(?P<nome_pessoa>.*)"')
def step_impl(context, nome_pessoa):
    pessoa = next((p for p in SistemaWeb.listar_pessoas() if p['nome'] == nome_pessoa), None)
    if pessoa:
        context.pessoa_email_para_excluir = pessoa['email']
    else:
        raise Exception(f"Pessoa '{nome_pessoa}' não encontrada na listagem para exclusão.")

@when('eu confirmo a exclusão')
def step_impl(context):
    if hasattr(context, 'pessoa_email_para_excluir'):
        SistemaWeb.excluir_pessoa(context.pessoa_email_para_excluir)
    else:
        raise Exception("Nenhuma pessoa foi marcada para exclusão antes da confirmação.")

@when('eu tento excluir uma pessoa com o e-mail "(?P<email>.*)"')
def step_impl(context, email):
    SistemaWeb.excluir_pessoa(email)


# --- THENS ---
@then('a pessoa "(?P<nome>.*)" deve ser cadastrada com sucesso')
def step_impl(context, nome):
    assert SistemaWeb.pessoa_existe_na_listagem(nome), f"A pessoa '{nome}' não foi encontrada na listagem após o cadastro."

# AJUSTE NA VERIFICAÇÃO DE MENSAGENS PARA SER MAIS FLEXÍVEL
@then('eu devo ver a mensagem "(?P<mensagem>.*)"')
def step_impl(context, mensagem):
    # Verifica se a mensagem está entre as mensagens de sucesso OU de erro
    # Isso cobre cenários onde a mensagem esperada é de erro mas o THEN genérico é 'eu devo ver a mensagem'
    assert SistemaWeb.verificar_mensagem_sucesso(mensagem) or SistemaWeb.verificar_mensagem_erro(mensagem), \
        f"Mensagem esperada '{mensagem}' não foi exibida. Mensagens de sucesso: {SistemaWeb._mensagens_sucesso}, Mensagens de erro: {SistemaWeb._mensagens_erro}"


@then('a pessoa "(?P<nome>.*)" deve aparecer na listagem de pessoas')
def step_impl(context, nome):
    assert SistemaWeb.pessoa_existe_na_listagem(nome), f"A pessoa '{nome}' não apareceu na listagem."

@then('a pessoa não deve ser cadastrada')
def step_impl(context):
    # Garante que houve uma mensagem de erro e NENHUMA de sucesso
    assert SistemaWeb._mensagens_erro, "Nenhuma mensagem de erro foi exibida, mas o cadastro deveria ter falhado."
    assert not SistemaWeb.verificar_mensagem_sucesso("Pessoa cadastrada com sucesso!"), "Mensagem de sucesso foi exibida indevidamente."

@then('eu devo ver a mensagem de erro "(?P<mensagem>.*)"')
def step_impl(context, mensagem):
    assert SistemaWeb.verificar_mensagem_erro(mensagem), f"Mensagem de erro esperada '{mensagem}' não foi exibida. Mensagens atuais: {SistemaWeb._mensagens_erro}"

@then('eu devo ver a pessoa "(?P<nome_pessoa>.*)" na listagem')
def step_impl(context, nome_pessoa):
    assert SistemaWeb.pessoa_existe_na_listagem(nome_pessoa), f"Pessoa '{nome_pessoa}' não encontrada na listagem."

@then('eu devo ver apenas a pessoa "(?P<nome_pessoa>.*)" nos resultados')
def step_impl(context, nome_pessoa):
    assert len(SistemaWeb._resultados_busca) == 1, f"Esperado 1 resultado, mas encontrei {len(SistemaWeb._resultados_busca)}."
    assert SistemaWeb._resultados_busca[0]['nome'] == nome_pessoa, f"O resultado da busca não é '{nome_pessoa}'."

@then('eu não devo ver a pessoa "(?P<nome_pessoa>.*)" nos resultados')
def step_impl(context, nome_pessoa):
    assert not any(p['nome'] == nome_pessoa for p in SistemaWeb._resultados_busca), f"A pessoa '{nome_pessoa}' foi encontrada nos resultados inesperadamente."

@then('a pessoa "(?P<nome>.*)" deve ser atualizada com sucesso')
def step_impl(context, nome):
    assert SistemaWeb.pessoa_existe_na_listagem(nome), f"A pessoa '{nome}' não foi encontrada com os dados atualizados."

@then('a pessoa "(?P<nome_pessoa>.*)" não deve aparecer na listagem de pessoas')
def step_impl(context, nome_pessoa):
    assert not SistemaWeb.pessoa_existe_na_listagem(nome_pessoa), f"A pessoa '{nome_pessoa}' ainda aparece na listagem inesperadamente."

@then('a pessoa "(?P<nome>.*)" deve ser removida com sucesso')
def step_impl(context, nome):
    assert not SistemaWeb.pessoa_existe_na_listagem(nome), f"A pessoa '{nome}' ainda está na listagem após a remoção."

@then('a pessoa não deve ser removida')
def step_impl(context):
    assert SistemaWeb._mensagens_erro, "Nenhuma mensagem de erro foi exibida, mas a pessoa não deveria ter sido removida."
    assert not SistemaWeb.verificar_mensagem_sucesso("Pessoa excluída com sucesso!"), "Mensagem de sucesso foi exibida indevidamente na tentativa de exclusão."

@then('eu não devo ver nenhuma pessoa nos resultados')
def step_impl(context):
    assert not SistemaWeb._resultados_busca, "Resultados da busca não estão vazios como esperado."

@then('a pessoa "(?P<nome_pessoa>.*)" não deve ser atualizada')
def step_impl(context, nome_pessoa):
    assert SistemaWeb._mensagens_erro, "Nenhuma mensagem de erro foi exibida, mas a pessoa não deveria ter sido atualizada."
    assert not SistemaWeb.verificar_mensagem_sucesso("Pessoa atualizada com sucesso!"), "Mensagem de sucesso exibida indevidamente."

@then('a pessoa "(?P<nome_pessoa>.*)" deve manter o e-mail "(?P<email_original>.*)" na listagem')
def step_impl(context, nome_pessoa, email_original):
    pessoa = SistemaWeb.obter_pessoa_por_email(email_original)
    assert pessoa and pessoa['nome'] == nome_pessoa, f"A pessoa '{nome_pessoa}' não manteve o e-mail '{email_original}'."
    assert not SistemaWeb.verificar_mensagem_sucesso("Pessoa atualizada com sucesso!"), "Mensagem de sucesso exibida indevidamente."