# ------------------------------------------------------------
# Parser: retorna uma LISTA DE TRACES
# ------------------------------------------------------------
def parse_syscalls(path):
    traces = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if '|' in line:
                seq = line.split('|', 1)[1]
                calls = [c for c in seq.split(';') if c]
            else:
                calls = line.split()

            if calls:
                traces.append(calls)

    return traces


# ------------------------------------------------------------
# Entrada
# ------------------------------------------------------------
inputs1 = parse_syscalls(
    "/home/toninhorf/Documentos/Systems-Calls-Project/Dates/ls/date_ls.txt"
)
inputs2 = parse_syscalls(
    "/home/toninhorf/Documentos/Systems-Calls-Project/Attacks/Ls/teste.txt"
)

# ------------------------------------------------------------
# Construção do banco NORMAL
# call -> set de sequências de tamanho 5
# ------------------------------------------------------------
library_normal = {}

for trace in inputs1:
    for i in range(len(trace)):
        # só considera se EXISTEM 5 syscalls depois
        if i + 6 >= len(trace):
            continue

        call = trace[i]
        seq5 = tuple(trace[i+1:i+7])  # EXATAMENTE 6

        if call not in library_normal:
            library_normal[call] = set()

        library_normal[call].add(seq5)

# ------------------------------------------------------------
# Verificação de mismatches
# ------------------------------------------------------------
mismatches = 0
total_windows = 0

for trace in inputs2:
    for i in range(len(trace)):
        if i + 6 >= len(trace):
            continue

        call = trace[i]
        seq5 = tuple(trace[i+1:i+7])
        total_windows += 1

        if call not in library_normal:
            mismatches += 1
            continue

        if seq5 not in library_normal[call]:
            mismatches += 1

# ------------------------------------------------------------
# Estatísticas
# ------------------------------------------------------------
percentual = 100.0 * mismatches / total_windows if total_windows else 0

print("-----------------------------------------------------------------------------")
print(f"Número de traces normais: {len(inputs1)}")
print(f"Total de janelas analisadas: {total_windows}")
print(f"Número de anomalias: {mismatches}")
print(f"Percentual de mismatches: {percentual:.2f}%")
print("-----------------------------------------------------------------------------")


