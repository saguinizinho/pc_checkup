import platform

def list_installed_programs():
    if platform.system() != "Windows":
        print("Listagem de programas disponível apenas no Windows.")
        return []

    import wmi
    c = wmi.WMI()
    programs = []

    for product in c.Win32_Product():
        name = product.Name
        if name:
            programs.append(name)
    return sorted(programs)