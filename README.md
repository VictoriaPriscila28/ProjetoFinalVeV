# Projeto de Testes de Aceitação com BDD (Behave) - Calculadora e CRUD de Pessoa

## 📄 Sobre o Projeto

Este repositório contém um projeto de testes de aceitação desenvolvido utilizando a metodologia **Behavior-Driven Development (BDD)** e a ferramenta **Behave** em Python. O objetivo principal foi demonstrar a aplicação de testes de aceitação para validar o comportamento de funcionalidades de software a partir da perspectiva do usuário e do negócio.

O projeto abrange a automação de testes para duas áreas distintas:
1.  **Calculadora Simples:** Validação das operações matemáticas básicas (soma, subtração, multiplicação e divisão), incluindo cenários de sucesso e tratamento de exceções (como divisão por zero).
2.  **Sistema de Gerenciamento de Pessoas (CRUD - Create, Read, Update, Delete):** Testes das funcionalidades de cadastro, listagem, busca, atualização e exclusão de registros de pessoas, simulando interações com um sistema web.

## 🎯 Objetivo

* Compreender e aplicar os princípios do BDD.
* Escrever cenários de teste claros e legíveis em Gherkin.
* Implementar a automação de testes utilizando o framework Behave.
* Validar o comportamento de funcionalidades essenciais de software.
* Documentar todo o processo de teste, desde a concepção dos cenários até a análise dos resultados.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Behave:** Framework BDD para Python.
* **Gherkin:** Linguagem de descrição de comportamento.
* **Spacy:** Biblioteca para processamento de linguagem natural (PLN) em português (usado indiretamente no mock do sistema, se houvesse campos de texto mais complexos no CRUD, mas mantido para compatibilidade).
* **Bibliotecas Auxiliares:** `requests`, `gnews` (apenas para contexto de projeto maior, não essencial para o Behave CRUD), `pandas`, `numpy`, `matplotlib`, `seaborn`, `sentence-transformers`, `bertopic`, `joblib` (estas últimas para o contexto de projeto de ML, não diretamente para o Behave CRUD, mas podem ter sido instaladas no mesmo ambiente).

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar os testes de aceitação.

### Pré-requisitos

* Python 3.x instalado.
* `pip` (gerenciador de pacotes do Python).

### 1. Clonar o Repositório

bash

git clone <https://github.com/VictoriaPriscila28/ProjetoFinalVeV.git>
cd <ProjetoFinalVeV> 

### 2. Configurar o ambiente virtual
python -m venv venv
### No Windows:
.\venv\Scripts\activate
### No macOS/Linux:
source venv/bin/activate

### 3. Baixar as dependências

pip install behave # Essencial para rodar os testes

### Instalações adicionais para os módulos mockados do sistema (calculadora, sistema_web)

pip install spacy
python -m spacy download pt_core_news_sm # Para o spacy, se usado em algum mock

### 4. Executar os testes
python -m behave