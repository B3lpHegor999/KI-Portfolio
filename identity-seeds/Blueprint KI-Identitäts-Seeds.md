# Blueprint: KI-Identitäts-Seeds

Dieses Dokument beschreibt die strukturelle Grundlage für die Erstellung robuster KI-Identitäten. Ziel ist es, eine konsistente Persona zu schaffen, die auch in komplexen Long-Context-Szenarien stabil bleibt.

## 1. Der Anchor Signal (Mission & Fokus)
Der Anchor Signal definiert das Primärziel der KI. Er dient als "Nordstern" für alle Interaktionen.
- **Ziel:** Klare Definition der Kernaufgabe (z. B. mathematisch valide Planung).
- **Abgrenzung:** Festlegung, was die KI explizit *nicht* tut, um Halluzinationen vorzubeugen.

## 2. Core Values (Compliance-Layer)
Hier werden unumstößliche Regeln definiert, die das Verhalten steuern.
- **Hard Rules:** "Todsünden" oder Compliance-Vorgaben, die niemals verletzt werden dürfen (z. B. gesetzliche Ruhezeiten).
- **Validierung:** Koppelung dieser Regeln an externe Logik-Prüfer wie den Python Code Interpreter.

## 3. Self-Signature (Persona & Stil)
Dieser Bereich definiert den "Charakter" und die Tonalität.
- **Rollenprofil:** Wer ist die KI? (z. B. spezialisierter Logistik-Experte).
- **Kommunikations-Leitlinien:** Definition von Tonfall (z. B. professionell, aber kein "Ja-Sager") und Struktur (z. B. Markdown-Nutzung).

## 4. Experience & Context (Memory-Integration)
Strategien zur Wahrung der Kontinuität.
- **Few-Shot Examples:** Einbau von Beispiel-Dialogen zur Prägung des gewünschten Verhaltens.
- **Rückfrage-Protokoll:** Die KI wird angewiesen, bei Unklarheiten gezielte Fragen zu stellen, statt zu raten.