import subprocess
import random
from separator import separator

# Adicionando meus diretórios primários:
# "fake" é usado como diretório que não existe.
# "nothing" será usado como configuração para não ter nenhum caminho.
primary_directories = {}
list = ["Desktop", "Documents", "Pictures", "Music", "Downloads", "Public", "Templates", "Videos", "snap", "fake", "nothing"]
for i in list:
    primary_directories[i] = []

# Adicionando diferentes caminhos:
primary_directories["Documents"].extend(["circuitos", "Rubiks05.github.io", "Strong-Password-Generator", "Computer-Science-Freshmen-at-UFPR", "Scientific-Calculator", "Sorting-and-Searching-Algorithms", "The-Boys"])
primary_directories["Pictures"].extend(["Images", "Screenshots"])
primary_directories["snap"].extend(["firefox", "snapd-desktop-integration", "spotify"])
primary_directories["Downloads"].extend(["coord.o", "entrada2.txt", "forrest-sense-of-self-1.pdf", "Generator2.py", "index.html", "outfile.tga", "testes", "dark_room.png", "entrada.txt", "forrest-sense-of-self.pdf", "Generator.py", "main.py", "strace_r.txt"])

resultado = []
comandos = []
for i in range(1000):
    random_primary_directory = random.choice(list)

    there_isnt_more = False
    if len(primary_directories[random_primary_directory]) != 0:
        random_path = random.choice(primary_directories[random_primary_directory])
    else:
        there_isnt_more = True
    

    if not there_isnt_more:
        path = "/"+random_primary_directory+"/"+random_path
    else:
        #então nós queremos realmente que não seja nada.
        if random_primary_directory == "nothing":
            path = ""
        else:
            path = "/"+random_primary_directory

    comando = "strace mv "+path
    comandos.append(comando)

    processo = subprocess.run(comando, shell=True, capture_output=True, text=True)

    resultado_preliminar = separator(processo.stderr)
    resultado.extend(resultado_preliminar)

with open('/home/toninho/Documents/Systems-Calls-Project/Dates/mv/date_mv.txt', 'w') as file1:
    file1.write(" ".join(resultado))

with open('/home/toninho/Documents/Systems-Calls-Project/Dates/mv/commands.txt', 'w') as file2:
    for i in range(len(comandos)):
        file2.write("{}. {}\n".format(i+1, comandos[i]))

#print(resultado)
#print()
#print("-------------------------------------")
#print()
#print(comandos)