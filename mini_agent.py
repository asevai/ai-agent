# MİNİ AI AGENT SİMÜLATÖRÜ
# Bu agent, basit görevleri yerine getirir

def mini_agent():
    print("🤖 Mini AI Agent Aktif!")
    print("Mevcut araçlar: 1) Hava Durumu, 2) Not Al, 3) Hesap Makinesi")
    
    while True:
        komut = input("\nAgent'e komut ver (çıkmak için 'exit'): ").strip().lower()
        
        if komut == "exit":
            print("👋 Agent kapanıyor. Görüşürüz!")
            break
        elif "hava" in komut:
            sehir = input("Hangi şehir? ")
            print(f"🌤️ {sehir.title()} için hava durumu: Güneşli, 22°C")
        elif "not" in komut:
            not_icerik = input("Notunuz: ")
            print(f"📝 Not alındı: {not_icerik}")
        elif "hesap" in komut or "topla" in komut:
            try:
                sayi1 = float(input("1. sayı: "))
                sayi2 = float(input("2. sayı: "))
                print(f"🧮 Sonuç: {sayi1 + sayi2}")
            except:
                print("❌ Geçersiz sayı!")
        else:
            print("⚠️ Bilinmeyen komut. Lütfen tekrar dene.")

# Agent'i başlat
mini_agent()