# tatil_agent.py
import requests
import json
from datetime import datetime

MEMORY_FILE = "tatil_memory.json"

# HAFIZA
def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"plans": []}

def save_memory(data):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# HAVA DURUMU (Open-Meteo)
def get_weather(city):
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo = requests.get(geo_url).json()
        if not geo.get("results"): return "Şehir bulunamadı."
        lat, lon, name = geo["results"][0]["latitude"], geo["results"][0]["longitude"], geo["results"][0]["name"]
        
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        data = requests.get(weather_url).json()
        temp = data["current_weather"]["temperature"]
        code = data["current_weather"]["weathercode"]
        desc = {0: "Açık", 1: "Az bulutlu", 2: "Parçalı bulutlu", 3: "Kapalı", 61: "Yağmur"}.get(code, "Diğer")
        return f"{name}: {temp}°C, {desc}"
    except:
        return "Hava bilgisi alınamadı."

# PLAN OLUŞTUR
def create_plan(city, days):
    weather = get_weather(city)
    plan = {
        "city": city,
        "days": days,
        "weather": weather,
        "steps": [
            f"Gün 1: {city} merkez turu",
            f"Gün 2: Tarihi yerler gezisi",
            f"Gün 3: Yerel lezzetler + dönüş"
        ],
        "completed": 0,
        "created": datetime.now().isoformat()
    }
    mem = load_memory()
    mem["plans"].append(plan)
    save_memory(mem)
    return f"{city} için {days} günlük tatil planı oluşturuldu!\nHava: {weather}"

# SONRAKİ ADIM
def next_step():
    mem = load_memory()
    if not mem["plans"]: return "Aktif plan yok."
    plan = mem["plans"][-1]
    if plan["completed"] >= len(plan["steps"]):
        return "Tatil planı tamamlandı!"
    step = plan["steps"][plan["completed"]]
    plan["completed"] += 1
    save_memory(mem)
    return f"[Tamamlandı] {step}"

# DURUM
def status():
    mem = load_memory()
    if not mem["plans"]: return "Plan yok."
    p = mem["plans"][-1]
    return f"{p['city']} Planı: {p['completed']}/{len(p['steps'])} tamamlandı\nHava: {p['weather']}"

# ANA AGENT
def tatil_agent():
    print("TATİL PLANLAYICI AI AGENT")
    print("Komutlar: plan [şehir] [gün], adım, durum, exit\n")
    while True:
        cmd = input("Agent > ").strip().lower()
        if cmd == "exit":
            print("Görüşürüz! Planlar kaydedildi.")
            break
        elif cmd.startswith("plan "):
            parts = cmd[5:].rsplit(" ", 1)
            city = parts[0].title()
            days = int(parts[1]) if len(parts) > 1 else 3
            print(create_plan(city, days))
        elif cmd == "adım":
            print(next_step())
        elif cmd == "durum":
            print(status())
        else:
            print("Bilinmeyen komut. Örnek: 'plan Roma 3'")

tatil_agent()