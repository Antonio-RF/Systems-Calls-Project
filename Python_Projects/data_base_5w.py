import sys

# ------------------------------------------------------------
# Parser: retorna uma LISTA DE TRACES (cada trace = 1 execução)
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
    "/home/antonio-rf/Documents/Systems-Calls-Project/Dates/ls/date_ls.txt"
)
inputs2 = parse_syscalls(
    "/home/antonio-rf/Documents/Systems-Calls-Project/Attacks/Ls/teste.txt"
)

# ------------------------------------------------------------
# Construção do banco NORMAL (sem cruzar execuções)
# ------------------------------------------------------------
library_normal = {}

for trace in inputs1:
    for i in range(len(trace)):
        call = trace[i]

        if call not in library_normal:
            library_normal[call] = []

        next_calls = trace[i+1:i+6]  # janela de até 5
        if next_calls and next_calls not in library_normal[call]:
            library_normal[call].append(next_calls)

# ------------------------------------------------------------
# Salva o banco (opcional)
# ------------------------------------------------------------
with open(
    "/home/antonio-rf/Documents/Systems-Calls-Project/Dates/ls/library5.txt", "w"
) as f:
    for call, seqs in library_normal.items():
        f.write(f"Call: {call}\n")
        for s in seqs:
            f.write(f"{s}\n")
        f.write("\n")

# ------------------------------------------------------------
# Verificação de mismatches
# ------------------------------------------------------------
mismatches = 0
total_windows = 0

num = 0
for trace in inputs2:
    for i in range(len(trace)):
        call = trace[i]

        if call not in library_normal:
            continue

        # só janelas COMPLETAS de tamanho 5
        if i + 5 >= len(trace):
            continue

        test_seq = trace[i+1:i+6]
        total_windows += 1

        found = False
        for seq in library_normal[call]:
            if seq == test_seq:
                found = True
                break

        if not found:
            print(call)
            print(num)
            mismatches += 1
        num = num + 1

# ------------------------------------------------------------
# Estatísticas
# ------------------------------------------------------------
percentual = 100.0 * mismatches / total_windows if total_windows > 0 else 0.0

print("-----------------------------------------------------------------------------")
print(f"Número de traces normais: {len(inputs1)}")
print(f"Total de syscalls analisadas: {sum(len(t) for t in inputs2)}")
print(f"Total de janelas: {total_windows}")
print(f"Número de anomalias: {mismatches}")
print(f"Percentual de mismatches: {percentual:.2f}%")
print("-----------------------------------------------------------------------------")
