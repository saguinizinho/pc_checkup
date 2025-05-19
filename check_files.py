import os

def scan_suspicious_files():
    suspicious_ext = ['.exe', '.bat', '.vbs', '.scr']
    suspicious_paths = ['C:\\Users', '/home']

    found = []

    for path in suspicious_paths:
        if not os.path.exists(path):
            continue
        for root, _, files in os.walk(path):
            for file in files:
                if any(file.lower().endswith(ext) for ext in suspicious_ext):
                    full_path = os.path.join(root, file)
                    if "AppData" in full_path or "Temp" in full_path or "Downloads" in full_path:
                        found.append(full_path)
    return found