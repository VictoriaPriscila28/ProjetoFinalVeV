# language: pt
Funcionalidade: Calculadora
  Como um usuário
  Eu quero realizar operações matemáticas básicas
  Para obter resultados corretos e precisos

  Cenário: Soma de dois números inteiros
    Dado que eu tenho os números 5 e 3
    Quando eu somo estes números
    Então o resultado deve ser 8

  Cenário: Soma de um número positivo e um número negativo
    Dado que eu tenho os números 10 e -4
    Quando eu somo estes números
    Então o resultado deve ser 6

  Cenário: Subtração de dois números inteiros
    Dado que eu tenho os números 10 e 4
    Quando eu subtraio estes números
    Então o resultado deve ser 6

  Cenário: Subtração que resulta em número negativo
    Dado que eu tenho os números 5 e 12
    Quando eu subtraio estes números
    Então o resultado deve ser -7

  Cenário: Multiplicação de dois números inteiros
    Dado que eu tenho os números 6 e 7
    Quando eu multiplico estes números
    Então o resultado deve ser 42

  Cenário: Multiplicação por zero
    Dado que eu tenho os números 9 e 0
    Quando eu multiplico estes números
    Então o resultado deve ser 0

  Cenário: Divisão de dois números inteiros
    Dado que eu tenho os números 15 e 3
    Quando eu divido estes números
    Então o resultado deve ser 5.0

  Cenário: Divisão por zero (cenário de erro)
    Dado que eu tenho os números 10 e 0
    Quando eu divido estes números
    Então o resultado deve ser Erro: Divisão por zero

  Cenário: Divisão que resulta em decimal
    Dado que eu tenho os números 7 e 2
    Quando eu divido estes números
    Então o resultado deve ser 3.5
