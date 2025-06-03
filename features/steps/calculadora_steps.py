from behave import given, when, then
from src.calculadora import Calculadora

@given('que eu tenho os números {num1:g} e {num2:g}') # Usar :g para float/int
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('eu somo estes números')
def step_impl(context):
    context.resultado = Calculadora.somar(context.num1, context.num2)

@when('eu subtraio estes números')
def step_impl(context):
    context.resultado = Calculadora.subtrair(context.num1, context.num2)

@when('eu multiplico estes números')
def step_impl(context):
    context.resultado = Calculadora.multiplicar(context.num1, context.num2)

@when('eu divido estes números')
def step_impl(context):
    context.resultado = Calculadora.dividir(context.num1, context.num2)

@then('o resultado deve ser {esperado}') # Não especificar tipo para lidar com string de erro
def step_impl(context, esperado):
    # Tenta converter o 'esperado' para float se não for a string de erro
    if isinstance(context.resultado, str) and "Erro" in context.resultado:
        assert context.resultado == esperado, f"Esperado: '{esperado}', Obtido: '{context.resultado}'"
    else:
        try:
            esperado_num = float(esperado)
            assert context.resultado == esperado_num, f"Esperado: {esperado_num}, Obtido: {context.resultado}"
        except ValueError:
            # Caso o 'esperado' seja uma string mas o resultado não seja o erro esperado
            assert False, f"Esperado um valor numérico mas obteve '{context.resultado}'"