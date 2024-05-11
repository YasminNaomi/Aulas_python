while True:
    while True:
        p1p =  input("Escolha P para PAR ou I para ÍMPAR: ")
        if p1p == "P" or p1p == "I":
            break

    if p1p == "P":
        p2p = "I"
    else:
        p2p = "P"

    p1 = int(input("Digite seu número (jogador 1): "))
    p2 = int(input("Digite seu número (jogador 2): "))
    soma = p1 + p2

    print(f"A soma dos números é {soma}")

    if soma % 2 == 0:
        resultado = "P"
        print("O resultado é par")
    else:
        resultado = "I"
        print("O resultado é ímpar")

    if p1p == resultado:
        print("O jogador 1 é o vencedor")
    else:
        print("O jogador 2 é o vencedor")

    cod = input("Digite SAIR para sair ou qualquer tecla para continuar: ")
    if cod == "SAIR":
        break


#==========================================
lista1 = [1, 2, 3, 4, 5]
lista2 = ["M", "N", "I", 1, 2, 3, [4, 5]]

a = list("TEXTO")
print(a)
print(lista1[::2])
print(lista1[1::2])
print(lista1[0:3])
print(lista2[-7:-1])
print(lista1)
print(type(lista1))
print(lista2)
print(type(lista2))
print(lista1[0])
print(lista2[2])
print(type(lista2[3]))
print(len(lista1))
print(len(lista2))

lista1.pop(0)
var = lista1.pop(0)
print(var)
print(lista1, "METODO POP")

# Declarando listas:
# a = list()
# a = []

animais = []
print(animais)
a = input("Digite o seu bicho de estimação: ")
animais.append(a)
print(animais)
animais.append("gato")
print(animais)
lista3 = ["felinos", "aves"]
animais.extend(lista3[0])
# animais.append(["a", "b"]) #inserir novos elementos
animais.extend(["a", "b"])
print(animais)
print([1, 2] + [3, 4])

x = [1, 2, 3, 4, 5]
y = x
x[0] = 0
print(x)
print(y)
# Apenas aponta para lista, não copia ela
# Para copiar, devemos usar o método .copy


quantidadeNotas = int(input("Escreva um número de notas a serem lidas: "))

for nota in range(quantidadeNotas):
    input(f"Digite a {nota + 1}° nota: ")
#=================================================
qprint(f'{horas:02d}:{minutos:02d}')uantidadeNotas = int(input("Escreva um número de notas a serem lidas: "))
notafinal = []
for i in range(quantidadeNotas):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    notafinal.append(nota)
print(notafinal)

soma = 0
for i in notafinal:
    print(f'nota: {i:}')
    soma += 1

print(f'A soma das notas é {soma}')
print(f'A media das notas é {soma/len(notafinal)}')
#===================================================

fila = []
while True:
    acao = input('Digite A para adicionar na fila ou R para remover da fila:')
    if acao == 'A':
        nome = input('Digite o nome da pessoa:')
        fila.append(nome)
    elif acao == 'R':
        rem = fila.pop(0)
        print(f'rem foi atendido')
        print(f'O tamanho da fila agora é de {len(fila)} pessoas.')
    else:
        print('Comando inválido')

    print(fila)
    enc = input('Deseja encerrar a fila? (S para encerrar)')

    if enc == 'S':
        break

print(fila)
#=====================================================

for horas in range(0, 24):
    for minutos in range(60):
        
