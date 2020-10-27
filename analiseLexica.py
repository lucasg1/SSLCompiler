# -*- coding: utf-8 -*-
# Esse codigo foi desenvolvido seguindo os passos da apostila de Compiladores - Turma IME 2020

import string
import alfabeto

tokens_stack=[] # pilha de tokens do arquivo de entrada
LINHAS=[] # ordem das linhas dos tokens para encontrar o erro futuramente
Erro = False
nextChar = "" # Próx char do arquivo
arq = None # Variavel que ira ter o codigo do programa a ser analisado

def searchKeyWord(nome): 
    # Retorna token de PALAVRAS RESERVADAS ou token do identificador - ID
    # uma busca binaria eh executada para encontrar a palavra
    esquerda=0
    direita=len(alfabeto.palavras_reservadas) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if alfabeto.palavras_reservadas[meio] == nome:
            return meio # encontrou a palavra reservada, retorna ela
        elif alfabeto.palavras_reservadas[meio] > nome:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return alfabeto.ID #retornar id?

# Ao receber o token ID da função searchKeyWord() 
# e concluir que uma palavra não é reservada,
# o Analisador Léxico deve determinar o seu token secundário
Identificadores = {}
cont = 0
def searchName(nome): 
    # Adiciona os identificadores num formato Hash juntamente com token secundario.
    # O token secundário é a ordem do identificador no texto, sendo considerado a primeira aparição apenas.
    global cont
    global Identificadores
    if nome not in Identificadores.keys():
        Identificadores[nome] = cont
        cont = cont + 1
        return cont
    if nome in Identificadores.keys():
        return Identificadores[nome]
vConsts = []
nNumConsts = 0

def addConst(s):
    # Adiciona os literais do programa, que representam as constantes da linguagem. Estão associados aos tokens CHARACTER, NUMERAL E STRINGVAL.
    # O token secundário é a ordem que foram adicionadas.
    vConsts.append(s)
    return len(vConsts)-1

def getConst(tokenSec):
    # Retorna a constante de token secundário tokenSec
    return vConsts[tokenSec]

# Automato
def isspace(n):
    # Pula os separadores
    if n in [chr(10), chr(13)," ", "\t", "\v", "\f"]:
        return True
    return False

def isalpha(n):
    # Verifica se eh um caracter ASCII
    if n in string.ascii_letters:
        return True
    return False

def isdigit(n):
    # Verifica se eh um digito
    if n in "0123456789":
        return True
    return False

global tokenSecundario
tokenSecundario=None
linha = 1
ch=1

def nextToken():
    # Retorna o token lido e suas variáveis token principal e secundária
    global nextChar
    global ch
    global linha
    global arq
    global tokenSecundario
    global Identificadores
    separador=""

    while(isspace(nextChar)):

        if (nextChar == "\n") or (nextChar == "\r"):
            linha+=1

        nextChar=arq.read(1)
        ch+=1

    if (nextChar==""):
            token=alfabeto.EOF

    elif (isalpha(nextChar)):
        textAux=[]

        while(isalpha(nextChar) or nextChar == '_'):
            textAux.append(nextChar)
            nextChar=arq.read(1)
            ch+=1

        text=separador.join(textAux)
        # print('token atual: ', text)
        
        token = searchKeyWord(text) # retorna a palavra reservada ou "alfabeto.ID"
        
        if(token==alfabeto.ID):
            tokenSecundario = searchName(text)
            # tokenSecundario = addConst(text)
            # if(text in Identificadores):
                # print('ja tinha um id e retornei' , Identificadores[text])
                
                # return Identificadores[text]
            # else:
            # print('token secundario = ', tokenSecundario)


    elif (isdigit(nextChar)):
        numeralAux=[]

        while(isdigit(nextChar)):
            numeralAux.append(nextChar)
            nextChar=arq.read(1)
            ch+=1
        numeral=separador.join(numeralAux)
        token = alfabeto.NUMERAL
        tokenSecundario = addConst(numeral)

    elif (nextChar=="\""):
        stringAux=[]
        stringAux.append(nextChar)
        nextChar=arq.read(1)
        ch+=1
        if(nextChar!="\""):
            while(nextChar!="\""):
                stringAux.append(nextChar)
                nextChar=arq.read(1)
                ch+=1

        stringAux.append(nextChar)
        nextChar=arq.read(1)
        ch+=1
        string=separador.join(stringAux)
        token = alfabeto.STRING
        # print('the string is ', string)
        # print('token secundario = ', tokenSecundario)
        tokenSecundario = addConst(string)

    else:
        if(nextChar=="\'"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.CHARACTER
            # print('the char is ', nextChar)
            # print('token secundario = ', tokenSecundario)
            tokenSecundario=addConst(nextChar)
            nextChar=arq.read(2) 
            ch+=2

        elif(nextChar==":"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.COLON

        elif(nextChar=="+"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="+"):
                token=alfabeto.PLUS_PLUS
                nextChar=arq.read(1)
                ch+=1
            else:
                token=alfabeto.PLUS

        elif(nextChar=="-"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="-"):
                token=alfabeto.MINUS_MINUS
                nextChar=arq.read(1)
                ch+=1

            else:
                token=MINUS

        elif(nextChar==";"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.SEMI_COLON

        elif(nextChar==","):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.COMMA

        elif(nextChar=="="):
            nextChar=arq.read(1)
            ch+=1

            if(nextChar=="="):
                token=alfabeto.EQUAL_EQUAL
                nextChar=arq.read(1)
                ch+=1

            else:
                token=alfabeto.EQUALS

        elif(nextChar=="["):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.LEFT_SQUARE

        elif(nextChar=="]"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.RIGHT_SQUARE

        elif(nextChar=="{"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.LEFT_BRACES

        elif(nextChar=="}"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.RIGHT_BRACES

        elif(nextChar=="("):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.LEFT_PARENTHESIS

        elif(nextChar==")"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.RIGHT_PARENTHESIS

        elif(nextChar=="&"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="&"):
                nextChar=arq.read(1)
                ch+=1
                token=alfabeto.AND
            else:
                token=alfabeto.UNKNOWN

        elif(nextChar=="|"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar=="|"):
                nextChar=arq.read(1)
                ch+=1
                token=alfabeto.OR
            else:
                token=alfabeto.UNKNOWN

        elif(nextChar=="<"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar)=="=":
                token=alfabeto.LESS_OR_EQUAL
                nextChar=arq.read(1)
                ch+=1
            else:
                token=alfabeto.LESS_THAN

        elif(nextChar==">"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar)=="=":
                token=alfabeto.GREATER_OR_EQUAL
                nextChar=arq.read(1)
                ch+=1
            else:
                token=alfabeto.GREATER_THAN

        elif(nextChar=="!"):
            nextChar=arq.read(1)
            ch+=1
            if(nextChar)=="=":
                token=alfabeto.NOT_EQUAL
                nextChar=arq.read(1)
                ch+=1
            else:
                token=NOT 

        elif(nextChar=="*"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.TIMES

        elif(nextChar=="."):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.DOT        

        elif(nextChar=="/"):
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.DIVIDE

        else:
            nextChar=arq.read(1)
            ch+=1
            token=alfabeto.UNKNOWN

    return token

def printSingleToken(token):
    if token < 18:
        print(alfabeto.palavras_reservadas[token])
    elif token < 44:
        print(alfabeto.simbolos[token-18])
    elif token < 48:
        print(alfabeto.tokens_regulares[token-44])
    elif token == 48:
        print('unknown')
    elif token == 49:
        print('eof')

def printTokens(tokens_stack):
    pilha = []

    for token in tokens_stack:
        if token < 18:
            pilha.append(alfabeto.palavras_reservadas[token])
        elif token < 44:
            pilha.append(alfabeto.simbolos[token-18])
        elif token < 48:
            pilha.append(alfabeto.tokens_regulares[token-44])
        elif token == 48:
            pilha.append('unknown')
        elif token == 49:
            pilha.append('eof')
            print('A pilha de tokens do codigo em anexo é dada por: ')
            print(pilha)

def openArq(arquivo):
    global arq
    global nextChar
    arq = arquivo
    nextChar = arq.read(1)

def reiniciar(arquivo):
    global arq
    global Identificadores
    global cont
    global vConsts
    global nNumConsts
    global tokenSecundario
    global linha
    global ch
    global tokens_stack
    global Erro
    arq.close()
    Identificadores = {}
    cont = 0
    vConsts = []
    nNumConsts = 0
    tokenSecundario=None
    linha = 1
    ch=1
    tokens_stack=[] # pilha de tokens do arquivo de entrada
    Erro = False

    arq = arquivo

def analiseLexica(arquivo):
    global Erro
    global arq
    global nextChar
    global tokens_stack
    global LINHAS

    arq=arquivo
    nextChar = arq.read(1)
    tokenAux=nextToken()

    while (tokenAux != alfabeto.EOF):
        tokens_stack.append(tokenAux)
        LINHAS.append(linha)
        if(tokenAux == alfabeto.UNKNOWN):
            # print("Caractere "+str(ch+1)+" não esperado na linha " + str(linha))
            Erro=True
        tokenAux=nextToken()
    tokens_stack.append(tokenAux)
    LINHAS.append(linha)

    ### printTokens(tokens_stack) Printa os ids dos tokens
    ### Faz a mudança entre numero dos tokens e o nome deles para output na tela

    # printTokens(tokens_stack)
    # print(vConsts)


    # if (not Erro):
    #     print ("Nenhum erro léxico foi encontrado.")

# arq = open('codigo.ssl', 'r')
# analiseLexica(arq)
