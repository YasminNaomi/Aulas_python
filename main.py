nome = 'Maria'
idade = 25
salario = 4650.37
msg = '%s tem %d e ganha R$%.2f' % (nome, idade, salario)
print(msg)

msg2 = '{:-^20s} tem {} anos e ganha R${:.2f}'.format(nome, idade, salario)
print(msg2)


msg3 = f'{nome:*^15s} tem {idade} anos e ganha R${salario:.1f}'
print(msg3)
i = 0
j = 10 
n = 0 
while i <j:
    i = i + 1
    j = j - 1
    n = n+1
print(i)

a = 10
k = 0
while k < a:
    a = a - 1
    print(a)

print("Fogo, Feliz ano novo!")

Numero = int(input("Digite um numero:"))

v = Numero
b = 1
while b <= v:
    if b % 2 == 0:
        print(b, "é par")
    else:
        print(b, "é impar")
    b = b + 1

n1 = int(input("digite o primeiro numero do inervalo:"))
n2 = int(input("digite o segundo numero do intervalo:"))
soma = 0
while n1 <= n2:
    if n1 % 2 == 0:
        soma = soma + n1
    n1 = n1 + 1
print(soma)

f = int(input("digite a quantidade de notas a serem digitadas:"))
r = 1
somato = 0
while r <= f:
    valor = float(input(f'digite a nota {r}: '))
    r = r + 1
    somato = somato + valor
media = somato / n
print(f'a media das notas e {media:.2f}')

if media >= 6:
    print('Você passou de ano, parabens')
else:
    print('Você não passou de ano.')

depositoinicial = float(input("Qual o valor do seu deposito:"))
taxadejuros = float(input("Qual a taxa de juros:"))
depositomensal = float(input("Qual é o seu deposito mensal:"))
periodo = int(input("Quanto tempo pretende manter em meses:"))

tempo = 0
juros = depositoinicial* (taxadejuros/100)
deposito = 0 
while tempo <= periodo:
    print(depositoinicial)
    depositoinicial = depositoinicial + juros + deposito
    deposito = deposito + depositomensal
    tempo = tempo + 1
