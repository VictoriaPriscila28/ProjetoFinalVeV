# features/cadastro_pessoa.feature
# language: pt
Funcionalidade: Cadastro de Pessoa
  Como um usuário do sistema
  Eu quero poder cadastrar novas pessoas
  Para gerenciar meus contatos de forma eficiente

  Scenario: CP01 - Cadastro de pessoa com dados válidos
    Given que estou na página de cadastro de pessoas
    When eu preencho o campo "nome" com "Ana Clara"
    And eu preencho o campo "idade" com "28"
    And eu preencho o campo "email" com "ana.clara@example.com"
    And eu clico no botão "Salvar"
    Then a pessoa "Ana Clara" deve ser cadastrada com sucesso
    And eu devo ver a mensagem "Pessoa cadastrada com sucesso!"
    And a pessoa "Ana Clara" deve aparecer na listagem de pessoas

  Scenario: CP02 - Tentativa de cadastro com e-mail duplicado
    Given que a pessoa "usuario.existente@example.com" já está cadastrada
    And que estou na página de cadastro de pessoas
    When eu preencho o campo "nome" com "Novo Usuário"
    And eu preencho o campo "idade" com "35"
    And eu preencho o campo "email" com "usuario.existente@example.com"
    And eu clico no botão "Salvar"
    Then a pessoa não deve ser cadastrada
    And eu devo ver a mensagem de erro "E-mail já cadastrado."

  Scenario: CP03 - Tentativa de cadastro com campo obrigatório vazio (e-mail)
    Given que estou na página de cadastro de pessoas
    When eu preencho o campo "nome" com "Pedro"
    And eu preencho o campo "idade" com "22"
    And eu preencho o campo "email" com "" # Email vazio
    And eu clico no botão "Salvar"
    Then a pessoa não deve ser cadastrada
    And eu devo ver a mensagem de erro "Campo Nome e E-mail são obrigatórios."

  Scenario: CP04 - Tentativa de cadastro com campo obrigatório vazio (nome)
    Given que estou na página de cadastro de pessoas
    When eu preencho o campo "nome" com "" # Nome vazio
    And eu preencho o campo "idade" com "40"
    And eu preencho o campo "email" com "nome.vazio@example.com"
    And eu clico no botão "Salvar"
    Then a pessoa não deve ser cadastrada
    And eu devo ver a mensagem de erro "Campo Nome e E-mail são obrigatórios."