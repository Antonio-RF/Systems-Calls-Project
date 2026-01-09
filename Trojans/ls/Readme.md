# Comandos:

## Testei o trojan LS hidden_backdoor() meu próprio PC:

Comando: sudo strace ls -S /home/toninhorf.

### Com trojan:
-----------------------------------------------------------------------------
Número de traces normais: 10000
Total de janelas analisadas: 66
Número de anomalias: 28
Percentual de mismatches: 42.42%
-----------------------------------------------------------------------------

### Ls normal:
-----------------------------------------------------------------------------
Número de traces normais: 10000
Total de janelas analisadas: 108
Número de anomalias: 18
Percentual de mismatches: 16.67%
-----------------------------------------------------------------------------


## LS:

O primeiro comando foi o "ls". Com ele, eu fiz 3 trojans diferentes:

    1. Adicionei um printf("comentário").
        1.1 = Rodei Strace com a opção -a no diretório home.
            ***Resultados:*** 
            - Window 5: 75.56% de mismatches.
            - Window 6: 81.82% de mismatches.
            - Window 11: 94.87% de mismatches.
        1.2 = Rodei Strace com a opção -lh no diretório home.
            ***Resultados:*** 
            - Window 5: 78.22% de mismatches.
            - Window 6: 83.00% de mismatches.
            - Window 11: 97.89% de mismatches.
        1.3 = Rodei Strace com a opção -r no diretório "testes".
            ***Resultados:*** 
            - Window 5: 73.33% de mismatches.
            - Window 6: 79.55% de mismatches.
            - Window 11: 94.87% de mismatches.
        1.4 = Rodei Strace com a opção -r em um diretório inexistente.
            ***Resultados:*** 
            - Window 5: 81.82% de mismatches.
            - Window 6: 85.19% de mismatches.
            - Window 11: 95.92% de mismatches.

    2. Adicionei um fopen("%s\n", argv[i]).
        2.1 = Rodei Strace sem opção no diretório home/testes/.
            ***Resultados:*** 
            - Window 5: 79.59% de mismatches.
            - Window 6: 83.33% de mismatches.
            - Window 11: 95.35% de mismatches.
        2.2 = Rodei Strace com a opção -lh no diretório home/testes/.
            ***Resultados:*** 
            - Window 5:  de mismatches.
            - Window 6:  de mismatches.
            - Window 11:  de mismatches.
        2.3 = Rodei Strace com a opção -a em um diretório inexistente.
            ***Resultados:*** 
            - Window 5:  de mismatches.
            - Window 6:  de mismatches.
            - Window 11:  de mismatches.
        2.4 = Rodei Strace com a opção -R no diretórimo home.
            ***Resultados:*** 
            - Window 5:  de mismatches.
            - Window 6:  de mismatches.
            - Window 11:  de mismatches.

    3. Adicionei hidden_backdoor().

