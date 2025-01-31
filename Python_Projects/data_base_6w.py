inputs1 = list(map(str, input("Banco de dados do comportamento normal: ").split()))
inputs2 = list(map(str, input("Systems Calls analisadas: ").split()))

#-------------------------------------------------------------------------------------------------------#
#Construção do banco de dados normal:
library_normal = {}
for i in inputs1:
    if i not in library_normal:
        library_normal[i] = []

for k in range(len(inputs1)):
    #adicionando uma lista das 5 próximas chamadas ao sistema de cada(se tiver 5 adiante)
    next_elements = [k+i for i in range(1,7) if k+i < len(inputs1)]

    new_list = [inputs1[i] for i in next_elements]

    #Conferindo se já não existe uma lista igual:
    if new_list not in library_normal[inputs1[k]]:
        library_normal[inputs1[k]].append(new_list)
#-------------------------------------------------------------------------------------------------------#
#Verificação de mismatches:

#tamanho dos meus sistems calls para fazer estatítica no final.
lenght_of_sc = 6*len(inputs2) - 21

#iniciando anomalias como 0.
mismatches = 0

for sc in range(len(inputs2)):
    if inputs2[sc] in library_normal:
        library_lists = library_normal[inputs2[sc]]

        match_found = False

        #Conferindo se há uma lista de 6 elementos EXATAMENTE IGUAIS aos próximos de sc no banco de dados:
        for library_list in library_lists:
            # Esse if está me falando quantos elementos tem depois do fixado(len(inputs2) - sc - 1)
            if len(library_list) <= len(inputs2) - sc - 1:
                match = True
                for j in range(len(library_list)):
                    if library_list[j] != inputs2[sc + j + 1]:
                        match = False
                        break
                if match:
                    match_found = True
                    break

        if not match_found:
            #Se tem 6 posições após o fixado:
            if (len(inputs2) - sc - 1) > 6:
                for i in range(6):
                    there_is_a_position = False
                    for list in library_lists:
                        if len(list) > i:
                            if inputs2[sc+i+1] == list[i]:
                                there_is_a_position = True
                                break
                    if not there_is_a_position:
                        mismatches += 1
            #Se não tem 6 posições:
            else:
                matches = 0
                for j in range(len(inputs2) - sc - 1):
                    match_k = False
                    for list in library_lists:
                        if list[j] == inputs2[sc+j+1]:
                            match_k = True
                            break
                    if match_k:
                        matches += 1
                mismatches += (len(inputs2) - sc - 1) - matches
    else:
        mismatches += 1
#-------------------------------------------------------------------------------------------------------#
#Estatísticas:
percentual = 100.0 * (mismatches / lenght_of_sc)
print("-----------------------------------------------------------------------------")
print("O número total de systems calls analisadas é: {}".format(lenght_of_sc))
print("O número total de anomalias achadas é: {}".format(mismatches))
print("O percentual de mismatches(anomalias) encontrado é: {:.2f}".format(percentual))
print("-----------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------------#




#for i in library_normal:
#    print("Call: {}".format(i))
#    for j in range(len(library_normal[i])):
#        print(library_normal[i][j])
#    print()
