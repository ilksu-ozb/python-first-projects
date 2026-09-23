import json
import os

def save_task(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4) #terminale yazdığımız komutları dosyaya kaydedecek

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file) #dosyadan okur
    else:
        return [] #dosya yoksa boş liste döndürür