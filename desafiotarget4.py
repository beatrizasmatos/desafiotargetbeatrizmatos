faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_faturamento_dos_estados = sum(faturamento_por_estado.values())

print("Percentual de faturamento por estado:")
for estado, faturamento in faturamento_por_estado.items():
    percentual_faturamento = (faturamento / total_faturamento_dos_estados) * 100
    print(f"{estado}: {percentual_faturamento:.2f}%")