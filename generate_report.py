def generate_report(system_info, processes, files, programs):
    with open("relatorio.txt", "w", encoding='utf-8') as f:
        f.write("=== RELATÓRIO DO SISTEMA ===\n")
        for line in system_info:
            f.write(line + "\n")

        f.write("\n=== PROCESSOS SUSPEITOS ===\n")
        for p in processes:
            f.write(f"{p['name']} (PID {p['pid']}) - {p['exe']}\n")

        f.write("\n=== ARQUIVOS SUSPEITOS ===\n")
        for path in files:
            f.write(f"{path}\n")

        f.write("\n=== PROGRAMAS INSTALADOS ===\n")
        for name in programs:
            f.write(f"{name}\n")

        f.write("\n=== FIM DO RELATÓRIO ===\n")