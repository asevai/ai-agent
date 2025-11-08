# multi_agent.py
import requests
import json
from datetime import datetime

# === HAVA AGENT ===
def hava_agent(city):
    try:
        geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1").json()
        if not geo.get("results"): return "Şehir yok."
        lat, lon = geo["results"][0]["latitude"], geo["results"][0]["longitude"]
        data = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true").json()
        temp = data["current_weather"]["temperature"]
        return f"Hava: {temp}°C"
    except:
        return "Hava alınamadı."

# === PLANLAMA AGENT ===
def planlama_agent(city, days):
    return [
        f"Gün 1: {city} merkez",
        f"Gün 2: Tarihi yerler",
        f"Gün 3: Yerel yemekler"
    ]

# === ARAŞTIRMA AGENT ===
def arastirma_agent(city):
    return f"{city} için Colosseum, Pantheon, Fontana di Trevi önerilir."

# === ANA AGENT ===
def multi_agent():
    print("MULTI-AGENT SİSTEMİ – EKİP ÇALIŞMASI")
    print("Komut: tatil [şehir] [gün]\n")
    
    while True:
        cmd = input("Kullanıcı > ").strip().lower()
        if cmd == "exit":
            print("Ekip dağılıyor!")
            break
        if cmd.startswith("tatil "):
            parts = cmd[6:].rsplit(" ", 1)
            city = parts[0].title()
            days = int(parts[1]) if len(parts) > 1 else 3
            
            print("\nAna Agent: Görev dağıtılıyor...\n")
            
            hava = hava_agent(city)
            print(f"Hava Agent: {hava}")
            
            plan = planlama_agent(city, days)
            print(f"Planlama Agent: {len(plan)} günlük plan hazır!")
            for i, step in enumerate(plan):
                print(f"  • {step}")
            
            oneri = arastirma_agent(city)
            print(f"Araştırma Agent: {oneri}")
            
            print("\nTatil planı tamamlandı!\n")
        else:
            print("Komut: 'tatil Roma 3'")

multi_agent()