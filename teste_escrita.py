#arquivo teste_escrita.py
arquivo = open('teste.txt', 'a')
arquivo.write('Python rocks \n')
print arquivo.mode
arquivo.close()