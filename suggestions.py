def suggest_fixes(items, tipo):
    if not items:
        print("Nenhuma irregularidade encontrada.")
        return

    print("\nSugestões de correção:")
    for item in items:
        if tipo == "processo":
            print(f"- Verificar o processo '{item['name']}' (PID {item['pid']}). Considere encerrá-lo se desconhecido.")
        elif tipo == "arquivo":
            print(f"- Analise o arquivo: {item}. Recomendado escanear com antivírus ou excluir se for suspeito.")