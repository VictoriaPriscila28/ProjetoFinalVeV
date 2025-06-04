# language: pt
Funcionalidade: Atualização e Exclusão de Pessoa
  Como um usuário do sistema
  Eu quero poder atualizar e excluir pessoas
  Para manter as informações de contato precisas e atualizadas

  Cenário: AP01 - Atualizar dados de uma pessoa com sucesso
    Dado que a pessoa "atualizar.teste@example.com" com nome "Teste Atualiza" e idade "20" está cadastrada
    Quando eu acesso a página de edição da pessoa "Teste Atualiza"
    E eu preencho o campo "nome" com "Teste Atualizado"
    E eu preencho o campo "idade" com "21"
    E eu preencho o campo "email" com "atualizado.teste@example.com"
    E eu clico no botão "Salvar Alterações"
    Então a pessoa "Teste Atualizado" deve ser atualizada com sucesso
    E eu devo ver a mensagem "Pessoa atualizada com sucesso!"
    E a pessoa "Teste Atualizado" deve aparecer na listagem de pessoas
    E a pessoa "Teste Atualiza" não deve aparecer na listagem de pessoas
