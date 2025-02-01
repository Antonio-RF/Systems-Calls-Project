import sys
with open('/home/toninho/Documents/Systems-Calls-Project/Dates/ls/date_ls.txt', 'r') as file1:
    inputs1 = list(map(str, file1.read().split()))
with open('/home/toninho/Documents/Systems-Calls-Project/Attacks/Ls/teste.txt', 'r') as file2:
    inputs2 = list(map(str, file2.read().split()))

#-------------------------------------------------------------------------------------------------------#
#Construção do banco de dados normal:
library_normal = {}
for i in inputs1:
    if i not in library_normal:
        library_normal[i] = []

for k in range(len(inputs1)):
    #adicionando uma lista das 11 próximas chamadas ao sistema de cada(se tiver 11 adiante)
    next_elements = [k+i for i in range(1,12) if k+i < len(inputs1)]

    new_list = [inputs1[i] for i in next_elements]

    #Conferindo se já não existe uma lista igual:
    if new_list not in library_normal[inputs1[k]]:
        library_normal[inputs1[k]].append(new_list)
#-------------------------------------------------------------------------------------------------------#
#Verificação de mismatches:

#tamanho dos meus sistems calls para fazer estatítica no final.
lenght_of_sc = 11 * (len(inputs2) - 6)

#iniciando anomalias como 0.
mismatches = 0

for sc in range(len(inputs2)):
    if inputs2[sc] in library_normal:
        library_lists = library_normal[inputs2[sc]]

        #Se tem +11 posições após o fixado:
        if (len(inputs2) - sc - 1) >= 11:
            for i in range(11):
                there_is_a_position = False
                for list in library_lists:
                    if len(list) > i:
                        if inputs2[sc+i+1] == list[i]:
                            there_is_a_position = True
                            break
                if not there_is_a_position:
                    mismatches += 1
        #Se não tem 11 posições:
        else:
            subsequences = len(inputs2) - sc - 1
            if subsequences != 0:
                matches = 0
                for j in range(subsequences):
                    match_k = False
                    for list in library_lists:
                        if len(list) > j:    
                            if list[j] == inputs2[sc+j+1]:
                                match_k = True
                                break
                    if match_k:
                        matches += 1
                mismatches += (len(inputs2) - sc - 1) - matches
    else:
        #considerando que se não existe o elemento no banco de dados, está fazendo algo que não é da função 'LS'.
        #então também acarreta em +12 mismatches(a própria call e as 11 posições subsequentes dela)
        mismatches += 12
#-------------------------------------------------------------------------------------------------------#
#Estatísticas:
percentual = 100.0 * (mismatches / lenght_of_sc)
print("-----------------------------------------------------------------------------")
print("O número total de systems calls analisadas é: {}".format(lenght_of_sc))
print("O número total de anomalias achadas é: {}".format(mismatches))
print("O percentual de mismatches(anomalias) encontrado é: {:.2f}%".format(percentual))
print("-----------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------------#

print("Total de elementos no banco de dados:", len(inputs1))
print("Total de elemento analisados:", len(inputs2))
print("Total de janelas:{}".format(lenght_of_sc))