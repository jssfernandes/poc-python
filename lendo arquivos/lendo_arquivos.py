# usado muito para arquivos
# sem with
arquivo = open("pessoas.txt", 'w')
# se der um bug na linha do write, ou em qualquer linha antes do close, vai dar problemas caso esqueça de fechar
arquivo.write("11,Lonna,Lawry,llawrya@yahoo.com")
arquivo.close()


# com with
# aqui, o with já lida com o abrir e fechar do arquivo, então ele não dá problemas caso esqueça de fechar
with open("pessoas.txt", 'w') as arquivo:
    arquivo.write("11,Lonna,Lawry,llawrya@yahoo.com")


# pode usar para ler tb, sem problemas
with open("pessoas.txt", 'r') as arquivo:
    print(arquivo.read())