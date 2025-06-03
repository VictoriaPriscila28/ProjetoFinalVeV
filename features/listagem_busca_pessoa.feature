# features/listagem_busca_pessoa.feature
# language: pt
Funcionalidade: Listagem e Busca de Pessoa
  Como um usuário do sistema
  Eu quero poder listar e buscar pessoas
  Para visualizar e encontrar informações de contato rapidamente

  Scenario: LP01 - Visualizar a listagem de todas as pessoas cadastradas
    Given que as seguintes pessoas estão cadastradas:
      | nome        | idade | email                     |
      | João Silva  | 30    | joao.silva@example.com    |
      | Maria Souza | 25    | maria.souza@example.com   |
      | Carlos Lima | 40    | carlos.lima@example.com   |
    When eu acesso a página de listagem de pessoas
    Then eu devo ver a pessoa "João Silva" na listagem
    And eu devo ver a pessoa "Maria Souza" na listagem
    And eu devo ver a pessoa "Carlos Lima" na listagem

  Scenario: BP01 - Buscar pessoa por nome com sucesso
    Given que as seguintes pessoas estão cadastradas:
      | nome        | idade | email                     |
      | Carlos Lima | 40    | carlos.lima@example.com   |
      | Fernanda Luz| 33    | fernanda.luz@example.com  |
    And eu acesso a página de busca de pessoas
    When eu preencho o campo "termo de busca" com "Carlos Lima"
    And eu clico no botão "Buscar"
    Then eu devo ver apenas a pessoa "Carlos Lima" nos resultados
    And eu não devo ver a pessoa "Fernanda Luz" nos resultados

  Scenario: BP02 - Buscar pessoa por nome que não existe
    Given que eu acesso a página de busca de pessoas
    When eu preencho o campo "termo de busca" com "Pessoa Inexistente"
    And eu clico no botão "Buscar"
    Then eu devo ver a mensagem "Nenhuma pessoa encontrada."
    And eu não devo ver nenhuma pessoa nos resultados