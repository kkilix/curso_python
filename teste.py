# -*- coding: UTF-8 -*-

class Conta(object):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def calcular_imposto(self): 
        self.saldo = self.saldo * 0.10
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, titular, saldo, bonus):
        super(ContaCorrente, self).__init__(titular, saldo)
        self.bonus = bonus

    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + 20



'''
import re

regex_url = r'(.*/perfis/\d+/convidar$)'
existe = re.match(regex_url, 'http://django.com/perfis/123/convidar')
print existe.group()
'''


'''
resultados = re.findall(r'(\w+\d$)', 'rota66 88centavos Peer2Peer Python2')
print resultados

resultados = re.findall(r'(\w+\d\b)', 'rota66 88centavos Peer2Peer Python2')
print resultados

resultados = re.findall(r'(^\d\w+)', '88centavos Peer2Peer Python2 99taxi')
print resultados

resultados = re.findall(r'(\b\d\w+)', '88centavos Peer2Peer Python2 99taxi')
print resultados
'''

'''
#resultados = re.findall('([A-Za-z]y)','Python ou jython')
#resultados = re.findall('([A-Za-z]y[A-Za-z]+)','Python ou jython ou PyPy')
#resultados = re.findall('(\wy\w+)','Python ou jython ou PyPy')
resultados = re.findall('(\wy\w+)','Python3 ou jython2 ou PyPy')
print resultados

resultados = re.findall('(\wy\w+\d)','Python3 ou jython2 ou PyPy')
print resultados

resultados = re.findall('[A-Za-z]+\d?','Python3 ou jython ou PyPy44')
print resultados

resultados = re.findall(r'[fF]\w{6}','Nico Flavio Fabiana Romulo')
print resultados

resultado = re.match(r'^#','#comentarios começam com tralha')
print resultado.group()

resultado = re.match(r'.*br$','http://alura.com.br')
print resultado.group()
'''

'''
#resultado = re.match('[pP]y','Python')
#resultado = re.match('[A-Za-z]y','Python')
resultado = re.match('[A-Za-z]y','Python ou jython')
r = resultado.group()
print 'Resultado: %s' %(r)
'''

'''
frase = 'Eu amo Python'
print frase
if len(frase) > 10:
    if(frase == 'Eu amo Python'):
        print 'Eu tambem'
    else:
        print 'Ham?'
else:
    print 'Tamanho insuficiente'
'''

'''
frase = 'Python'
contador = 0
while(contador < len(frase)):
    print frase[contador]
    contador+=1
print 'FIM'
'''