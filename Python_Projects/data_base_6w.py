inputs = list(map(str, input().split()))

library = {}
for i in inputs:
    if i not in library:
        library[i] = []

for k in range(len(inputs)):
    #adicionando uma lista das 5 próximas chamadas ao sistema de cada(se tiver 5 adiante)
    next_elements = [k+i for i in range(1,7) if k+i < len(inputs)]

    new_list = [inputs[i] for i in next_elements]

    #Conferindo se já não existe uma lista igual:
    if new_list not in library[inputs[k]]:
        library[inputs[k]].append(new_list)

for i in library:
    print("Call: {}".format(i))
    for j in range(len(library[i])):
        print(library[i][j])
    print()
