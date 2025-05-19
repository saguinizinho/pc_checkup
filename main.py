from check_system import check_system_info
from check_processes import get_suspicious_processes
from check_files import scan_suspicious_files
from check_network import check_open_connections
from check_programs import list_installed_programs
from suggestions import suggest_fixes
from generate_report import generate_report

def main():
    print("=== VERIFICAÇÃO DO SISTEMA ===\n")
    from io import StringIO
    import sys

    buffer = StringIO()
    sys.stdout = buffer
    check_system_info()
    sys.stdout = sys.__stdout__
    system_output = buffer.getvalue().strip().split("\n")
    for line in system_output:
        print(line)

    print("\n=== PROCESSOS SUSPEITOS ===")
    processes = get_suspicious_processes()
    for proc in processes:
        print(f"- {proc['name']} (PID {proc['pid']}) - {proc['exe']}")
    suggest_fixes(processes, "processo")

    print("\n=== ARQUIVOS SUSPEITOS ===")
    suspicious_files = scan_suspicious_files()
    for f in suspicious_files:
        print(f"- {f}")
    suggest_fixes(suspicious_files, "arquivo")

    print("\n=== PROGRAMAS INSTALADOS ===")
    programs = list_installed_programs()
    for name in programs[:10]:
        print(f"- {name}")

    print("\nGerando relatório completo...")
    generate_report(system_output, processes, suspicious_files, programs)
    print("Relatório salvo como 'relatorio.txt'")

if __name__ == "__main__":
    main()