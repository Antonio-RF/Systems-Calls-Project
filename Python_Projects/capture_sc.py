import subprocess
import random
from separator import separator

# Adicionando meus diretórios primários:
# "fake" é usado como diretório que não existe.
# "nothing" será usado como configuração para não ter nenhum caminho.
list_primary_directories = ["Desktop", "Documents", "Pictures", "Music", "Downloads", "Public", "Templates", "Videos", "snap", "fake", " "]
primary_directories = {
    "Documents": {},
    "Pictures": {},
    "Desktop": [],
    "Music": [],
    "Public": [],
    "Downloads": {},
    "Templates": [],
    "Videos": [],
    "snap": {},
    "fake": [],
    "": []
}

list_secundary_directories = ["Documents", "Pictures", "snap", "Downloads"]
# Adicionando caminhos secundários:
primary_directories["Documents"].update({
    "circuitos": [],
    "Rubiks05.github.io": [], 
    "Strong-Password-Generator": [], 
    "Computer-Science-Freshmen-at-UFPR": [], 
    "Scientific-Calculator": [], 
    "Sorting-and-Searching-Algorithms": [], 
    "The-Boys": [],
    "certificados_cursos": [],
    "Competitive-programming": [],
    "CTF": [],
})
primary_directories["Pictures"].update({
    "Images": [],
    "Screenshots": []
})
primary_directories["snap"].update({
    "firefox": [], 
    "snapd-desktop-integration": [], 
    "spotify": []
})
primary_directories["Downloads"].update({
    "coord.o": [], 
    "entrada2.txt": [], 
    "forrest-sense-of-self-1.pdf": [], 
    "Generator2.py": [], 
    "index.html": [], 
    "outfile.tga": [], 
    "testes": [], 
    "dark_room.png": [], 
    "entrada.txt": [], 
    "forrest-sense-of-self.pdf": [], 
    "Generator.py": [], 
    "main.py": [], 
    "strace_r.txt": [],
    "firefox": []
})

list_third_directories = ["circuitos", "Rubiks05.github.io", "Strong-Password-Generator", "certificados_cursos", "Competitive-programming", "CTF" ,"Computer-Science-Freshmen-at-UFPR", "Scientific-Calculator", "Sorting-and-Searching-Algorithms", "The-Boys", "Images", "Screenshots", "firefox", "snapd-desktop-integration", "spotify", "testes", "firefox"]
# Adicionando caminhos terciários:
primary_directories["Documents"]["circuitos"].extend(["trabalho_semaforos.md", "README.md", "imgs"])
primary_directories["Documents"]["Rubiks05.github.io"].extend(["Assets", "index.html", "LICENSE", "Script.js", "style.css", "fake"])
primary_directories["Documents"]["Strong-Password-Generator"].extend(["Comments.txt", "Generator.py", "Menu.txt", "README.md", "CONTRIBUTING.md", "Images", "passwords.txt", "fake"])
primary_directories["Documents"]["Computer-Science-Freshmen-at-UFPR"].extend(["README.md", "CI1055", "CI1068", "CM303", "CM310", "Images", "CI1056", "CI1210", "CM304", "CM311", "fake"])
primary_directories["Documents"]["Scientific-Calculator"].extend(["requirements.txt", "README.md", "main.py", "LICENSE"])
primary_directories["Documents"]["Sorting-and-Searching-Algorithms"].extend(["docs", "Logs", "'Relatório de ALG2.pdf'", "tp.c", "Images", "README.md", "tp", "tp.c.txt"])
primary_directories["Documents"]["The-Boys"].extend(["Images", "README.md", "theboys."])
primary_directories["Documents"]["certificados_cursos"].extend(["Python_Cybersecurity", "python_cybersecurity.jpg"])
primary_directories["Documents"]["Competitive-programming"].extend(["Bee-Crowd", "CodeForces", "LICENSE", "README.md", "fake"])
primary_directories["Documents"]["CTF"].extend(["Bandit"])
primary_directories["Pictures"]["Images"].extend(["grade-bcc.png", "fake"])
primary_directories["Pictures"]["Screenshots"].extend(["Opção2.png", "'picture1(strong-password).png'", "'Picture2(TheBoys).png'", "'Picture3(sorting&searching).png'", "'Picture4(strong-password).png'", "'Picture5(TheBoys).jpeg'", "Results_Attack1.png", "Results_IC.png", "Results..png", "Results.png", "'Screenshot from 2025-01-30 19-09-58.png'", "'Screenshot from 2025-02-01 15-40-57.png'", "'Screenshot from 2025-02-01 17-03-32.png'", "fake"])
primary_directories["snap"]["firefox"].extend(["3836", "common", "current"])
primary_directories["snap"]["snapd-desktop-integration"].extend(["253", "83", "common", "current"])
primary_directories["snap"]["spotify"].extend(["82", "common", "current"])
primary_directories["Downloads"]["testes"].extend(["entrada1.txt"])
primary_directories["Downloads"]["firefox"].extend(["application.ini", "browser", "crashreporter", "defaults", "dependentlibs.list", "firefox", "firefox-bin", "firefox-bin.sig", "firefox.sig", "fonts", "glxtest", "gmp-clearkey"])

list_documents = ["circuitos", "Rubiks05.github.io", "Strong-Password-Generator", "Computer-Science-Freshmen-at-UFPR", "Scientific-Calculator", "Sorting-and-Searching-Algorithms", "The-Boys"]
list_pictures = ["Images", "Screenshots"]
list_snap = ["firefox", "snapd-desktop-integration", "spotify"]
list_downloads = ["testes", "firefox", "coord.o", "entrada2.txt", "forrest-sense-of-self-1.pdf", "Generator2.py", "index.html", "outfile.tga", "dark_room.png", "entrada.txt", "forrest-sense-of-self.pdf", "Generator.py", "main.py", "strace_r.txt"]

#Opções que podem ser escolhidas com o comando x: 
ls_options = ["", "-a", "-l", "-R", "-i", "-lh", "-l", "-1", "-s", "-t", "/", "..", "-la", "-S", "*.txt", "*", "-R -l"]

resultado = []
comandos = []
for i in range(100):
    random_primary_directory = random.choice(list_primary_directories)

    there_isnt_more = False
    if random_primary_directory in list_secundary_directories:
        if random_primary_directory == "Documents":
            random_secundary_directory = random.choice(list_documents)
        if random_primary_directory == "Pictures":
            random_secundary_directory = random.choice(list_pictures)
        if random_primary_directory == "snap":
            random_secundary_directory = random.choice(list_snap)
        if random_primary_directory == "Downloads":
            random_secundary_directory = random.choice(list_downloads)
    else:
        there_isnt_more = True
    
    there_isnt_more2 = False
    if not there_isnt_more:
        if random_secundary_directory in list_third_directories:
            random_third_directory = random.choice(primary_directories[random_primary_directory][random_secundary_directory])
        else:
            there_isnt_more2 = True
    
    if there_isnt_more:
        if random_primary_directory == " ":
            path = ""
        else:
            path = "/"+random_primary_directory
    else:
        if there_isnt_more2:
            path = "/"+random_primary_directory+"/"+random_secundary_directory
        else:
            path = "/"+random_primary_directory+"/"+random_secundary_directory+"/"+random_third_directory
    
    option_ls = random.choice(ls_options)

    comando = "strace ls "+option_ls+" "+path
    comandos.append(comando)

    processo = subprocess.run(comando, shell=True, capture_output=True, text=True)

    resultado_preliminar = separator(processo.stderr)
    resultado.extend(resultado_preliminar)

with open('/home/toninho/Documents/Systems-Calls-Project/Dates/ls/date_ls.txt', 'w') as file1:
    file1.write(" ".join(resultado))

with open('/home/toninho/Documents/Systems-Calls-Project/Dates/ls/commands.txt', 'w') as file2:
    for i in range(len(comandos)):
        file2.write("{}. {}\n".format(i+1, comandos[i]))
