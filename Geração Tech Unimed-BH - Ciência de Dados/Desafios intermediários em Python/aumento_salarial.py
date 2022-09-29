# A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

# Salário	Percentual de Reajuste
# 0 - 600.00            17%
# 600.01 - 900.00       13%
# 900.01 - 1500.00      12%
# 1500.01 - 2000.00     10%
# Acima de 2000.00      5%


## Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

## A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais.


# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)
salario = int(input()) 

if (salario >= 0 and salario <= 600):
  novo_salario = salario * 1.17 
elif (salario >= 600.01 and salario <= 900):
  novo_salario = salario * 1.13
elif (salario >= 900.01 and salario <= 1500):
  novo_salario = salario * 1.12
elif (salario >= 1500.01 and salario <= 2000  ):
  novo_salario = salario * 1.10  
else:
  novo_salario = salario * 1.05
  
reajuste = novo_salario - salario
percentual = reajuste*100/salario
print(f"Novo salario: {novo_salario:.2f}\n Reajuste ganho: {reajuste:.2f}\n Em percentual: {percentual:.0f} %")

