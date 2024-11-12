import json

with open("/Users/BeatrizMatos/Documents/targetdesafio/exercicio3target/faturamentodesafiotarget.json", "r") as arquivo:
    dados = json.load(arquivo)
    import json

faturamento_diario = dados["faturamento_diario"]
faturamento_validos = [valor for valor in faturamento_diario.values() if valor > 0]

menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)
media_faturamento = sum(faturamento_validos) / len(faturamento_validos)
dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_faturamento)

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
print(f"Média de faturamento: {media_faturamento}")
