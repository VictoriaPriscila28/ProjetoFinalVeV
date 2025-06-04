# features/listagem_busca_pessoa.feature
# language: pt
Funcionalidade: Listagem e Busca de Pessoa
  Como um usuário do sistema
  Eu quero poder listar e buscar pessoas
  Para visualizar e encontrar informações de contato rapidamente

  Cenário: LP01 - Visualizar a listagem de todas as pessoas cadastradas
    Dado que as seguintes pessoas estão cadastradas:
      | nome        | idade | email                     |
      | João Silva  | 30    | joao.silva@example.com    |
      | Maria Souza | 25    | maria.souza@example.com   |
      | Carlos Lima | 40    | carlos.lima@example.com   |
    Quando eu acesso a página de listagem de pessoas
    Então eu devo ver a pessoa "João Silva" na listagem
    E eu devo ver a pessoa "Maria Souza" na listagem
    E eu devo ver a pessoa "Carlos Lima" na listagem

  Cenário: BP01 - Buscar pessoa por nome com sucesso
    Dado que as seguintes pessoas estão cadastradas:
      | nome         | idade | email                     |
      | Carlos Lima  | 40    | carlos.lima@example.com   |
      | Fernanda Luz | 33    | fernanda.luz@example.com  |
    E eu acesso a página de busca de pessoas
    Quando eu preencho o campo "termo de busca" com "Carlos Lima"
    E eu clico no botão "Buscar"
    Então eu devo ver apenas a pessoa "Carlos Lima" nos resultados
    E eu não devo ver a pessoa "Fernanda Luz" nos resultados

  Cenário: BP02 - Buscar pessoa por nome que não existe
    Dado que eu acesso a página de busca de pessoas
    Quando eu preencho o campo "termo de busca" com "Pessoa Inexistente"
    E eu clico no botão "Buscar"
    Então eu devo ver a mensagem "Nenhuma pessoa encontrada."
    E eu não devo ver nenhuma pessoa nos resultados
