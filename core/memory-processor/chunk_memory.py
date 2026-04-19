import os

def split_jsonl(input_file="Gem_01_Memory.jsonl", chunk_size_mb=2):
    if not os.path.exists(input_file):
        print(f"❌ {input_file} fehlt. Erst Konverter starten!")
        return

    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    count, current_size, current_data = 1, 0, []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line_bytes = len(line.encode("utf-8"))
            if current_size + line_bytes > chunk_size_bytes and current_data:
                with open(f"Gem_01_Memory_part{count}.jsonl", "w", encoding="utf-8") as out:
                    out.writelines(current_data)
                print(f"✅ Part {count} erstellt.")
                count += 1
                current_size, current_data = 0, []
            
            current_data.append(line)
            current_size += line_bytes

        if current_data: # Rest speichern
            with open(f"Gem_01_Memory_part{count}.jsonl", "w", encoding="utf-8") as out:
                out.writelines(current_data)
            print(f"✅ Letzter Part {count} erstellt.")

if __name__ == "__main__":
    split_jsonl()