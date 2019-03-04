import re


print("********* ------------------------------- *********")

print("Projeto Linguagem Formais e Automatos - Laboratório")

print("********* ------------------------------- *********")

'''variáveis'''

a = False
b = True
vetor = []
variavel = ""
continuar = ""
alfabeto = []
regras_producao = []
variavel_inicial = ""
contador = 0
palavra_final = ""
sequencia_utilizada_usuario = []
concatenar = ""
tamanho_palavra = ""
contador = 0

regras = {
    "de": "",
    "para": ""
}


def valida_para(letra):

    if len(letra) == 1:
        if letra == "" or letra == " ":
            if len(concatenar) < 1:
                return False
            else:
                return True
        if str(letra).upper() in vetor or str(letra).lower() in alfabeto:
            return False
        else:
            print("\nValor digitado não foi encontrado nas Variáveis e nem no Alfabeto! Digite novamente!\n")
            return True

    else:
        print("Foi digitado mais que uma letra por vez. Digite novamente!\n")
        return True



'''Execução do programa'''

print("\n1 - Recebendo as VARIAVEIS\n")

while b:
    b = False
    a = False
    while not a:
        if b:
            b = False
            variavel = ""
            print("\nNão foi recebida nenhuma variável anteriormente, apenas um espao em branco. Digite novamente!\n")

        variavel = input("\nDigite a VARIÁVEL: \t").upper()

        '''Verificar se não está sendo recebido variáveis duplicadas'''
        if len(variavel) <= 1:
            if len(vetor) > 0:
                if variavel in vetor:
                    a = False
                    print("\nFoi detectado duplicidade nas letras das variáveis. Digite novamente!\n")

            if variavel != "" and variavel != " ":
                vetor.append(variavel.upper())
                continuar = input("\nDeseja continuar? (S/N):  \t").upper()

                if continuar != "S":
                    a = True

                    '''Verificar se no array eu não tenho espaço em branco, já que isso tem q estar no alfabeto'''
                    if len(vetor) > 0:
                        for valor in range(0, len(vetor), 1):
                            if vetor[valor] == "":
                                vetor.remove("")
                                print("\nEspaço em branco digitado removido...\n")
                                a = True
                                b = True
                            if vetor[valor] == ' ':
                                vetor.remove(" ")
                                print("\nEspaço em branco digitado removido...\n")
                                a = True
                                b = True
            else:
                print("\nEspaço em branco ou nulo digitado! Entrada não válida! Digite novamente!\n")
        else:
            print("Variável contem mais de uma letra! Digite novamente!\n")
            a = True
            b = True

a = True
continuar = ""


print("\n2 - Recebendo as ALFABETO\n")

while a:
    variavel = input("\nDigite a letra do alfabeto: \t")

    if len(variavel) <= 1:
        if len(alfabeto) > 0:
            '''Verificar se não está sendo recebido letras do alfabeto duplicadas'''
            if variavel in alfabeto:
                a = True
                print("\nFoi detctado duplicidade nas letras do alfabeto. Digite novamente!\n")
                variavel = ""

        if not (variavel == "" or variavel == " "):
            alfabeto.append(variavel.lower())
            continuar = input("\nDeseja continuar? (S/N):  \t").upper()

            if continuar != "S":
                a = False

            for valor in range(0, len(alfabeto), 1):
                if variavel in vetor:
                    a = True
                    print("\nFoi detectado uma das variáveis digitadas no passo 1. Digite novamente!\n")
                    alfabeto.remove(variavel)
                    valor = len(alfabeto)
        else:
            print("\nEspaço em branco ou nulo digitado. Entrada não é válida! Digite novamente!\n")
        if not a:
            print("\nFoi detectado espaco em branco ou vazio. Digite novamente!\n")
    else:
        print("\nLetra do alfabeto digitada contem mais de um caracter! Digite novamente!\n")

#Receber as regras de produção
print("\n3 - Recebendo a REGRA DE PRODUCAO\n")

a = True
b = True

while a:
    b = True
    de_variavel = input("\nDigite a variável a ser subtituida: \t").upper()

    if de_variavel not in vetor:
        print("\nNão foi encontrada a letra digitada nas Variáveis recebidas. Digite novamente!\t")
        de_variavel = ""
    else:
        # receber as letras de cada vez
        print("\n########## Por favor, será recebido uma letra de cada vez na regra para. ##########\n")
        print("\nA letra deve estar contida na variável ou alfabeto\n")
        print("Precione qualquer tecla para continuar.\n")
        #input()
        while b:
            regras["de"] = de_variavel
            a = False
            while not a:
                para_variavel = input("\nDigite  valor a ser trocado: \t")
                a = True
                a = valida_para(para_variavel)
                if not a:
                    a = False
                    concatenar += str(para_variavel)
                    print("\nLetra válida!\n")
                    if len(concatenar) == 1:
                        if concatenar == "" or concatenar == " ":
                            regras["de"] = de_variavel.upper()
                            regras["para"] = concatenar
                            regras_producao.append(regras)
                            a = True

                else:
                    a = False
                    regras["para"] = ""
                if not a:
                    continuar = input("\nDeseja continuar? (S/N):  \t").upper()

                    if continuar != "S":
                        if len(concatenar) < 1:
                            a = False
                        else:
                            if regras["para"] != "" or regras["para"] != " ":
                                regras["de"] = de_variavel.upper()
                                regras["para"] = concatenar
                                regras_producao.append(regras)
                                a = True
                            else:
                                a = False
                                print("Valor não pode conter letras e valor nulo. Ou não estar presente no alfabeto ou variáveis!. Digite novamente!\n")

            if len(concatenar) < 1:
                break
            continuar = input("\nDeseja adicionar outra REGRA DE PRODUÇÃO?\t").upper()
            concatenar = ""
            if continuar == "S":
                b = False
            else:
                b = False
                a = False


#Receber a variável inicial
a = True
b = True
print("\n4 - Recebendo a variável INICIAL\n")
while b:
    b = False
    a = True
    while a:
        variavel_inicial = input("\nDigite a variável Inicial: \t").upper()

        if variavel_inicial not in vetor:
            print("Variavel inicial não foi encontrada nas VARIÁVEIS! Digite novamente!\n")
            a = False
            b = True
        else:
            print("Variável válida! Continuando...")
            a = False

#Receber a palavra a ser "encontrada" no fim

print("\n6 - Recebendo a palavra FINAL que deve ser encontrada\n")

a = True
b = True

while b:
    b = False
    while a:
        palavra_final = input("\nDigite a palavra a ser encontrada: \t").lower()
        lista = list(palavra_final)
        #Verifica se na palavra final tem alguma variável, se tiver pede para o usuário digitar novamente
        for valor3 in range(0, len(lista), 1):
            if lista[valor3] not in alfabeto:
                contador += 1

        if contador == 0:
            a = False
            print("\nA palavra digitada pode ser formada pelo Alfabeto. Tudo ok. Continuando...")
        else:
            print("\nAlguma letra da palavra final não foi encontrada no alfabeto. Por favor, digite novamente!\n")
            a = True

#Iniciar os passos para encontrar a palavra final dada pelo Usuário

#Antes recebe a sequencia utilizada pelo usuário

print("\n7 - Recebendo a sequencia utilizada pelo usupario para chegar na resposta")

a = True
b = True

while b:
    b = False
    while a:
        sequencia_utilizada_usuario = input("\nDigite a sequencia utilizada para chegar na resposta: \t")
