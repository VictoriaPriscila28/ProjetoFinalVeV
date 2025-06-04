# features/cadastro_pessoa.feature
# language: pt
Funcionalidade: Cadastro de Pessoa
  Como um usuário do sistema
  Eu quero poder cadastrar novas pessoas
  Para gerenciar meus contatos de forma eficiente

  Cenário: CP01 - Cadastro de pessoa com dados válidos
    Dado que estou na página de cadastro de pessoas
    Quando eu preencho o campo "nome" com "Ana Clara"
    E eu preencho o campo "idade" com "28"
    E eu preencho o campo "email" com "ana.clara@example.com"
    E eu clico no botão "Salvar"
    Então a pessoa "Ana Clara" deve ser cadastrada com sucesso
    E eu devo ver a mensagem "Pessoa cadastrada com sucesso!"
    E a pessoa "Ana Clara" deve aparecer na listagem de pessoas

  Cenário: CP02 - Tentativa de cadastro com e-mail duplicado
    Dado que a pessoa "usuario.existente@example.com" já está cadastrada
    E que estou na página de cadastro de pessoas
    Quando eu preencho o campo "nome" com "Novo Usuário"
    E eu preencho o campo "idade" com "35"
    E eu preencho o campo "email" com "usuario.existente@example.com"
    E eu clico no botão "Salvar"
    Então a pessoa não deve ser cadastrada
    E eu devo ver a mensagem de erro "E-mail já cadastrado."

  Cenário: CP03 - Tentativa de cadastro com campo obrigatório vazio (e-mail)
    Dado que estou na página de cadastro de pessoas
    Quando eu preencho o campo "nome" com "Pedro"
    E eu preencho o campo "idade" com "22"
    E eu preencho o campo "email" com "" # Email vazio
    E eu clico no botão "Salvar"
    Então a pessoa não deve ser cadastrada
    E eu devo ver a mensagem de erro "Campo Nome e E-mail são obrigatórios."

  Cenário: CP04 - Tentativa de cadastro com campo obrigatório vazio (nome)
    Dado que estou na página de cadastro de pessoas
    Quando eu preencho o campo "nome" com "" # Nome vazio
    E eu preencho o campo "idade" com "40"
    E eu preencho o campo "email" com "nome.vazio@example.com"
    E eu clico no botão "Salvar"
    Então a pessoa não deve ser cadastrada
    E eu devo ver a mensagem de erro "Campo Nome e E-mail são obrigatórios."
