# ReAct Agent Simülatörü

def react_agent(gorev):
    print(f"🎯 GÖREV: {gorev}\n")
    adim = 1
    
    # Simüle edilmiş araçlar
    def google_search(sorgu):
        print(f"   [Araç] Google: {sorgu}")
        return f"{sorgu} için sonuç: [simüle veri]"
    
    def calculate(islem):
        print(f"   [Araç] Hesap Makinesi: {islem}")
        try:
            return eval(islem)
        except:
            return "Hesaplama hatası"
    
    def translate(metin):
        print(f"   [Araç] Çeviri: {metin}")
        return f"{metin} → [çeviri simülasyonu]"
    
    # ReAct döngüsü
    dusunce = f"Bu görevi çözmek için ne yapmalıyım? Görev: {gorev}"
    print(f"🤔 Düşünce {adim}: {dusunce}")
    adim += 1
    
    # Basit karar mekanizması
    if "hesapla" in gorev.lower() or any(op in gorev for op in ["+", "-", "*", "/"]):
        # Sayıları çıkar
        import re
        sayilar = re.findall(r'\d+', gorev)
        if len(sayilar) >= 2:
            islem = f"{sayilar[0]} + {sayilar[1]}"
            sonuc = calculate(islem)
            print(f"   Gözlem: {sonuc}")
            print(f"✅ Sonuç: {sayilar[0]} + {sayilar[1]} = {sonuc}\n")
            return
    
    elif "ara" in gorev.lower() or "bul" in gorev.lower():
        sorgu = gorev.split("ara")[-1].strip() if "ara" in gorev else gorev
        sonuc = google_search(sorgu)
        print(f"   Gözlem: {sonuc}")
        print(f"✅ Sonuç: {sorgu} bulundu!\n")
        return
    
    elif "çevir" in gorev.lower():
        metin = gorev.split("çevir")[-1].strip()
        sonuc = translate(metin)
        print(f"   Gözlem: {sonuc}")
        print(f"✅ Çeviri tamamlandı!\n")
        return
    
    else:
        print(f"   Gözlem: Bilinmeyen görev tipi.")
        print(f"✅ Sonuç: Bu görevi öğreniyorum. Yakında yapabilirim!\n")

# Test et!
print("🧠 ReAct Agent Aktif!\n")
react_agent("2 ve 5'i topla hesapla")
react_agent("en iyi AI kurslarını ara")
react_agent("hello world İngilizceye çevir")
react_agent("Bana hava durumunu söyle")