# -*- coding: UTF-8 -*-

#erros.py

with open("perfis.csv") as arquivo:
    for linha in arquivo:
        print linha

'''
#Não podemos nos esquecer de importar o módulo models
from models import *
try:
    arquivo = open('perfis.csv','r')
    valores = arquivo.readline().split(':') #deve ser virgula, para simular o problema
    Perfil(*valores)
    arquivo.close()


#except IOError as erro:
    #print('Deu IOError %s' % erro)

#except TypeError as erro:
    #print('Deu TypeError %s' % erro)


except (IOError,TypeError) as erro:
    print('Deu Error %s' % erro)

finally:
    if(arquivo is not None):
        print('fechando arquivo')
        arquivo.close()
'''