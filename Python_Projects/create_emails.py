tamanho_arquivo = 50000

texto_base = "This is a test writed only in ASCII!"

repeticoes = tamanho_arquivo // len(texto_base)
resto = tamanho_arquivo % len(texto_base)

conteudo = (texto_base * repeticoes) + texto_base[:resto]

with open("/home/toninho/Documents/Systems-Calls-Project/Dates/sendmail/email3.txt", "w") as arquivo:
    arquivo.write(conteudo)

print("Success!")