#import area
import os

""" # exercicio em aula

nomeArq = input('Digite o nome do arquivo: ')
arq = open(nomeArq, 'r')
c = arq.read(1)
while c:
    print(c)
    c = arq.read(1)
arq.close() 
"""

#lista 2
""" # exercicio 1 - r + eh pra ler e escrever 
nomeArq = input('Digite o nome do arquivo: ')
textoArq = input('Digite o texto do arquivo: ')
arq = open(nomeArq, 'r+')
arq.write(textoArq)
arq.close() 
"""

""" # exercicio 2 'rb' eh pra ler em modo binario
nomeArq = input('Digite o nome do arquivo: ')
arq = open(nomeArq, 'rb') 
tamArq = os.path.getsize(nomeArq)
#contar tamanho do arquivo
tamanho_bytes = os.path.getsize(nomeArq)
#contar linhas
num_linhas = 0
for linha in arq:
    num_linhas += 1

print(f"O arquivo '{nomeArq}' tem '{tamanho_bytes}' bytes e '{num_linhas}' linhas")
arq.close() """

""" # exercicio 3
nomeArq = input('Digite o nome do arquivo: ')
arq = open(nomeArq, 'r')
novoArq = open("ex3.txt", 'wb')
text = arq.read()
newText = ' '.join(text.split())
novoArq.write(newText.encode())
arq.close()
novoArq.close()
"""

""" # exercicio 4
nomeArq = input('Digite o nome do arquivo que deseja remover os comentários:')
arq = open(nomeArq, 'r')
novoArq = open("ex4.py", 'wb')
linhas = arq.readlines()
for linha in linhas:
    if linha[0] == '#':
        novoTexto = linha.replace(linha, " ")
        novoArq.write(novoTexto.encode())
    else:
        novoArq.write(linha.encode())
print("Comentários removidos!")
arq.close()
novoArq.close()
"""

""" # exercicio 4 melhorado
nome = input('Digite o nome do arquivo que deseja remover os comentários:')
ext = input('Informe a extensão do arquivo: (formato .ext)')
nomeArq = nome + ext
novoNome = input('Digite o nome do novo arquivo:')
novaExt = input('Informe a extensão desse arquivo: (formato .ext)')
novoArqNome = novoNome + '_semComentarios ' +novaExt
arq = open(nomeArq, 'r')
novoArq = open(novoArqNome, 'wb')
# novoArq = open("ex4.py", 'wb')
linhas = arq.readlines()
for linha in linhas:
    if linha[0] == '#' or linha[0] == '/':
        novoTexto = linha.replace(linha, " ")
        novoArq.write(novoTexto.encode())
    else:
        novoArq.write(linha.encode())
print("Comentários removidos!")
arq.close()
novoArq.close()
"""

""" # exercicio 5
nomeArq = input('Digite o nome do arquivo a ser alterado: ')
typeArq = input('Sentido da conversão: (digite L se for uma conversão Windows->Linux e W se for uma conversão Linux->Windows)')
arq = open(nomeArq, 'rb')
novoArq = open("ex5.txt", 'wb')
linhas = arq.readlines()
if typeArq == 'L' or typeArq == 'Linux':
    for linha in linhas:
        if linha[0] == '\r':
            novoTexto = linha.replace("\r", "\n")
            novoArq.write(novoTexto.encode())
        else:
            texto = linha.decode()
            novoArq.write(texto.encode())
elif typeArq == 'W' or typeArq == 'Windows':
    for linha in linhas:
        if linha[0] == '\n':
            novoTexto = linha.replace("\n", "\r\n")
            novoArq.write(novoTexto.encode())
        else:
            texto = linha.decode()
            novoArq.write(texto.encode())
print("Conversão completa!")
arq.close()
novoArq.close()
"""

# exercicio 6
numeros = []
i = 0
while i <= 9:
    numero = input("Informe um número")
    numeros.append(int(numero))
    i+=1
arq = open("ex6.txt", 'w')
for numero in numeros:
        numero_binario = bin(numero)
        if numero_binario[0] == '0' and numero_binario[1] == 'b':
            binario = numero_binario.replace("0b", "")
            arq.write(binario+"\n")
        else:
        arq.write(numero+"\n")
print("Conversão completa!")
arq.close()