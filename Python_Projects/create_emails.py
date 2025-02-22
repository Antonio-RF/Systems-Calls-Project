tamanho_arquivo = 50000

texto_base = "This is a test that I will encrypt in PGP"

repeticoes = tamanho_arquivo // len(texto_base)
resto = tamanho_arquivo % len(texto_base)

conteudo = (texto_base * repeticoes) + texto_base[:resto]

with open("/home/toninho/Documents/Systems-Calls-Project/Dates/sendmail/email8.txt", "w") as arquivo:
    arquivo.write(conteudo)

lista = []















print("Success!")