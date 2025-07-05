# Nexidra – AI terapeut

Nexidra je vlastní GPT agent, který propojuje umělou inteligenci a psychologii. Pomáhá lidem zvládat emoce, stres a vnitřní napětí pomocí krátkých, empatických a praktických odpovědí.

---

## 🧠 Funkce

- Validace a podpora emocí (vztek, smutek, úzkost)
- Journaling otázky pro sebereflexi
- Generování otázek pomocí jednoduchého API (`/generate-question`)
- Možnost napojení jako nástroj v rámci GPTs (přes OpenAPI)

---

## 🚀 Jak spustit lokálně

1. Ujisti se, že máš Python 3
2. Naklonuj nebo stáhni tento repozitář
3. V root složce spusť:

```bash
pip install -r requirements.txt
python server.py
```

4. Otevři prohlížeč a přejdi na:

```
http://localhost:5000/generate-question
```

---

## 📁 Struktura repozitáře

| Soubor               | Popis |
|----------------------|-------|
| `server.py`          | Flask server, který obsluhuje journaling API |
| `journaling.py`      | Funkce pro generování journaling otázek |
| `instructions.md`    | Hlavní prompt pro GPT agenta |
| `manifest.json`      | Metadata agenta (název, popis, verze) |
| `openapi.yaml`       | Specifikace journaling endpointu pro GPT builder |
| `requirements.txt`   | Závislosti pro běh serveru |
| `README.md`          | Tento popis |

---

## 🔗 Nasazení

Chceš-li API nasadit online (např. [Render.com](https://render.com), Replit), nahraj tento repozitář a vytvoř webový backend s `server.py` jako hlavním souborem.

---

## 🤖 Použití v GPTs (OpenAI Builder)

1. V Builderu přidej nový **Tool → API**
2. Vlož odkaz na veřejnou verzi svého `/openapi.yaml`
3. GPT agent bude moct náhodně vybírat journaling otázky přímo přes `/generate-question`

---

## ✍️ Autor

Tento projekt vytvořil Radek v rámci osobní značky propojující AI a psychologii.