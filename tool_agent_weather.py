# GEREKLİ: pip install requests
import requests
import json

# API ANAHTARINI BURAYA YAZ (kendi anahtarını al!)
API_KEY = "5468b562b6248a958a6e495256bed711"  # <-- DÜZENLE!

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"{city.title()}: {temp}°C, {desc.capitalize()}"
        else:
            return f"Şehir bulunamadı: {data.get('message', 'Hata')}"
    except:
        return "API bağlantı hatası. İnternetini kontrol et."

def calculator(expression):
    # Güvenli hesaplama (sadece + - * /)
    allowed = set('0123456789+-*/. ()')
    if all(c in allowed for c in expression):
        try:
            return f"Sonuç: {eval(expression)}"
        except:
            return "Hesaplama hatası!"
    else:
        return "Geçersiz karakter!"

def tool_agent():
    print("🌤️ Tool Agent v1 – Hava Durumu + Hesap Makinesi")
    print("Komutlar: hava [şehir], hesapla [işlem], exit\n")
    
    while True:
        komut = input("Agent > ").strip()
        if komut.lower() == "exit":
            print("Agent kapanıyor...")
            break
        elif komut.lower().startswith("hava "):
            sehir = komut[5:].strip()
            print(f"🔍 Araç: Hava durumu alınıyor...")
            print(get_weather(sehir))
        elif komut.lower().startswith("hesapla "):
            islem = komut[8:].strip()
            print(f"🧮 Araç: Hesaplanıyor...")
            print(calculator(islem))
        else:
            print("Bilinmeyen komut. 'hava İstanbul' veya 'hesapla 5*3' dene.")

# Başlat
tool_agent()