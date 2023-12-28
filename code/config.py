def main_info():
    return (
        {'value': 99.0, 'address': 0x0072B200, 'offset': [0x1E40, 0x10, 0x70, 0x18, 0x08, 0x58, 0x28, 0x1B0], 'DLL':"mono-2.0-bdwgc.dll"},     # Motivation
        {'value': 99, 'address': 0x01A8FDC0, 'offset': [0x820, 0xCD8, 0x28, 0x70, 0xE0], 'DLL':"UnityPlayer.dll"}
    )

def gacha_UR():
    return (
        {'value': 99, 'address': 0x0072B200, 'offset': [0x1920, 0x70, 0x50, 0x10, 0x20, 0x18], 'DLL':"mono-2.0-bdwgc.dll"}, 
        {'value': 99, 'address': 0x0072B200, 'offset': [0x1920, 0x70, 0x50, 0x10, 0x28, 0x18], 'DLL':"mono-2.0-bdwgc.dll"},
        {'value': 99, 'address': 0x0072B200, 'offset': [0x1920, 0x70, 0x50, 0x10, 0x30, 0x18], 'DLL':"mono-2.0-bdwgc.dll"},
        {'value': 99, 'address': 0x0072B200, 'offset': [0x1920, 0x70, 0x50, 0x10, 0x38, 0x18], 'DLL':"mono-2.0-bdwgc.dll"}
    )

def gacha_SR():
    return (
        {'value': 99, 'address': 0x0072B200, 'offset': [0x1920, 0x70, 0x50, 0x10, 0x20, 0x20], 'DLL':"mono-2.0-bdwgc.dll"},
        {'value': 99, 'address': 0x0072B200, 'offset': [0x1920, 0x70, 0x50, 0x10, 0x28, 0x20], 'DLL':"mono-2.0-bdwgc.dll"},
        {'value': 99, 'address': 0x0072B200, 'offset': [0x1920, 0x70, 0x50, 0x10, 0x30, 0x20], 'DLL':"mono-2.0-bdwgc.dll"},
        {'value': 99, 'address': 0x0072B200, 'offset': [0x1920, 0x70, 0x50, 0x10, 0x38, 0x20], 'DLL':"mono-2.0-bdwgc.dll"}
    )

def load_data():
    return (
        gacha_UR(),
        gacha_SR(),
        main_info()
    )
        
        
        
        
    