import re

print("********* ------------------------------- *********")

print("Projeto Linguagem Formais e Automatos - Laboratório")

print("********* ------------------------------- *********")

'''variáveis'''

a = True
b = True
vetor = []
variavel = ""
alfabeto = []
regras_producao = []
variavel_inicial = ""
contador = 0
palavra_final = ""
sequencia_utilizada_usuario = []

regras = {
    "de": "",
    "para": ""
}

print("1 - Recebendo as VARIAVEIS\n")

while b:
    b = False
    while a:
        variavel = input("Digite a VARIÁVEL")
        vetor.append(variavel)
        continuar = input("Deseja continuar? (S/N):  \t")

        if continuar != "S":
            a = False

            '''Verificar se no array eu não tenho espaço em branco, já que isso tem q estar no alfabeto'''
            if len(vetor) <= 1:
                for valor in range(1, len(vetor) + 1, 1):
                    if vetor[valor - 1] == ' ':
                        vetor = []
                        a = True
                        b = True

a = True
continuar = ""


print("2 - Recebendo as ALFABETO\n")
while a:
    letra = input("Digite a letra do alfabeto: \t")
    alfabeto.append(letra)
    continuar = input("Deseja continuar? (S/N):  \t")

    if continuar != "S":
        a = False



#Receber as regras de produção
print("3 - Recebendo a REGRA DE PRODUCAO\n")

a = True
b = True

while a:
    de_variavel = input("Digite a variável a ser subtituida: \t")
    if de_variavel not in vetor:
        de_variavel = ""
    else:
        while b:
            regras["de"] = de_variavel
            para_variavel = input("Digite  valor a ser trocado: \t")
            for valor in range(1, len(vetor) + 1, 1):
                if re.search(para_variavel, str(valor)) is not None:
                    regras["de"] = ""
                    regras["para"] = ""
                else:
                    for valor in range(1, len(alfabeto) + 1, 1):
                        if re.search(para_variavel, str(valor)) is not None:
                            b = False

                        else:
                            regras["de"] = de_variavel
                            regras["para"] = para_variavel
                            regras_producao.append(regras)

            continuar = input("Deseja continuar? (S/N):  \t")

            if continuar != "S":
                a = False
                b = False



#Receber a variável inicial
a = True
b = True
print("4 - Recebendo a variável INICIAL\n")
while b:
    b = False
    a = True
    while a:
        variavel_inicial = input("Digite a variável Inicial: \t")

        if variavel_inicial not in vetor:
            a = False
            b = True
        else:
            a = False

#Receber a palavra a ser "encontrada" no fim

print("6 - Recebendo a palavra FINAL que deve ser encontrada\n")

a = True

while a:
    palavra_final = input("Digite a palavra a ser encontrada: \t")
    #Verifica se na palavra final tem alguma variável, se tiver pede para o usuário digitar novamente
    for valor in range(1, len(vetor) + 1, 1):
        if re.search(valor, palavra_final) is None:
            for valor in range(1, len(alfabeto) + 1, 1):
                if re.search(valor, str(alfabeto)) is None:
                    a = False
        else:
            a = True
            palavra_final = ""


#Iniciar os passos para encontrar a palavra final dada pelo Usuário

#Antes recebe a sequencia utilizada pelo usuário


