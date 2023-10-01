print('Atividade 1')
print('')

def leNota(n):
  notas = []
  for i in range(n):
    dado = float(input('Digite a nota: '))
    notas.append(dado)
  return notas

def calculaMedia(notas):
  soma = 0 
  for i in range(len(notas)):
    soma = soma + notas[i]
  return(soma/len(notas))

print('Bem vindo ao programa de cálculo de médias')
n1 = int(input('Digite o número de notas a serem calculadas: '))
notas = leNota(n1)
print('As notas são:' , notas)
media = calculaMedia(notas)
print('A média é:', media)

################################################ Atividade 2

print('')
print('--------------------')
print('')
print('Atividade 2')
print('')

nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
media = (nota1 + nota2)//2
if media == 10:
  print('Aprovado com Distinção.')
elif media >= 7:
  print('Aprovado.')
else:
  print('Reprovado.')

###########################

print('')
print('--------------------')
print('')
print('Atividade 3')
print('')

s = (float(input('Qual o salário por hora? ')))
h = (float(input('Quantas horas você trabalha por mês? ')))
salb = (s*h)

####Desconto IR
if salb <= 900:
  print('Isento')
elif salb <= 1500:
  irr = salb * 0.05
  porc = ('5%')
elif salb <= 2500:
  irr = salb * 0.1
  porc = ('10%')
elif salb > 2500:
  irr = salb * 0.2
  porc = ('20%')
##################

inss = salb * 0.1
fgts = salb * 0.11
print('')
print('Salário bruto igual a: R$', salb)
print('(-) IR', porc, ': R$', irr)
print('(-) INSS 10%: R$', inss)
print('FGTS 11%: R$', fgts)
print('Total de Descontos: R$' , (irr + inss))
print('Salário Liquido: R$', (salb - irr - inss))

############################################## Atividade 4

print('')
print('--------------------')
print('')
print('Atividade 4')
print('')

file1 = 4.90
alca1 = 5.90
pic1 = 6.90

file2 = 5.80
alca2 = 6.80
pic2 = 7.80

print('Seja bem-vindo ao Hipermercado Tabajara!')
print('As opções de carne são: File Duplo, Alcatra e Picanha. ')
print('')
tipo = (input('Qual o tipo de carne você deseja? ').lower())
kg = float(input('Quantos quilos de carne você deseja? '))
print('') 
print('Então você deseja', kg, 'quilos de', tipo,'.')

##########Carnes
if tipo == ('file duplo'):
  if kg < 5:
    total = file1 * kg
    print('Valor total:' , total , 'kg')
  elif kg > 5:
    total = file2 * kg
    print('Valor total:' , total , 'kg')
################
elif tipo == ('file'):
  if kg < 5:
    total = file1 * kg
    print('Valor total:' , total , 'kg')
  elif kg > 5:
    total = file2 * kg
    print('Valor total:' , total , 'kg')
################
elif tipo == ('alcatra'):
  if kg < 5:
    total = alca1 * kg
    print('Valor total:' , total , 'kg')
  elif kg > 5:
    total = alca2 * kg
    print('Valor total:' , total , 'kg')
################
elif tipo == ('picanha'):
  if kg < 5:
    total = pic1 * kg
    print('Valor total:' , total , 'kg')
  elif kg > 5:
    total = pic2 * kg
    print('Valor total:' , total , 'kg')
else:
  print('Desculpe, não entendi.')
#################

pag = (input('Você possui o cartão Tabajara? (s/n) ').lower())
if pag == ('s'):
  print('Você possui um desconto de 5%: R$' , total * 0.05)
  print('Valor a pagar: R$' , total-(total*0.05))
else:
  print('Ok.')
  print('Valor a pagar: R$' , total)

################################################ Atividade 6

print('')
print('--------------------')
print('')
print('*****Atividade 5 se encontra no final.')

print('')
print('--------------------')
print('')
print('Atividade 6')
print('')

divida = float(input('Qual a divida? '))
parc = int(input('Em quantas parcelas você deseja pagar? '))
print('')
if parc == 1:
  juros = 0
elif parc == 3:
  juros = 0.1
elif parc == 6:
  juros = 0.15
elif parc == 9:
  juros = 0.2
elif parc == 12:
  juros = 0.25
else:
  print('Valor de parcela inválido.')
valf = divida+(divida*juros)
print('Valor da divida: R$', valf)
print('Valor dos juros: ', divida*juros)
print('Quantidade de parcelas:', parc, 'Parcelas')
print('Valor da parcela: R$', valf/parc)

############################################# Atividade 7

print('')
print('--------------------')
print('')
print('Atividade 7')
print('')

print('Bem-vindo ao Restaurante!')
print('')
print('Cardápio:')
print('--------------------------------')
print('Cachorro Quente / #100 /R$ 1,20')
print('Bauru Simples / #101 /R$ 1,30')
print('Bauru com ovo / #102 /R$ 1,50')
print('Hambúrguer / #103 /R$ 1,20')
print('Cheeseburguer / #104 /R$ 1,30')
print('Refrigerante / #105 /R$ 1,00')
print('')

cardapio = {
    '100': 1.2,
    '101': 1.3,
    '102': 1.5,
    '103': 1.2,
    '104': 1.3,
    '105': 1.0,
}

custo_total = 0
produtos = {}

while True:
    codigo = input("Qual é o código do produto? ")
    if codigo not in cardapio:
        print("Código inválido. Tente novamente.")
        continue
    preco = cardapio[codigo]
    unidades = int(input("Quantas unidades? "))
    custo = preco * unidades
    custo_total += custo

    if codigo not in produtos:
            produtos[codigo] = {"quantidade": unidades, "custo": custo}
    else:
            produtos[codigo]["quantidade"] += unidades
            produtos[codigo]["custo"] += custo

    print('')
    mais_pedidos = input('Quer pedir mais alguma coisa? (s/n) ')
    if mais_pedidos.lower() != "s":
        break

for codigo, info in produtos.items():
    quantidade = info["quantidade"]
    custo = info["custo"]
    preco_unitario = cardapio[codigo]
    print('')
    print(quantidade, 'unidades do produto', codigo, 'custaram R$',custo)
print('')
print('O custo total é R$',custo_total)

############################################# Atividade 5

print('')
print('--------------------')
print('')
print('Atividade 5')
print('')

while True:
  soma = 0
  count = 1
  total = []
  valores = float
  while valores != 0:
    valores = float(input('Digite o valor do item: '))
    total.append(valores)
  for val in total:
    if val != 0:
      print('Produto ',count,': R$', val)
      soma += val
      count += 1
  pagamento = float(input('Quanto vai pagar em dinheiro?\n '))
  print('')
  print('Lojas Tabajara')
  print('Total: R$',soma)
  print('Dinheiro: R$',pagamento)
  if pagamento - soma > 0:
    print('Troco: R$',pagamento - soma)
  else:
    print('Valor insuficiente.')
  print('')
  print('---------------------')
  print('')
