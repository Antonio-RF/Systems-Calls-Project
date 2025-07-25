import re
# Recebendo o texto inteiro ao dar Strace.
'''
def separator(entradas):
    nomes = re.findall(r'(\w+)\s*\(', entradas)

    #tirando nomes desnecessários:
    for word in nomes:
        if word.isupper():
            nomes.remove(word)


    return nomes
'''
entradas = []
while (True):
    string = str(input())
    if string == "":
        break
    entradas.append(string)

resultado = []
for line in entradas:
    #conferindo se os elementos de entradas realmente contém a estrutura de um System Call ('chamada()')
    eh_system_call = False
    if '(' in line and ')' in line:
        eh_system_call = True
    if eh_system_call:    
        interesse = line.split("(", 1)[0]
        resultado.append(interesse)

print(";".join(resultado))
