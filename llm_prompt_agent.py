# llm_prompt_agent.py - GÜNCEL VERSİYON

def llm_simulator(prompt):
    prompt = prompt.lower().strip()
    
    if "kaç elma" in prompt or "elma" in prompt:
        return ("Chain-of-Thought ile çözüyorum:\n"
                "1. Ali'nin 3 elması var.\n"
                "2. Ayşe 5 elma verdi → 3+5=8\n"
                "3. 2 elma yedi → 8-2=6\n"
                "Sonuç: 6 elma kaldı.")
    
    elif "ingilizceye çevir" in prompt or "çevir" in prompt and "ingilizce" in prompt:
        if "merhaba nasılsın" in prompt:
            return "Hello, how are you?"
        else:
            return "Çeviri yapıyorum: [Metin çevrilemedi, örnek eksik]"
    
    elif "tatil planı" in prompt or "günlük" in prompt and "plan" in prompt:
        return ("3 Günlük İstanbul Tatil Planı:\n"
                "Gün 1: Tarihi Yarımada (Ayasofya, Topkapı)\n"
                "Gün 2: Boğaz Turu + Bebek'te kahvaltı\n"
                "Gün 3: Adalar turu + alışveriş")
    
    elif "plan" in prompt:
        return ("1. Uçak bileti ara\n"
                "2. Otel karşılaştır\n"
                "3. Restoran öner\n"
                "4. Rota çiz")
    
    else:
        return "Anladım. Bu görevi hafızama aldım ve planlıyorum..."

def prompt_agent():
    print("🧠 LLM Prompt Agent v2 Aktif!")
    print("Doğal dilde görev ver, ben LLM gibi cevap vereceğim.\n")
    
    while True:
        giris = input("Sana: ").strip()
        if giris.lower() == "exit":
            print("🛑 Prompt Agent kapanıyor.")
            break
        cevap = llm_simulator(giris)
        print(f"Agent: {cevap}\n")

# Başlat
prompt_agent()