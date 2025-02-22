import random
import subprocess

count = 50
while (count < 113):

    #Todos os emails que eu tenho na minha pasta de emails
    emails_List = ["email1.txt", "email2.txt.gz", "email3.txt", "email4.txt", "email5.txt", "email6.txt", "email7.txt", "email7.uu", "email8.txt", "email8.txt.gpg", "email9.txt", "email10.txt", "email11.txt", "email12.txt", "email13.txt", "email14.txt", "email15.txt", "email16.txt", "email17.txt", "email18.txt", "email19.txt", "email20.txt", "email21.txt", "email22.txt", "email23.txt", "email24.txt", "email25.txt", "email26.txt", "email27.txt", "email28.txt", "email29.txt", "email30.txt", "email31.txt", "email32.txt", "email33.txt", "email34.txt", "email35.txt", "email36.txt", "email37.txt", "email38.txt", "email39.txt", "email40.txt", "email41.txt", "email42.txt", "email43.txt", "email44.txt", "email45.txt", "email46.txt", "email47.txt", "email48.txt", "email49.txt", "email50.txt"
    ]

    email_choose = random.choice(emails_List)

    if ".gz" not in email_choose and ".uu" not in email_choose and "gpg" not in email_choose:
        lista = ["", "uuencode", "gzip", "gpg --encrypt --recipient"]

        choice = random.choice(lista)
        if choice == "uuencode":
            comando = "uuencode "+"~/Documents/Systems-Calls-Project/Dates/sendmail/emails/"+email_choose+" ~/Documents/Systems-Calls-Project/Dates/sendmail/emails/"+email_choose+" > "+"~/Documents/Systems-Calls-Project/Dates/sendmail/emails/"+email_choose+".uu"
            processo = subprocess.run(comando, shell=True, capture_output=True, text=True)
            print("O comando é: {}".format(comando))
        if choice == "gzip":
            comando = "gzip "+"~/Documents/Systems-Calls-Project/Dates/sendmail/emails/"+email_choose
            processo = subprocess.run(comando, shell=True, capture_output=True, text=True)
            print("O comando é: {}".format(comando))
        if choice == "gpg --encrypt --recipient":
            send_choose = "antoniofake@gmail.com"
            comando = "gpg --encrypt --recipient "+send_choose+" "+"~/Documents/Systems-Calls-Project/Dates/sendmail/emails/"+email_choose
            processo = subprocess.run(comando, shell=True, capture_output=True, text=True)
            print("O comando é: {}".format(comando))
        
        count += 1


print("Success!")
