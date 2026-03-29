import asyncio
from bleak import BleakScanner

async def tara():
    print("Bluetooth cihazları taranıyor...\n")
    cihazlar = await BleakScanner.discover(timeout=5.0)
    
    if not cihazlar:
        print("Hiç cihaz bulunamadı!")
        return
    
    for c in cihazlar:
        print(f"İsim : {c.name or 'Bilinmiyor'}")
        print(f"MAC  : {c.address}")
        print("-" * 30)

asyncio.run(tara())