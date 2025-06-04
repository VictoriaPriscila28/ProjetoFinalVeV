# features/steps/environment.py
from behave import given, when, then
from src.sistema_web import SistemaWeb # Importa sua classe de simulação

def before_scenario(context, scenario):
    """
    Função executada ANTES de cada cenário.
    Aqui, resetamos o estado do nosso sistema simulado para garantir
    que cada cenário de teste seja independente dos outros.
    """
    SistemaWeb.reset()
    # A Calculadora não precisa de reset, pois é stateless.
    # Se houvesse alguma configuração específica para a calculadora, ela seria removida aqui.