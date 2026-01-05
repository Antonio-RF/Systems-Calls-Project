import matplotlib.pyplot as plt

ls_normal = [2.4, 5.1, 8.7, 12.3, 18.9, 24.5]
ls_trojan = [36.0, 38.2, 41.5, 44.7, 46.9, 48.8]

plt.boxplot(
    [ls_normal, ls_trojan],
    labels=["ls normal", "ls trojanizado"]
)

plt.ylabel("Porcentagem de syscalls suspeitas (%)")
plt.title("Comparação de comportamento do comando ls")

plt.show()
