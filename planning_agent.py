# planning_agent.py
import json
from datetime import datetime

# Planlama hafızası
PLAN_FILE = "agent_plan.json"

def load_plan():
    try:
        with open(PLAN_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"tasks": [], "completed": [], "current_step": 0}

def save_plan(plan):
    with open(PLAN_FILE, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)

def create_plan(task):
    plan = load_plan()
    plan["tasks"] = [
        f"Uçak bileti ara: {task}",
        "Otel önerisi al",
        "Restoran rezervasyonu yap",
        "Günlük rota çiz"
    ]
    plan["completed"] = []
    plan["current_step"] = 0
    save_plan(plan)
    return f"Plan oluşturuldu: {len(plan['tasks'])} adım"

def execute_step():
    plan = load_plan()
    if plan["current_step"] >= len(plan["tasks"]):
        return "Tüm adımlar tamamlandı!"
    
    current = plan["tasks"][plan["current_step"]]
    # Simüle edilmiş eylem
    result = f"[Simüle] {current} tamamlandı."
    plan["completed"].append({
        "step": plan["current_step"] + 1,
        "task": current,
        "result": result,
        "time": datetime.now().isoformat()
    })
    plan["current_step"] += 1
    save_plan(plan)
    return result

def show_plan():
    plan = load_plan()
    output = "PLAN DURUMU:\n"
    for i, task in enumerate(plan["tasks"]):
        status = "✅" if i < plan["current_step"] else "⏳"
        output += f"  {status} Adım {i+1}: {task}\n"
    output += f"\nTamamlanan: {len(plan['completed'])} / {len(plan['tasks'])}"
    return output

def planning_agent():
    print("Planlama AI Agent Aktif!")
    print("Komutlar: plan [görev], adım, durum, exit\n")
    
    while True:
        komut = input("Agent > ").strip()
        if komut.lower() == "exit":
            print("Plan kaydedildi. Görüşürüz!")
            break
        elif komut.lower().startswith("plan "):
            gorev = komut[5:].strip()
            print(create_plan(gorev))
        elif komut.lower() == "adım":
            print(execute_step())
        elif komut.lower() == "durum":
            print(show_plan())
        else:
            print("Bilinmeyen komut. 'plan tatil' dene.")

# Başlat
planning_agent()