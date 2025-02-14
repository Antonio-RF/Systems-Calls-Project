import subprocess
import random
from separator import separator

# Adicionando meus diretórios primários:
# "fake" é usado como diretório que não existe.
# "nothing" será usado como configuração para não ter nenhum caminho.
list_primary_directories = ["Desktop", "Documents", "Pictures", "Music", "Downloads", "Public", "Templates", "Videos", "snap", "fake", "Teste", ""]
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
    "": {}
}

list_secundary_directories = ["Desktop", "Documents", "Pictures", "Music", "Downloads", "Public", "Templates", "Videos", "snap", "fake", "Teste", ""]
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
primary_directories[""].update({
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
primary_directories[""]["Teste"].extend(["teste.txt"])

list_ = ["teste.txt", ""]

#Opções que podem ser escolhidas com o comando x: 
mv_options = ["", "-i", "-f", "-n", "-u", "-v"]
resultado = []
comandos = []
for i in range(10):
    random_primary_directory1 = random.choice(list_primary_directories)
    random_primary_directory2 = random.choice(list_primary_directories)

    there_isnt_more = False
    if random_primary_directory1 in list_secundary_directories:
        random_secundary_directory1 = random.choice(list_)
        random_secundary_directory2 = random.choice(list_)
    else:
        there_isnt_more = True
    
    there_isnt_more2 = False
    if not there_isnt_more:
        if random_secundary_directory1 in list_third_directories:
            random_third_directory1 = random.choice(primary_directories[random_primary_directory1][random_secundary_directory1])
            random_third_directory2 = random.choice(primary_directories[random_primary_directory2][random_secundary_directory2])
        else:
            there_isnt_more2 = True
    
    if there_isnt_more:
        if random_primary_directory1 == " ":
            path1 = ""
            path2 = ""
        else:
            path1 = "/"+random_primary_directory1
            path2 = "/"+random_primary_directory2
    else:
        if there_isnt_more2:
            path1 = "/"+random_primary_directory1+"/"+random_secundary_directory1
            path2 = "/"+random_primary_directory2+"/"+random_secundary_directory2
        else:
            path1 = "/"+random_primary_directory1+"/"+random_secundary_directory1+"/"+random_third_directory1
            path2 = "/"+random_primary_directory2+"/"+random_secundary_directory2+"/"+random_third_directory2
    
    option_mv = random.choice(mv_options)

    comando = "strace mv "+option_mv+" "+path1+" "+path2
    print("Esse é o comando: {}".format(comando))
    comandos.append(comando)

    processo = subprocess.run(comando, shell=True, capture_output=True, text=True)

    resultado_preliminar = separator(processo.stderr)
    resultado.extend(resultado_preliminar)


with open('/home/toninho/Documents/Systems-Calls-Project/Dates/mv/date_mv.txt', 'w') as file1:
    file1.write(" ".join(resultado))

with open('/home/toninho/Documents/Systems-Calls-Project/Dates/mv/commands.txt', 'w') as file2:
    for i in range(len(comandos)):
        file2.write("{}. {}\n".format(i+1, comandos[i]))
