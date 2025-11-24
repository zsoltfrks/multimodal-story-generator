# ml-practice-research

Practice project for an ML based university project.

## 🤖 Hugging Face AI Alkalmazás

Ez egy multimodális AI alkalmazás, amely a [Hugging Face](https://huggingface.co/models) modelljeivel működik.

### ✨ Funkciók

Az alkalmazás négy fő AI képességet támogat:

1. **Sentiment Analysis (Hangulatelemzés)** - Szövegek érzelmi töltetének elemzése
2. **Question Answering (Kérdés-válasz)** - Kérdések megválaszolása szöveges kontextus alapján
3. **Text Summarization (Szöveg összefoglalás)** - Hosszú szövegek automatikus összefoglalása
4. **Image Classification (Képosztályozás)** - Képeken található objektumok felismerése

### 📋 Telepítés

#### Követelmények
- Python 3.8 vagy újabb
- pip package manager

#### Lépések

1. **Repository klónozása**
```bash
git clone https://github.com/zsoltfrks/ml-practice-research.git
cd ml-practice-research
```

2. **Virtuális környezet létrehozása (ajánlott)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# vagy
venv\Scripts\activate  # Windows
```

3. **Függőségek telepítése**
```bash
pip install -r requirements.txt
```

### 🚀 Használat

#### Demo mód

A demo mód automatikusan bemutatja mind a négy AI funkciót:

```bash
python ai_app.py
```

#### Interaktív mód

Az interaktív módban saját szövegeket és képeket próbálhatsz ki:

```bash
python ai_app.py --interactive
```

### 📚 Példák

#### Sentiment Analysis
```python
from ai_app import HuggingFaceAI

ai = HuggingFaceAI()
result = ai.analyze_sentiment("I love this amazing technology!")
print(result)
# {'label': 'POSITIVE', 'score': 0.9998}
```

#### Question Answering
```python
ai = HuggingFaceAI()
context = "Hugging Face was founded in 2016 in New York."
question = "When was Hugging Face founded?"
answer = ai.answer_question(context, question)
print(answer['answer'])  # "2016"
```

#### Text Summarization
```python
ai = HuggingFaceAI()
long_text = "..." # hosszú szöveg
summary = ai.summarize_text(long_text)
print(summary)
```

#### Image Classification
```python
ai = HuggingFaceAI()
results = ai.classify_image("path/to/image.jpg")
# vagy URL:
results = ai.classify_image("https://example.com/image.jpg")
print(results)
```

### 🔧 Használt Modellek

Az alkalmazás a következő Hugging Face modelleket használja:

- **Sentiment Analysis**: distilbert-base-uncased-finetuned-sst-2-english
- **Question Answering**: distilbert-base-cased-distilled-squad
- **Summarization**: facebook/bart-large-cnn
- **Image Classification**: google/vit-base-patch16-224

### 📖 További információk

- [Hugging Face Modellek](https://huggingface.co/models)
- [Transformers Dokumentáció](https://huggingface.co/docs/transformers)
- [Pipeline API](https://huggingface.co/docs/transformers/main_classes/pipelines)

### 🤝 Közreműködés

Ez egy egyetemi gyakorló projekt. Javaslatokat és fejlesztéseket szívesen fogadunk!

### 📝 Licenc

MIT License
