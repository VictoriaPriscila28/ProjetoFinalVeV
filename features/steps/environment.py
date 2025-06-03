# features/steps/environment.py
from src.sistema_web import SistemaWeb # Importa sua classe de simulação

def before_scenario(context, scenario):
    """
    Função executada ANTES de cada cenário.
    Aqui, resetamos o estado do nosso sistema simulado para garantir
    que cada cenário de teste seja independente dos outros.
    """
    SistemaWeb.reset()
    # Para a calculadora, não é necessário reset, pois ela é stateless.
    # if "Calculadora" not in scenario.feature.name: # Exemplo de condicional se houvessem mais resets
    #    SistemaWeb.reset()