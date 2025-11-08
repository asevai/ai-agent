# memory_agent.py
import json
from datetime import datetime

# Hafıza dosyası
MEMORY_FILE = "agent_memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"history": [], "facts": {}}

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)

def remember_fact(key, value):
    memory = load_memory()
    memory["facts"][key] = value
    memory["history"].append({
        "time": datetime.now().isoformat(),
        "type": "fact",
        "key": key,
        "value": value
    })
    save_memory(memory)
    return f"Hafızaya alındı: {key} = {value}"

def recall_fact(key):
    memory = load_memory()
    if key in memory["facts"]:
        return f"Hatırlıyorum: {key} = {memory['facts'][key]}"
    else:
        return "Bunu hatırlamıyorum."

def get_history():
    memory = load_memory()
    recent = memory["history"][-5:]
    return [f"{h['time'][:10]}: {h['key']} = {h['value']}" for h in recent]

def memory_agent():
    print("Hafızalı AI Agent Aktif!")
    print("Komutlar: hatırla [anahtar] [değer], sor [anahtar], geçmiş, exit\n")
    
    while True:
        komut = input("Agent > ").strip()
        if komut.lower() == "exit":
            print("Hafıza kaydedildi. Görüşürüz!")
            break
        elif komut.lower().startswith("hatırla "):
            parts = komut[8:].split(" ", 1)
            if len(parts) == 2:
                key, value = parts
                print(remember_fact(key, value))
            else:
                print("Kullanım: hatırla isim Ahmet")
        elif komut.lower().startswith("sor "):
            key = komut[4:].strip()
            print(recall_fact(key))
        elif komut.lower() == "geçmiş":
            print("Son 5 kayıt:")
            for item in get_history():
                print(f"  • {item}")
        else:
            print("Bilinmeyen komut. 'hatırla isim Ahmet' dene.")

# Başlat
memory_agent()