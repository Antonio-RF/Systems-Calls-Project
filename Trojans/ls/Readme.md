# Comandos:

## LS:

O primeiro comando foi o "ls". Com ele, eu fiz 3 trojans diferentes:

    1. Adicionei um printf("comentário").
        1.1 = Rodei Strace com a opção -a no diretório home.
        1.2 = Rodei Strace com a opção -lh no diretório home.
        1.3 = Rodei Strace com a opção -r no diretório "testes".
        1.4 = Rodei Strace com a opção -r em um diretório inexistente.

    2. Adicionei um fopen("%s\n", argv[i]).

    3. Adicionei hidden_backdoor().

