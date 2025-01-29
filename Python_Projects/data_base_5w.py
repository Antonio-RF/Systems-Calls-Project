inputs = list(map(str, input().split()))

library = {}
for i in inputs:
    if i not in library:
        library[i] = []

for k in range(len(inputs)):
    #adicionando uma lista das 5 próximas chamadas ao sistema de cada(se tiver 5 adiante)
    next_elements = [k+i for i in range(1,6) if k+i < len(inputs)]

    library[inputs[k]].append([inputs[i] for i in next_elements])

for i in library:
    print("Call: {}".format(i))
    for j in range(len(library[i])):
        print(library[i][j])
    print()
