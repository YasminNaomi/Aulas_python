h= 100
l= 0
while l < h:
    l = l + 1
    print(l)

k= 100
p= 50
while p < k:
    p = p + 1
    print(p)

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        print("Você digitou 0. Saindo do programa.")
        break
    else:
        print("Você digitou:", numero)


def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

try:
    numero = int(input("Digite um número para exibir a tabuada: "))
    tabuada(numero)
except ValueError:
    print("Por favor, digite um número válido.")


numero = int(input("Digite um número:"))
v= numero
b= 1
while b <= v:
    if numero % 2 ==0:
        print(b, 'Número par')
    else:
        print(b, "Número impar")
    b= b + 1

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    if numero1 > numero2:
        maior = numero1
        menor = numero2
    else:
        maior = numero2
        menor = numero1
    
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
except ValueError:
    print("Por favor, digite números válidos.")
