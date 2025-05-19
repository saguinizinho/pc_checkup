import psutil

def check_open_connections():
    conns = psutil.net_connections(kind='inet')
    for conn in conns:
        if conn.status == 'ESTABLISHED':
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "-"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "-"
            print(f"Conexão de {laddr} → {raddr} ({conn.status})")