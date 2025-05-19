import psutil

def get_suspicious_processes(blacklist=None):
    if blacklist is None:
        blacklist = ['coinminer', 'keylogger', 'rat', 'hacktool', 'cheatengine']

    suspicious = []
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if proc.info['name'] and any(bad in proc.info['name'].lower() for bad in blacklist):
                suspicious.append(proc.info)
        except:
            continue
    return suspicious