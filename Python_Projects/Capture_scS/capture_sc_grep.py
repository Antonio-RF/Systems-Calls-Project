import subprocess
import random
from separator import separator

# Adicionando meus diretórios primários:
# "fake" é usado como diretório que não existe.
# "nothing" será usado como configuração para não ter nenhum caminho.
list_primary_directories = ["Desktop", "Documents", "Pictures", "Music", "Downloads", "Public", "Templates", "Videos", "snap", "fake", "Teste"]
primary_directories = {
    "Documents": {},
    "Pictures": {},
    "Desktop": {},
    "Music": {},
    "Public": {},
    "Downloads": {},
    "Templates": {},
    "Videos": {},
    "snap": {},
    "fake": {},
}

list_secundary_directories = ["Desktop", "Documents", "Pictures", "Music", "Downloads", "Public", "Templates", "Videos", "snap", "fake", "Teste"]
# Adicionando caminhos secundários:
primary_directories["Documents"].update({
    "Teste": [],
    "teste.txt": []
})
primary_directories["Pictures"].update({
    "Teste": [],
    "teste.txt": []
})
primary_directories["Desktop"].update({
    "Teste": [],
    "teste.txt": []
})
primary_directories["Music"].update({
    "Teste": [],
    "teste.txt": []
})
primary_directories["Public"].update({
    "Teste": [],
    "teste.txt": []
})
primary_directories["Downloads"].update({
    "Teste": [],
    "teste.txt": []
})
primary_directories["Templates"].update({
    "Teste": [],
    "teste.txt": []
})
primary_directories["Videos"].update({
    "Teste": [],
    "teste.txt": []
})
primary_directories["snap"].update({
    "Teste": [],
    "teste.txt": []
})

list_third_directories = ["Teste"]
# Adicionando caminhos terciários:
primary_directories["Documents"]["Teste"].extend(["teste.txt"])
primary_directories["Pictures"]["Teste"].extend(["teste.txt"])
primary_directories["Desktop"]["Teste"].extend(["teste.txt"])
primary_directories["Music"]["Teste"].extend(["teste.txt"])
primary_directories["Public"]["Teste"].extend(["teste.txt"])
primary_directories["Downloads"]["Teste"].extend(["teste.txt"])
primary_directories["Templates"]["Teste"].extend(["teste.txt"])
primary_directories["Videos"]["Teste"].extend(["teste.txt"])
primary_directories["snap"]["Teste"].extend(["teste.txt"])

list_ = ["teste.txt", ""]

#Opções que podem ser escolhidas com o comando x:
grep_options = ["", "-i", "-v", "-c", "-l", "-n", "-w", "-x", "-A", "-B", "-C"]
# Observação: deixei de colocar a opção '-r' pois dá muitos problemas, colocarei depois manualmente.
search_option = ["' '", '"a"', '"b"', '"c"', '"d"', '"e"', '"f"']
resultado = []
comandos = []
for i in range(10000):
    random_primary_directory = random.choice(list_primary_directories)

    there_isnt_more = False
    if random_primary_directory in list_secundary_directories:
        random_secundary_directory = random.choice(list_)
    else:
        there_isnt_more = True
    
    there_isnt_more2 = False
    if not there_isnt_more:
        if random_secundary_directory in list_third_directories:
            random_third_directory = random.choice(primary_directories[random_primary_directory][random_secundary_directory])
        else:
            there_isnt_more2 = True
    
    if there_isnt_more:
        if random_primary_directory == "":
            path = ""
        else:
            path = "/"+random_primary_directory
    else:
        if there_isnt_more2:
            path = "/"+random_primary_directory+"/"+random_secundary_directory
        else:
            path = "/"+random_primary_directory+"/"+random_secundary_directory+"/"+random_third_directory
    
    option_grep = random.choice(grep_options)
    option_search = random.choice(search_option)

    comando = "strace grep "+option_grep+" "+option_search+" "+path
    print("Esse é o comando: {}".format(comando))
    comandos.append(comando)

    processo = subprocess.run(comando, shell=True, capture_output=True, text=True)

    resultado_preliminar = separator(processo.stderr)
    resultado.extend(resultado_preliminar)


with open('/home/toninho/Documents/Systems-Calls-Project/Dates/grep/date_grep.txt', 'w') as file1:
    file1.write(" ".join(resultado))

with open('/home/toninho/Documents/Systems-Calls-Project/Dates/grep/commands.txt', 'w') as file2:
    for i in range(len(comandos)):
        file2.write("{}. {}\n".format(i+1, comandos[i]))