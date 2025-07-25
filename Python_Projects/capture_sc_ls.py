import subprocess
import random
from separator import separator

# Adicionando meus diretórios primários:
# "fake" é usado como diretório que não existe.
# "nothing" será usado como configuração para não ter nenhum caminho.
list_primary_directories = ["Desktop", "Documentos", "Imagens", "Músicas", "Downloads", "Public", "Templates", "Videos", "snap", "fake", " "]
primary_directories = {
    "Documentos": {},
    "Imagens": {},
    "Desktop": [],
    "Músicas": [],
    "Public": [],
    "Downloads": {},
    "Templates": [],
    "Videos": [],
    "snap": {},
    "fake": [],
    "": []
}

list_secundary_directories = ["Documentos", "Imagens", "snap", "Downloads"]
# Adicionando caminhos secundários:
primary_directories["Documentos"].update({
    "circuitos": [],
    "Antonio-RF.github.io": [], 
    "Strong-Password-Generator": [], 
    "Computer-Science-Freshmen-at-UFPR": [], 
    "Scientific-Calculator": [], 
    "Sorting-and-Searching-Algorithms": [], 
    "The-Boys": [],
    "certificados_cursos": [],
    "Competitive-programming": [],
    "Capture-The-Flag": [],
})
primary_directories["Imagens"].update({
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

list_third_directories = ["circuitos", "Antonio-RF.github.io", "Strong-Password-Generator", "certificados_cursos", "Competitive-programming", "Capture-The-Flag" ,"Computer-Science-Freshmen-at-UFPR", "Scientific-Calculator", "Sorting-and-Searching-Algorithms", "The-Boys", "Images", "Screenshots", "firefox", "snapd-desktop-integration", "spotify", "testes", "firefox"]
# Adicionando caminhos terciários:
primary_directories["Documentos"]["circuitos"].extend(["trabalho_semaforos.md", "README.md", "imgs"])
primary_directories["Documentos"]["Antonio-RF.github.io"].extend(["Assets", "index.html", "LICENSE", "Script.js", "style.css", "fake"])
primary_directories["Documentos"]["Strong-Password-Generator"].extend(["Comments.txt", "Generator.py", "Menu.txt", "README.md", "CONTRIBUTING.md", "Images", "passwords.txt", "fake"])
primary_directories["Documentos"]["Computer-Science-Freshmen-at-UFPR"].extend(["README.md", "CI1055", "CI1068", "CM303", "CM310", "Images", "CI1056", "CI1210", "CM304", "CM311", "fake"])
primary_directories["Documentos"]["Scientific-Calculator"].extend(["requirements.txt", "README.md", "main.py", "LICENSE"])
primary_directories["Documentos"]["Sorting-and-Searching-Algorithms"].extend(["docs", "Logs", "'Relatório de ALG2.pdf'", "tp.c", "Images", "README.md", "tp", "tp.c.txt"])
primary_directories["Documentos"]["The-Boys"].extend(["Images", "README.md", "theboys."])
primary_directories["Documentos"]["certificados_cursos"].extend(["Python_Cybersecurity", "python_cybersecurity.jpg"])
primary_directories["Documentos"]["Competitive-programming"].extend(["Bee-Crowd", "CodeForces", "LICENSE", "README.md", "fake"])
primary_directories["Documentos"]["Capture-The-Flag"].extend(["Bandit"])
primary_directories["Imagens"]["Images"].extend(["grade-bcc.png", "fake"])
primary_directories["Imagens"]["Screenshots"].extend(["Opção2.png", "'picture1(strong-password).png'", "'Picture2(TheBoys).png'", "'Picture3(sorting&searching).png'", "'Picture4(strong-password).png'", "'Picture5(TheBoys).jpeg'", "Results_Attack1.png", "Results_IC.png", "Results..png", "Results.png", "'Screenshot from 2025-01-30 19-09-58.png'", "'Screenshot from 2025-02-01 15-40-57.png'", "'Screenshot from 2025-02-01 17-03-32.png'", "fake"])
primary_directories["snap"]["firefox"].extend(["3836", "common", "current"])
primary_directories["snap"]["snapd-desktop-integration"].extend(["253", "83", "common", "current"])
primary_directories["snap"]["spotify"].extend(["82", "common", "current"])
primary_directories["Downloads"]["testes"].extend(["entrada1.txt"])
primary_directories["Downloads"]["firefox"].extend(["application.ini", "browser", "crashreporter", "defaults", "dependentlibs.list", "firefox", "firefox-bin", "firefox-bin.sig", "firefox.sig", "fonts", "glxtest", "gmp-clearkey"])

list_documents = ["circuitos", "Antonio-RF.github.io", "Strong-Password-Generator", "Computer-Science-Freshmen-at-UFPR", "Scientific-Calculator", "Sorting-and-Searching-Algorithms", "The-Boys"]
list_pictures = ["Images", "Screenshots"]
list_snap = ["firefox", "snapd-desktop-integration", "spotify"]
list_downloads = ["testes", "firefox", "coord.o", "entrada2.txt", "forrest-sense-of-self-1.pdf", "Generator2.py", "index.html", "outfile.tga", "dark_room.png", "entrada.txt", "forrest-sense-of-self.pdf", "Generator.py", "main.py", "strace_r.txt"]

#Opções que podem ser escolhidas com o comando x: 
ls_options = ["", "-a", "-l", "-i", "-lh", "-l", "-1", "-s", "-t", "/", "..", "-la", "-S", "*.txt", "*"]
resultado = []
linhas_resultado = []
comandos = []
for i in range(10000):
    random_primary_directory = random.choice(list_primary_directories)

    there_isnt_more = False
    if random_primary_directory in list_secundary_directories:
        if random_primary_directory == "Documentos":
            random_secundary_directory = random.choice(list_documents)
        if random_primary_directory == "Imagens":
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

    comando = "strace ls "+option_ls+" ~"+path
    print("Esse é o comando: {}".format(comando))
    comandos.append(comando)

    processo = subprocess.run(comando, shell=True, capture_output=True, text=True)

    resultado_preliminar = separator(processo.stderr)
    linha = "{}| {}".format(comando, ";".join(resultado_preliminar))
    linhas_resultado.append(linha)


with open('/home/toninhorf/Documentos/Systems-Calls-Project/Dates/ls/date_ls.txt', 'w') as file1:
    for linha in linhas_resultado:
        file1.write(linha + "\n")

with open('/home/toninhorf/Documentos/Systems-Calls-Project/Dates/ls/commands.txt', 'w') as file2:
    for i in range(len(comandos)):
        file2.write("{}. {}\n".format(i+1, comandos[i]))
