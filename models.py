# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0 #self._Perfil__curtidas

    def imprimir(self):
        print "Nome : %s, Telefone: %s, Empresa: %s, Curtidas: %s" %(self.nome, self.telefone, self.empresa, self.__curtidas)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    '''@classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo,'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis'''

    '''@classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo,'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')

            #novo
            if(len(valores) is not 3):
                raise ValueError('Uma linha no arquivo deve ter 3 valores')

            perfis.append(classe(*valores))
        arquivo.close()
        return perfis


class Perfil_Vip(Perfil):
    'Classe padrão para perfis de usuários VIPs'

    def __init__(self, nome, telefone, empresa, apelido=''):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0'''

    @staticmethod
    def gerar_perfis(nome_arquivo):
        arquivo = open(nome_arquivo,'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            if(len(valores) is not 3):
                raise Perfil_Error('Uma linha no arquivo deve ter 3 valores') #lançando Perfil_Error
            perfis.append(Perfil(*valores))
        arquivo.close()
        return perfis


class Perfil_Error(Exception):
    def __init(self, mensagem):
        self.mensagem = mensagem

    def __str__(self):
        return repr(self.mensagem)

'''
class Data(object):
    'Classe para formatar datas'

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime(self):
        print "%s/%s/%s" %(self.dia, self.mes, self.ano)


class Pessoa(object):

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprime_imc(self):
        imc = self.peso / (self.altura **2)
        print "Imc de %s: %s" %(self.nome, imc)
'''