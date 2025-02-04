import re
# Recebendo o texto inteiro ao dar Strace.
def separator(entradas):
    nomes = re.findall(r'(\w+)\s*\(', entradas)

    #tirando nomes desnecessários:
    for word in nomes:
        if word.isupper():
            nomes.remove(word)


    return nomes

