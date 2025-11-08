# real_ai_agent.py
import requests
import json
from datetime import datetime

# === KONFİGÜRASYON ===

MEMORY_FILE = "agent_memory.json"
PLAN_FILE = "agent_plan.json"

# === HAFIZA ===
def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"facts": {}, "history": []}

def save_memory(mem):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, ensure_ascii=False, indent=2)

def remember(key, value):
    mem = load_memory()
    mem["facts"][key] = value
    mem["history"].append({"time": datetime.now().isoformat(), "key": key, "value": value})
    save_memory(mem)

def recall(key):
    mem = load_memory()
    return mem["facts"].get(key, "Hatırlamıyorum.")

# === ARAÇ: HAVA DURUMU ===
def get_weather(city):
    # Şehir → koordinat (geocoding)
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=tr"
    try:
        geo = requests.get(geo_url).json()
        if not geo.get("results"):
            return f"{city} bulunamadı."
        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]
        
        # Hava durumu
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        data = requests.get(weather_url).json()
        temp = data["current_weather"]["temperature"]
        desc = {0: "Açık", 1: "Az bulutlu", 2: "Parçalı bulutlu", 3: "Bulutlu", 
                45: "Sisli", 61: "Hafif yağmur", 63: "Yağmur", 80: "Sağanak"}.get(
                data["current_weather"]["weathercode"], "Bilinmiyor")
        
        result = f"{city.title()}: {temp}°C, {desc}"
        remember(f"weather_{city.lower()}", result)
        return result
    except:
        return "Bağlantı hatası."
# === PLANLAMA ===
def create_travel_plan(city):
    plan = [
        f"Uçak bileti ara: İstanbul → {city}",
        f"Otel öner: {city} merkez",
        f"Restoran bul: {city} yerel lezzet",
        "Günlük gezi rotası çiz"
    ]
    with open(PLAN_FILE, "w", encoding="utf-8") as f:
        json.dump({"tasks": plan, "current": 0}, f, ensure_ascii=False, indent=2)
    return f"{city} için 4 adımlı plan oluşturuldu!"

def execute_next_step():
    try:
        with open(PLAN_FILE, "r", encoding="utf-8") as f:
            plan = json.load(f)
        step = plan["current"]
        if step >= len(plan["tasks"]):
            return "Tüm adımlar tamamlandı!"
        task = plan["tasks"][step]
        result = f"[Tamamlandı] {task}"
        plan["current"] += 1
        with open(PLAN_FILE, "w", encoding="utf-8") as f:
            json.dump(plan, f, ensure_ascii=False, indent=2)
        return result
    except:
        return "Plan bulunamadı. Önce 'plan [şehir]' yaz."

# === ANA AGENT ===
def real_ai_agent():
    print("GERÇEK AI AGENT v1.0 – Hava + Hafıza + Planlama")
    print("Komutlar: hava [şehir], plan [şehir], adım, sor [anahtar], durum, exit\n")
    
    while True:
        cmd = input("Agent > ").strip().lower()
        if cmd == "exit":
            print("AI Agent kapanıyor. Hafıza ve plan kaydedildi!")
            break
        elif cmd.startswith("hava "):
            city = cmd[5:].strip().title()
            print(get_weather(city))
        elif cmd.startswith("plan "):
            city = cmd[5:].strip().title()
            print(create_travel_plan(city))
        elif cmd == "adım":
            print(execute_next_step())
        elif cmd.startswith("sor "):
            key = cmd[4:].strip()
            print(recall(key))
        elif cmd == "durum":
            try:
                with open(PLAN_FILE, "r", encoding="utf-8") as f:
                    p = json.load(f)
                print(f"Plan: {p['current']}/{len(p['tasks'])} tamamlandı")
            except:
                print("Aktif plan yok.")
        else:
            print("Bilinmeyen komut. Örnek: 'hava Ankara', 'plan Paris'")

# Başlat
real_ai_agent()