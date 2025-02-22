import random

count = 9
while count<51:
#-------------------------------------------------------------------------------------------------------#
    # Criando uma lista de tamanhos que serão sortiados.
    # Coloquei a repetição do tamanho 50000 como metade do tamanho, prevalecendo o que o paper fez.
    # Exatamente a quantidade de diferentes tamanhos que o paper fez (12).
    list_sizes = [1, 10, 1000, 2000, 5000, 10000, 20000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 75000, 100000, 200000, 300000]
    tamanho_arquivo = random.choice(list_sizes)

#-------------------------------------------------------------------------------------------------------#
    # Construindo diferentes frases, igual o paper faz.
    list_aleatory_words = [
        "ocean", "mountain", "forest", "desert", "river", "valley", "island", "volcano", "glacier", "canyon", "comet", "nebula", "galaxy", "asteroid", "meteor", "constellation", "satellite", "blackhole", "supernova", "piano", "guitar", "violin", "trumpet", "flute", "drums", "cello", "saxophone", "harmonica", "xylophone", "wolf", "tiger", "eagle", "shark", "elephant", "dolphin", "panther", "octopus", "raven", "chameleon","sun", "moon", "star", "lightning", "rainbow", "hurricane", "tornado", "earthquake", "tsunami", "avalanche", "ruby", "emerald", "sapphire", "diamond", "topaz", "amethyst", "opal", "garnet", "pearl", "onyx", "rose", "tulip", "orchid", "sunflower", "lavender", "daisy", "lily", "cherryblossom", "jasmine", "violet", "castle", "tower", "bridge", "fortress", "lighthouse", "palace", "cottage", "cathedral", "pyramid", "labyrinth", "whisper", "echo", "silence", "melody", "harmony", "symphony", "rhapsody", "serenade", "ballad", "chant", "wizard", "sorcerer", "witch", "alchemist", "enchanter", "seer", "oracle", "druid", "warlock", "necromancer", "shadow", "phantom", "illusion", "mirage", "specter", "apparition", "shade", "wraith", "poltergeist", "entity","clock", "compass", "telescope", "microscope", "barometer", "thermometer", "sextant", "chronometer", "astrolabe", "pendulum"]

    texto_base = ""
    for i in range(10):
        texto_base = texto_base+random.choice(list_aleatory_words)
#-------------------------------------------------------------------------------------------------------#
    # Criando os arquivos e colocando ele na pasta do sendmail.
    repeticoes = tamanho_arquivo // len(texto_base)
    resto = tamanho_arquivo % len(texto_base)

    conteudo = (texto_base * repeticoes) + texto_base[:resto]

    email = f"email{count}.txt"

    with open(f"/home/toninho/Documents/Systems-Calls-Project/Dates/sendmail/emails/{email}", "w") as arquivo:
        arquivo.write(conteudo)

    count += 1


print("Success!")