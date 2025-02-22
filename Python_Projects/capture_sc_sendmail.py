import subprocess
import random
from separator import separator

resultado = []
comandos = []
for i in range(1000):

    # 4 emails = [fake, real, real, real].
    # Para testar diferentes remetentes e enviar para emails reais e fakes igual o paper faz. 
    list_emails = ["antoniofake@gmail.com", "antoniidaressurreicao@gmail.com", "marcosassisstresser@gmail.com", "emailtesteic1234@gmail.com"]

    email_choose = random.choice(list_emails)

    files_list = ["convert_emails.py", "email22.txt.gpg", "email34.txt.gz", "email45.txt.gz", "email10.txt.gz", "email22.txt.uu", "email34.txt.uu", "email45.txt.uu", "email10.txt.uu", "email23.txt.gz", "email35.txt.gpg", "email46.txt.gz", "email11.txt.gz", "email23.txt.uu", "email35.txt.gz", "email46.txt.uu", "email11.txt.uu", "email24.txt.gpg", "email35.txt.uu", "email47.txt.gz", "email12.txt.gz", "email24.txt.gz", "email36.txt", "email47.txt.uu", "email12.txt.uu", "email24.txt.uu", "email36.txt.gpg", "email48.txt.gz", "email13.txt.gz", "email25.txt.gz", "email37.txt.gz", "email48.txt.uu", "email13.txt.uu", "email25.txt.uu", "email38.txt", "email49.txt", "email14.txt.gpg", "email26.txt.gpg", "email38.txt.gpg", "email49.txt.gpg", "email14.txt.gz", "email26.txt.gz", "email38.txt.uu", "email49.txt.uu", "email15.txt", "email26.txt.uu", "email39.txt.gpg", "email4.txt.gz",
    "email15.txt.gpg", "email27.txt", "email39.txt.gz", "email4.txt.uu", "email15.txt.uu", "email27.txt.uu", "email39.txt.uu", "email50.txt.gpg", "email16.txt.gz", "email28.txt.gz", "email3.txt.gz", "email50.txt.gz", "email16.txt.uu", "email28.txt.uu", "email3.txt.uu", "email5.txt.gz", "email17.txt", "email29.txt", "email40.txt.gpg", "email5.txt.uu", "email18.txt.gpg", "email2.txt.gz", "email40.txt.gz", "email6.txt.gz", "email18.txt.gz," "email30.txt", "email41.txt.gz", "email6.txt.uu", "email18.txt.uu", "email30.txt.uu", "email41.txt.uu", "email7.txt.gpg", "email19.txt", "email31.txt.gz", "email42.txt.gpg", "email7.txt.gz", "email19.txt.gpg", "email31.txt.uu", "email42.txt.gz", "email7.txt.uu", "email1.txt.gz", "email32.txt.gpg", "email42.txt.uu", "email7.uu", "email1.txt.uu", "email32.txt.gz", "email43.txt.gpg", "email8.txt", "email20.txt.gz", "email32.txt.uu", "email43.txt.gz", "email8.txt.gpg", "email20.txt.uu", "email33.txt", "email43.txt.uu", "email8.txt.uu", "email21.txt.gz", "email33.txt.gpg", "email44.txt.gpg", "email9.txt.gpg", "email21.txt.uu", "email33.txt.uu", "email44.txt.gz", "email9.txt.gz"]

    file_choose = random.choice(files_list)

    comando = f"strace sendmail {email_choose} < ~/Documents/Systems-Calls-Project/Dates/sendmail/emails/{file_choose}"
    print("Esse é o comando: {}".format(comando))
    comandos.append(comando)

    processo = subprocess.run(comando, shell=True, capture_output=True, text=True)

    resultado_preliminar = separator(processo.stderr)
    resultado.extend(resultado_preliminar)


with open('/home/toninho/Documents/Systems-Calls-Project/Dates/sendmail/date_ls.txt', 'w') as file1:
    file1.write(" ".join(resultado))

with open('/home/toninho/Documents/Systems-Calls-Project/Dates/sendmail/commands.txt', 'w') as file2:
    for i in range(len(comandos)):
        file2.write("{}. {}\n".format(i+1, comandos[i]))

