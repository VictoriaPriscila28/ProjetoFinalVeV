# features/atualizacao_exclusao_pessoa.feature
# language: pt
Funcionalidade: Atualização e Exclusão de Pessoa
  Como um usuário do sistema
  Eu quero poder atualizar e excluir pessoas
  Para manter as informações de contato precisas e atualizadas

  Scenario: AP01 - Atualizar dados de uma pessoa com sucesso
    Given que a pessoa "atualizar.teste@example.com" com nome "Teste Atualiza" e idade "20" está cadastrada
    When eu acesso a página de edição da pessoa "Teste Atualiza"
    And eu preencho o campo "nome" com "Teste Atualizado"
    And eu preencho o campo "idade" com "21"
    And eu preencho o campo "email" com "atualizado.teste@example.com"
    And eu clico no botão "Salvar Alterações"
    Then a pessoa "Teste Atualizado" deve ser atualizada com sucesso
    And eu devo ver a mensagem "Pessoa atualizada com sucesso!"
    And a pessoa "Teste Atualizado" deve aparecer na listagem de pessoas
    And a pessoa "Teste Atualiza" não deve aparecer na listagem de pessoas

  Scenario: AP02 - Tentativa de atualização de e-mail para um já existente
    Given que as seguintes pessoas estão cadastradas:
      | nome        | idade | email                     |
      | Ana Silva   | 28    | ana.silva@example.com     |
      | Bruno Souza | 35    | bruno.souza@example.com   |
    When eu acesso a página de edição da pessoa "Ana Silva"
    And eu preencho o campo "email" com "bruno.souza@example.com"
    And eu clico no botão "Salvar Alterações"
    Then a pessoa "Ana Silva" não deve ser atualizada
    And eu devo ver a mensagem de erro "Novo e-mail já cadastrado por outra pessoa."
    And a pessoa "Ana Silva" deve manter o e-mail "ana.silva@example.com" na listagem

  Scenario: EP01 - Excluir uma pessoa com sucesso
    Given que a pessoa "excluir.teste@example.com" com nome "Teste Exclui" e idade "30" está cadastrada
    When eu acesso a página de listagem de pessoas
    And eu clico no botão "Excluir" para a pessoa "Teste Exclui"
    And eu confirmo a exclusão
    Then a pessoa "Teste Exclui" deve ser removida com sucesso
    And eu devo ver a mensagem "Pessoa excluída com sucesso!"
    And a pessoa "Teste Exclui" não deve aparecer na listagem de pessoas

  Scenario: EP02 - Tentativa de exclusão de pessoa inexistente (não visível)
    Given que eu acesso a página de listagem de pessoas
    When eu tento excluir uma pessoa com o e-mail "nao.existe@example.com"
    Then a pessoa não deve ser removida
    And eu devo ver a mensagem de erro "Pessoa não encontrada para exclusão."
