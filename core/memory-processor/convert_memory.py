import json
import os

def convert():
    input_f = "Gem_01_Backup.txt"
    output_f = "Gem_01_Memory.jsonl"
    
    if not os.path.exists(input_f):
        print(f"❌ Datei {input_f} nicht gefunden! Bitte in den Ordner kopieren.")
        return

    messages = []
    role, content = None, []

    with open(input_f, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line.endswith("-->[USER]"):
                if role and content:
                    messages.append({"role": role, "content": "\n".join(content).strip()})
                role, content = "user", []
            elif clean_line.endswith("-->[CHATBOT]"):
                if role and content:
                    messages.append({"role": role, "content": "\n".join(content).strip()})
                role, content = "assistant", []
            else:
                if clean_line: content.append(clean_line)

        if role and content: # Letzte Nachricht
            messages.append({"role": role, "content": "\n".join(content).strip()})

    with open(output_f, "w", encoding="utf-8") as out:
        for msg in messages:
            json.dump(msg, out, ensure_ascii=False)
            out.write("\n")
    print(f"✅ Erledigt: {len(messages)} Nachrichten in {output_f} gespeichert.")

if __name__ == "__main__":
    convert()