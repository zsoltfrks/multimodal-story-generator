"""
Hugging Face AI Alkalmazás - Példa Használat

Ez a fájl bemutatja, hogyan használható az ai_app.py különböző AI feladatokra.
Tartalma: kód példák és várható eredmények dokumentálása.
"""

# ============================================================================
# 1. SENTIMENT ANALYSIS - Hangulatelemzés
# ============================================================================

"""
Példa használat:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

# Pozitív szöveg elemzése
result = ai.analyze_sentiment("I love this amazing technology!")
print(result)
# Várható kimenet:
# {'label': 'POSITIVE', 'score': 0.9998}

# Negatív szöveg elemzése
result = ai.analyze_sentiment("This is terrible and disappointing.")
print(result)
# Várható kimenet:
# {'label': 'NEGATIVE', 'score': 0.9997}

# Semleges szöveg elemzése
result = ai.analyze_sentiment("The weather is normal today.")
print(result)
# Várható kimenet:
# {'label': 'NEUTRAL', 'score': 0.8523}
"""


# ============================================================================
# 2. QUESTION ANSWERING - Kérdés-válasz rendszer
# ============================================================================

"""
Példa használat:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

context = '''
Hugging Face is a company that develops tools for building applications using 
machine learning. It is most notable for its Transformers library built for 
natural language processing applications and its platform that allows users 
to share machine learning models and datasets. The company was founded in 2016 
in New York City and is now based in Paris, France.
'''

# Kérdés 1: Alapítás éve
question = "When was Hugging Face founded?"
answer = ai.answer_question(context, question)
print(f"Kérdés: {question}")
print(f"Válasz: {answer['answer']}")
print(f"Bizonyosság: {answer['score']:.2%}")
# Várható kimenet:
# Kérdés: When was Hugging Face founded?
# Válasz: 2016
# Bizonyosság: 99.87%

# Kérdés 2: Helyszín
question = "Where is Hugging Face based?"
answer = ai.answer_question(context, question)
print(f"Kérdés: {question}")
print(f"Válasz: {answer['answer']}")
# Várható kimenet:
# Válasz: Paris, France

# Kérdés 3: Termék információ
question = "What is Transformers library used for?"
answer = ai.answer_question(context, question)
print(f"Válasz: {answer['answer']}")
# Várható kimenet:
# Válasz: natural language processing applications
"""


# ============================================================================
# 3. TEXT SUMMARIZATION - Szöveg összefoglalás
# ============================================================================

"""
Példa használat:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

long_text = '''
Artificial intelligence (AI) is intelligence demonstrated by machines, as 
opposed to natural intelligence displayed by animals including humans. AI 
research has been defined as the field of study of intelligent agents, which 
refers to any system that perceives its environment and takes actions that 
maximize its chance of achieving its goals. The term "artificial intelligence" 
had previously been used to describe machines that mimic and display "human" 
cognitive skills that are associated with the human mind, such as "learning" 
and "problem-solving". This definition has since been rejected by major AI 
researchers who now describe AI in terms of rationality and acting rationally, 
which does not limit how intelligence can be articulated. AI applications 
include advanced web search engines, recommendation systems, understanding 
human speech, self-driving cars, automated decision-making and competing at 
the highest level in strategic game systems.
'''

summary = ai.summarize_text(long_text)
print(f"Eredeti szöveg hossza: {len(long_text)} karakter")
print(f"Összefoglalás hossza: {len(summary)} karakter")
print(f"Összefoglalás: {summary}")

# Várható kimenet:
# Eredeti szöveg hossza: 869 karakter
# Összefoglalás hossza: 145 karakter
# Összefoglalás: Artificial intelligence (AI) is intelligence demonstrated by 
# machines. AI research has been defined as the field of study of intelligent 
# agents. AI applications include advanced web search engines, recommendation 
# systems, self-driving cars and more.
"""


# ============================================================================
# 4. IMAGE CLASSIFICATION - Képosztályozás
# ============================================================================

"""
Példa használat:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

# Helyi kép fájl elemzése
results = ai.classify_image("path/to/cat.jpg")
print("Top 3 eredmény:")
for i, result in enumerate(results[:3], 1):
    print(f"{i}. {result['label']}: {result['score']:.2%}")

# Várható kimenet (macskás kép esetén):
# Top 3 eredmény:
# 1. tabby cat: 45.32%
# 2. Egyptian cat: 32.18%
# 3. tiger cat: 12.45%

# URL-ről történő kép elemzése
image_url = "https://example.com/dog.jpg"
results = ai.classify_image(image_url)
print("Top 5 eredmény:")
for i, result in enumerate(results[:5], 1):
    print(f"{i}. {result['label']}: {result['score']:.2%}")

# Várható kimenet (kutyás kép esetén):
# Top 5 eredmény:
# 1. golden retriever: 67.89%
# 2. Labrador retriever: 18.23%
# 3. cocker spaniel: 5.67%
# 4. Irish setter: 3.45%
# 5. dog: 2.34%
"""


# ============================================================================
# 5. INTERAKTÍV HASZNÁLAT - Parancssorból
# ============================================================================

"""
Az alkalmazás két módban futtatható:

1. DEMO MÓD (alapértelmezett):
   python ai_app.py
   
   Ez automatikusan végigfuttatja az összes demo funkciót és megmutatja
   az eredményeket.

2. INTERAKTÍV MÓD:
   python ai_app.py --interactive
   
   Ez elindít egy interaktív menüt, ahol manuálisan kiválaszthatod,
   melyik funkciót szeretnéd használni és saját adatokat adhatsz meg.
   
   Menü opciók:
   1. Sentiment Analysis - Saját szöveg hangulatelemzése
   2. Question Answering - Kérdés megválaszolása kontextus alapján
   3. Text Summarization - Hosszú szöveg összefoglalása
   4. Image Classification - Kép objektumfelismerés
   0. Kilépés
"""


# ============================================================================
# 6. PYTHON KÓDBÓL TÖRTÉNŐ HASZNÁLAT
# ============================================================================

"""
Teljes példa program:

#!/usr/bin/env python3
from ai_app import HuggingFaceAI

def main():
    # AI objektum létrehozása
    ai = HuggingFaceAI()
    
    # 1. Vásárlói vélemények elemzése
    reviews = [
        "This product is amazing! Best purchase ever!",
        "Terrible quality, broke after one day.",
        "It's okay, nothing special."
    ]
    
    print("Vásárlói vélemények elemzése:")
    for review in reviews:
        result = ai.analyze_sentiment(review)
        print(f"  '{review[:30]}...' -> {result['label']}")
    
    # 2. FAQ rendszer
    faq_context = '''
    Our store is open Monday to Friday from 9 AM to 6 PM.
    We offer free shipping on orders over $50.
    Returns are accepted within 30 days of purchase.
    '''
    
    questions = [
        "What are the opening hours?",
        "Do you offer free shipping?",
        "What is the return policy?"
    ]
    
    print("\nFAQ válaszok:")
    for q in questions:
        answer = ai.answer_question(faq_context, q)
        print(f"  Q: {q}")
        print(f"  A: {answer['answer']}")
    
    # 3. Termékleírás összefoglalása
    product_desc = '''
    [Hosszú termékleírás szövege...]
    '''
    summary = ai.summarize_text(product_desc)
    print(f"\nTerméköszszefoglalás: {summary}")
    
    # 4. Termékképek automatikus címkézése
    images = ["product1.jpg", "product2.jpg", "product3.jpg"]
    print("\nTermékképek elemzése:")
    for img in images:
        try:
            results = ai.classify_image(img)
            print(f"  {img}: {results[0]['label']}")
        except Exception as e:
            print(f"  {img}: Hiba - {e}")

if __name__ == "__main__":
    main()
"""


# ============================================================================
# 7. HASZNOS TIPPEK ÉS MEGJEGYZÉSEK
# ============================================================================

"""
MODELLEK LETÖLTÉSE:
- Az első futtatáskor a modellek automatikusan letöltődnek a Hugging Face-ről
- A modellek a ~/.cache/huggingface/ könyvtárba kerülnek mentésre
- Nagyobb modellek esetén a letöltés több percig is tarthat
- Internet kapcsolat szükséges az első futtatáshoz

TELJESÍTMÉNY:
- GPU használata jelentősen felgyorsítja a feldolgozást
- CPU-n is működik, de lassabban
- A pipeline() automatikusan felismeri és használja a GPU-t, ha elérhető

TESTRESZABÁS:
- Különböző modellek használhatók a pipeline() függvényben
- Példa: pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
- Magyar nyelvre is vannak modellek: keress "hungarian" kulcsszóra a Hugging Face-en

HIBAELHÁRÍTÁS:
- Ha nem töltődnek le a modellek, ellenőrizd az internet kapcsolatot
- OutOfMemory hiba esetén használj kisebb modelleket
- CUDA hibák esetén ellenőrizd a PyTorch és CUDA kompatibilitást

TOVÁBBI FUNKCIÓK:
- Translation (fordítás): pipeline("translation", model="Helsinki-NLP/opus-mt-en-hu")
- Named Entity Recognition: pipeline("ner")
- Text Generation: pipeline("text-generation")
- Zero-shot Classification: pipeline("zero-shot-classification")
"""
