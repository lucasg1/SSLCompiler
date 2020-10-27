# -*- coding: utf-8 -*-
import analiseLexica as lexica
import analiseSintatica as sintatica

# Os arquivos analiseLexica e analiseSintatica realizam as analises
# lexica e sintatica respectivamente
# Os outputs das analises podem ser visualizados apos a execucao desse codigo

nome_arquivo = 'codigo.ssl'

arq = open(nome_arquivo, 'r')
# lexica.openArq(arq)
lexica.analiseLexica(arq)
arq = open(nome_arquivo, 'r')
lexica.reiniciar(arq)
sintatica.parse(arq)

arq.close()