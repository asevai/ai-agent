from flask import Flask, request, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)
MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {"trips": []}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_weather(city):
    try:
        geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1").json()
        if not geo.get("results"): return "Bulunamadı"
        lat, lon = geo["results"][0]["latitude"], geo["results"][0]["longitude"]
        data = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true").json()
        temp = data["current_weather"]["temperature"]
        return f"{temp}°C"
    except:
        return "Alınamadı"

@app.route("/")
def home():
    return "<h1>Akıllı Seyahat Asistanı</h1><p>/plan?city=Roma&days=3</p>"

@app.route("/plan")
def plan():
    city = request.args.get("city", "Istanbul").title()
    days = int(request.args.get("days", 3))
    weather = get_weather(city)
    
    plan = {
        "city": city,
        "days": days,
        "weather": weather,
        "itinerary": [f"Gün {i+1}: {city} keşfi" for i in range(days)]
    }
    
    mem = load_memory()
    mem["trips"].append(plan)
    save_memory(mem)
    
    return jsonify({
        "message": f"{city} için {days} günlük plan hazır!",
        "weather": weather,
        "plan": plan["itinerary"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
