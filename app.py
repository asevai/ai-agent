# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def get_weather(city):
    try:
        geo = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1").json()
        if not geo.get("results"): return "Şehir yok."
        lat, lon = geo["results"][0]["latitude"], geo["results"][0]["longitude"]
        data = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true").json()
        temp = data["current_weather"]["temperature"]
        return f"{city.title()}: {temp}°C"
    except:
        return "Hava alınamadı."

@app.route("/")
def home():
    return """
    <h1>AI Agent API</h1>
    <p>/weather?city=Ankara</p>
    """

@app.route("/weather")
def weather():
    city = request.args.get("city", "Istanbul")
    result = get_weather(city)
    return jsonify({"city": city, "weather": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)