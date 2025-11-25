# Hugging Face AI Alkalmazás - Részletes Használati Útmutató

## 📖 Bevezetés

Ez az alkalmazás négy fő AI funkciót biztosít a Hugging Face Transformers könyvtár használatával:

1. **Sentiment Analysis** - Szövegek érzelmi töltetének automatikus elemzése
2. **Question Answering** - Intelligens kérdés-válasz rendszer
3. **Text Summarization** - Automatikus szövegösszefoglalás
4. **Image Classification** - Képek tartalmának felismerése

## 🔧 Telepítés és Beállítás

### Rendszerkövetelmények

- **Python**: 3.8 vagy újabb verzió
- **RAM**: Minimum 4 GB (ajánlott: 8 GB vagy több)
- **Tárhely**: ~5 GB a modellek cache-eléséhez
- **Internet**: Szükséges az első futtatáshoz (modellek letöltése)

### Telepítési Lépések

1. **Repository letöltése**
   ```bash
   git clone https://github.com/zsoltfrks/ml-practice-research.git
   cd ml-practice-research
   ```

2. **Virtuális környezet létrehozása (AJÁNLOTT!)**
   
   Linux/Mac:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
   Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Függőségek telepítése**
   ```bash
   pip install -r requirements.txt
   ```
   
   Ez telepíti:
   - `transformers` - Hugging Face Transformers könyvtár
   - `torch` - PyTorch deep learning framework
   - `pillow` - Képfeldolgozás
   - `requests` - HTTP kérések kezelése

### Első Futtatás

Az első futtatáskor az alkalmazás automatikusan letölti a szükséges AI modelleket a Hugging Face Hub-ról. Ez a folyamat:
- Néhány perctől akár 10-15 percig is tarthat
- Internetkapcsolatot igényel
- A modelleket a `~/.cache/huggingface/` könyvtárba menti
- Csak egyszer kell lefutnia, utána offline is működik

## 🚀 Használati Módok

### 1. Demo Mód (Automatikus Bemutató)

Ez a legegyszerűbb módja az alkalmazás kipróbálásának:

```bash
python ai_app.py
```

**Mit csinál a demo mód?**
- Bemutatja mind a négy AI funkciót
- Előre definiált példákat használ
- Automatikusan végigfut az összes képességen
- Kiírja az eredményeket a konzolra

**Várható kimenet:**
```
============================================================
🚀 HUGGING FACE AI ALKALMAZÁS
============================================================

💡 Demo mód - különböző AI képességek bemutatása

============================================================
🎭 SENTIMENT ANALYSIS DEMO
============================================================

📊 Sentiment Analysis modell betöltése...
✅ Sentiment Analysis modell betöltve!

Szöveg: I love this amazing AI technology! It's fantastic!
➜ Eredmény: POSITIVE (Bizonyosság: 99.98%)

Szöveg: This is terrible and disappointing.
➜ Eredmény: NEGATIVE (Bizonyosság: 99.97%)

[... további demo eredmények ...]
```

### 2. Interaktív Mód (Saját Adatok Tesztelése)

Az interaktív módban saját szövegeket és képeket próbálhatsz ki:

```bash
python ai_app.py --interactive
```

**Menü navigáció:**
```
============================================================
🤖 INTERAKTÍV MÓD
============================================================

Válassz egy funkciót:
1. Sentiment Analysis
2. Question Answering
3. Text Summarization
4. Image Classification
0. Kilépés

Választás (0-4): 
```

**Példa interakció - Sentiment Analysis:**
```
Választás (0-4): 1
Add meg a szöveget: This product exceeded all my expectations!
➜ POSITIVE (99.87%)
```

**Példa interakció - Question Answering:**
```
Választás (0-4): 2
Add meg a kontextust: Python was created by Guido van Rossum and first released in 1991.
Add meg a kérdést: When was Python released?
➜ 1991 (98.45%)
```

### 3. Python Kódból (Programozói Használat)

Saját Python scriptek írásához:

```python
from ai_app import HuggingFaceAI

# AI objektum létrehozása
ai = HuggingFaceAI()

# 1. Sentiment Analysis
result = ai.analyze_sentiment("This is an amazing product!")
print(f"Sentiment: {result['label']} ({result['score']:.2%})")

# 2. Question Answering
context = "The Eiffel Tower is located in Paris, France."
question = "Where is the Eiffel Tower?"
answer = ai.answer_question(context, question)
print(f"Answer: {answer['answer']}")

# 3. Text Summarization
long_text = """[hosszú szöveg ide]"""
summary = ai.summarize_text(long_text)
print(f"Summary: {summary}")

# 4. Image Classification
results = ai.classify_image("path/to/image.jpg")
for r in results[:3]:
    print(f"{r['label']}: {r['score']:.2%}")
```

## 📚 Részletes Funkció Leírások

### 1. Sentiment Analysis (Hangulatelemzés)

**Mit csinál?**
Meghatározza egy szöveg érzelmi töltetét (pozitív, negatív, semleges).

**Használati példák:**
- Vásárlói vélemények elemzése
- Közösségi média posztok hangulatelemzése
- Ügyfélszolgálati visszajelzések értékelése
- Termékrecenziók automatikus kategorizálása

**Python kód:**
```python
ai = HuggingFaceAI()
result = ai.analyze_sentiment("I love this product!")
# Eredmény: {'label': 'POSITIVE', 'score': 0.9998}
```

**Parancssorból:**
```bash
python ai_app.py --interactive
# Válassz 1-et, add meg a szöveget
```

**Kimenet értelmezése:**
- `label`: POSITIVE vagy NEGATIVE
- `score`: 0-1 közötti bizonyossági érték (pl. 0.95 = 95%)

### 2. Question Answering (Kérdés-Válasz)

**Mit csinál?**
Megválaszol kérdéseket egy adott szöveges kontextus alapján.

**Használati példák:**
- FAQ rendszerek
- Dokumentum-alapú keresés
- Tudásbázis lekérdezések
- Oktatási anyagok feldolgozása

**Python kód:**
```python
ai = HuggingFaceAI()
context = """
Machine learning is a subset of artificial intelligence.
It focuses on the development of computer programs that can
access data and use it to learn for themselves.
"""
question = "What is machine learning?"
answer = ai.answer_question(context, question)
print(f"Válasz: {answer['answer']}")
print(f"Bizonyosság: {answer['score']:.2%}")
```

**Tippek a jobb eredményekért:**
- A kontextusban szerepeljen a válasz
- Világos, konkrét kérdéseket tegyél fel
- Kerüld a túl általános kérdéseket

### 3. Text Summarization (Szövegösszefoglalás)

**Mit csinál?**
Hosszú szövegeket rövid, lényegre törő összefoglalásokká alakít.

**Használati példák:**
- Hírcikkek összefoglalása
- Kutatási anyagok rövidítése
- Meeting jegyzőkönyvek összegzése
- Email-ek főbb pontjainak kiemelése

**Python kód:**
```python
ai = HuggingFaceAI()
long_article = """
[Több bekezdésnyi hosszú szöveg...]
"""
summary = ai.summarize_text(
    long_article,
    max_length=130,  # Maximum összefoglaló hossz
    min_length=30     # Minimum összefoglaló hossz
)
print(summary)
```

**Paraméterek beállítása:**
- `max_length`: Maximum token szám az összefoglalásban (alapértelmezett: 130)
- `min_length`: Minimum token szám (alapértelmezett: 30)
- Hosszabb szövegekhez növeld a `max_length` értéket

### 4. Image Classification (Képosztályozás)

**Mit csinál?**
Felismeri és kategorizálja a képeken található objektumokat.

**Használati példák:**
- Termékfotók automatikus címkézése
- Állatfajok azonosítása
- Tárgyi eszközök felismerése
- Minőségellenőrzés képek alapján

**Python kód - Lokális fájl:**
```python
ai = HuggingFaceAI()
results = ai.classify_image("cat.jpg")
for i, result in enumerate(results[:5], 1):
    print(f"{i}. {result['label']}: {result['score']:.2%}")
```

**Python kód - URL-ről:**
```python
ai = HuggingFaceAI()
url = "https://example.com/dog.jpg"
results = ai.classify_image(url)
print(f"Top eredmény: {results[0]['label']}")
```

**Támogatott formátumok:**
- JPG/JPEG
- PNG
- BMP
- GIF
- WEBP

## ⚙️ Haladó Beállítások

### GPU Használat

Ha van NVIDIA GPU-d és telepítve van a CUDA:

```python
import torch
print(f"GPU elérhető: {torch.cuda.is_available()}")
print(f"GPU név: {torch.cuda.get_device_name(0)}")
```

Az alkalmazás automatikusan használja a GPU-t, ha elérhető.

### Különböző Modellek Használata

Lecserélheted az alapértelmezett modelleket:

```python
from transformers import pipeline

# Magyar nyelvű sentiment analysis
sentiment = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Fordítás angolról magyarra
translator = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-hu"
)
```

### Batch Feldolgozás (Több Elem Egyszerre)

Hatékonyabb több elem feldolgozásakor:

```python
ai = HuggingFaceAI()
texts = [
    "First text to analyze",
    "Second text to analyze",
    "Third text to analyze"
]

# A pipeline támogatja a batch-et
for text in texts:
    result = ai.analyze_sentiment(text)
    print(f"{text}: {result['label']}")
```

## 🔍 Hibaelhárítás

### Probléma: Modellek nem töltődnek le

**Megoldások:**
1. Ellenőrizd az internet kapcsolatot
2. Próbáld meg VPN nélkül
3. Tisztítsd a cache-t: `rm -rf ~/.cache/huggingface/`
4. Manuális letöltés: `huggingface-cli download model_name`

### Probléma: OutOfMemoryError

**Megoldások:**
1. Használj kisebb modelleket
2. Csökkentsd a batch size-t
3. Zárj be más programokat
4. GPU esetén csökkentsd a `max_length` paramétert

### Probléma: Lassú feldolgozás

**Megoldások:**
1. Használj GPU-t, ha van
2. Csökkentsd a modell méretét
3. Batch feldolgozás használata
4. Quantized modellek használata

### Probléma: Import Error

```bash
# Újratelepítés
pip uninstall transformers torch
pip install -r requirements.txt

# Vagy specifikus verziók
pip install transformers==4.35.0 torch==2.0.0
```

## 📊 Teljesítmény Optimalizálás

### CPU vs GPU Sebesség

| Feladat | CPU (Core i7) | GPU (RTX 3060) |
|---------|---------------|----------------|
| Sentiment Analysis | ~0.5s | ~0.1s |
| Question Answering | ~1.0s | ~0.2s |
| Summarization | ~3.0s | ~0.5s |
| Image Classification | ~1.5s | ~0.3s |

### Memória Használat

- Sentiment Analysis: ~1 GB RAM
- Question Answering: ~1.5 GB RAM
- Summarization: ~2 GB RAM
- Image Classification: ~1 GB RAM

## 🌍 Nemzetközi Használat

### Magyar Nyelv Támogatás

```python
from transformers import pipeline

# Magyar szöveg elemzése
sentiment_hu = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

result = sentiment_hu("Ez egy fantasztikus termék!")
print(result)
```

### Fordítás

```python
# Angol -> Magyar
translator = pipeline("translation_en_to_hu", model="Helsinki-NLP/opus-mt-en-hu")
result = translator("Hello, how are you?")
print(result[0]['translation_text'])  # "Szia, hogy vagy?"
```

## 📝 Best Practices

1. **Modellek Cache-elése**: Az első futtatás után a modellek gyorsabban betöltődnek
2. **Hibakezelés**: Mindig használj try-except blokkokat production kódban
3. **Batch Processing**: Több elem feldolgozásakor használj batch-eket
4. **Resource Management**: Használj context managereket vagy `del` objektumokat, ha már nincs rájuk szükség
5. **Logging**: Implementálj megfelelő loggolást debug célokra

## 🎓 További Tanulási Források

- [Hugging Face Dokumentáció](https://huggingface.co/docs)
- [Transformers Tutorial](https://huggingface.co/course)
- [Model Hub](https://huggingface.co/models)
- [Datasets Hub](https://huggingface.co/datasets)

## 💡 Projekt Ötletek

1. **Automatikus Email Rendező**: Kategorizálja emaileket sentiment alapján
2. **FAQ Bot**: Építs chatbotot a question answering használatával
3. **Hírek Összefoglalója**: Napi hírek automatikus összegzése
4. **Fotó Katalogizáló**: Automatikus képcímkézés nagy fotógyűjteményekhez
5. **Közösségi Média Monitor**: Márka említések sentiment elemzése

## 🤝 Közreműködés és Fejlesztés

Ha szeretnél hozzájárulni a projekthez:

1. Fork-old a repository-t
2. Készíts egy új branch-et (`git checkout -b feature/UjFunkció`)
3. Commit-old a változtatásokat (`git commit -m 'Új funkció hozzáadása'`)
4. Push-old a branch-et (`git push origin feature/UjFunkció`)
5. Nyiss egy Pull Request-et

## 📄 Licenc

MIT License - Lásd a LICENSE fájlt a részletekért.

## ❓ Gyakori Kérdések (FAQ)

**K: Működik offline is?**  
V: Igen, miután egyszer letöltötted a modelleket.

**K: Mennyire pontosak az eredmények?**  
V: A modellek általában 85-95% pontosságúak, de ez függ a feladattól és a bemenet minőségétől.

**K: Támogat más nyelveket is?**  
V: Igen, cserélheted a modelleket multilingual verziókra.

**K: Használhatom kereskedelmi célokra?**  
V: Ellenőrizd az egyes modellek licencét a Hugging Face Hub-on.

**K: Mennyire biztonságos?**  
V: A modellek lokálisan futnak, nincs adatküldés külső szerverekre.

---

**Utolsó frissítés:** 2024. november  
**Verzió:** 1.0  
**Szerző:** ML Practice Research Team
