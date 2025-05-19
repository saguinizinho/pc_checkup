import platform
import psutil
import socket

def check_system_info():
    print(f"SO: {platform.system()} {platform.release()}")
    print(f"Arquitetura: {platform.machine()}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"CPU: {platform.processor()}")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print(f"Disco: {round(psutil.disk_usage('/').total / (1024**3), 2)} GB")