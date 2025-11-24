"""
AI Application using Hugging Face Models
Multimodális AI alkalmazás szöveg- és képfeldolgozáshoz
"""

from transformers import pipeline
from PIL import Image
import requests
from io import BytesIO
import sys


class HuggingFaceAI:
    """
    Hugging Face modelleket használó AI alkalmazás
    Képességek: szöveg-feldolgozás, képfeldolgozás
    """
    
    def __init__(self):
        self.sentiment_analyzer = None
        self.qa_model = None
        self.image_classifier = None
        self.summarizer = None
        
    def load_sentiment_analyzer(self):
        """Sentiment analysis modell betöltése"""
        print("📊 Sentiment Analysis modell betöltése...")
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        print("✅ Sentiment Analysis modell betöltve!")
        
    def load_qa_model(self):
        """Question Answering modell betöltése"""
        print("❓ Question Answering modell betöltése...")
        self.qa_model = pipeline("question-answering")
        print("✅ Question Answering modell betöltve!")
        
    def load_summarizer(self):
        """Text summarization modell betöltése"""
        print("📝 Summarization modell betöltése...")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        print("✅ Summarization modell betöltve!")
        
    def load_image_classifier(self):
        """Image classification modell betöltése"""
        print("🖼️  Image Classification modell betöltése...")
        self.image_classifier = pipeline("image-classification")
        print("✅ Image Classification modell betöltve!")
    
    def analyze_sentiment(self, text):
        """
        Szöveg hangulatelemzése
        
        Args:
            text: Az elemzendő szöveg
            
        Returns:
            A sentiment elemzés eredménye
        """
        if not self.sentiment_analyzer:
            self.load_sentiment_analyzer()
        
        result = self.sentiment_analyzer(text)[0]
        return result
    
    def answer_question(self, context, question):
        """
        Kérdés megválaszolása szöveg kontextus alapján
        
        Args:
            context: A kontextus szöveg
            question: A kérdés
            
        Returns:
            A válasz
        """
        if not self.qa_model:
            self.load_qa_model()
        
        result = self.qa_model(question=question, context=context)
        return result
    
    def summarize_text(self, text, max_length=130, min_length=30):
        """
        Szöveg összefoglalása
        
        Args:
            text: Az összefoglalandó szöveg
            max_length: Maximum összefoglaló hossz
            min_length: Minimum összefoglaló hossz
            
        Returns:
            Az összefoglalás
        """
        if not self.summarizer:
            self.load_summarizer()
        
        result = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]['summary_text']
    
    def classify_image(self, image_path_or_url):
        """
        Kép osztályozása / objektumfelismerés
        
        Args:
            image_path_or_url: Kép fájl útvonala vagy URL
            
        Returns:
            Az osztályozás eredménye
        """
        if not self.image_classifier:
            self.load_image_classifier()
        
        # URL vagy lokális fájl kezelése
        if image_path_or_url.startswith('http'):
            try:
                response = requests.get(image_path_or_url, timeout=10)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
            except requests.exceptions.RequestException as e:
                raise ValueError(f"Hiba a kép letöltésekor: {e}")
        else:
            image = Image.open(image_path_or_url)
        
        results = self.image_classifier(image)
        return results


def demo_sentiment_analysis(ai):
    """Sentiment analysis demo"""
    print("\n" + "="*60)
    print("🎭 SENTIMENT ANALYSIS DEMO")
    print("="*60)
    
    texts = [
        "I love this amazing AI technology! It's fantastic!",
        "This is terrible and disappointing.",
        "The weather is normal today."
    ]
    
    for text in texts:
        print(f"\nSzöveg: {text}")
        result = ai.analyze_sentiment(text)
        print(f"➜ Eredmény: {result['label']} (Bizonyosság: {result['score']:.2%})")


def demo_question_answering(ai):
    """Question answering demo"""
    print("\n" + "="*60)
    print("❓ QUESTION ANSWERING DEMO")
    print("="*60)
    
    context = """
    Hugging Face is a company that develops tools for building applications using machine learning.
    It is most notable for its Transformers library built for natural language processing applications
    and its platform that allows users to share machine learning models and datasets. The company was
    founded in 2016 in New York City and is now based in Paris, France.
    """
    
    questions = [
        "When was Hugging Face founded?",
        "Where is Hugging Face based?",
        "What is Transformers library used for?"
    ]
    
    print(f"\nKontextus: {context[:100]}...")
    
    for question in questions:
        print(f"\nKérdés: {question}")
        result = ai.answer_question(context, question)
        print(f"➜ Válasz: {result['answer']} (Bizonyosság: {result['score']:.2%})")


def demo_summarization(ai):
    """Text summarization demo"""
    print("\n" + "="*60)
    print("📝 TEXT SUMMARIZATION DEMO")
    print("="*60)
    
    text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to natural
    intelligence displayed by animals including humans. AI research has been defined as the field
    of study of intelligent agents, which refers to any system that perceives its environment and
    takes actions that maximize its chance of achieving its goals. The term "artificial intelligence"
    had previously been used to describe machines that mimic and display "human" cognitive skills
    that are associated with the human mind, such as "learning" and "problem-solving". This definition
    has since been rejected by major AI researchers who now describe AI in terms of rationality and
    acting rationally, which does not limit how intelligence can be articulated. AI applications include
    advanced web search engines, recommendation systems, understanding human speech, self-driving cars,
    automated decision-making and competing at the highest level in strategic game systems.
    """
    
    print(f"\nEredeti szöveg ({len(text)} karakter):")
    print(text)
    
    summary = ai.summarize_text(text)
    print(f"\nÖsszefoglalás ({len(summary)} karakter):")
    print(f"➜ {summary}")


def demo_image_classification(ai):
    """Image classification demo"""
    print("\n" + "="*60)
    print("🖼️  IMAGE CLASSIFICATION DEMO")
    print("="*60)
    
    # Példa képek URL-jei
    image_urls = [
        "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
    ]
    
    for url in image_urls:
        print(f"\nKép elemzése: {url}")
        try:
            results = ai.classify_image(url)
            print("➜ Top 3 eredmény:")
            for i, result in enumerate(results[:3], 1):
                print(f"   {i}. {result['label']}: {result['score']:.2%}")
        except Exception as e:
            print(f"   ⚠️  Hiba: {e}")


def interactive_mode(ai):
    """Interaktív mód a felhasználói bemenettel"""
    print("\n" + "="*60)
    print("🤖 INTERAKTÍV MÓD")
    print("="*60)
    print("\nVálassz egy funkciót:")
    print("1. Sentiment Analysis")
    print("2. Question Answering")
    print("3. Text Summarization")
    print("4. Image Classification")
    print("0. Kilépés")
    
    while True:
        choice = input("\nVálasztás (0-4): ").strip()
        
        if choice == "0":
            print("Viszlát! 👋")
            break
        elif choice == "1":
            text = input("Add meg a szöveget: ")
            result = ai.analyze_sentiment(text)
            print(f"➜ {result['label']} ({result['score']:.2%})")
        elif choice == "2":
            context = input("Add meg a kontextust: ")
            question = input("Add meg a kérdést: ")
            result = ai.answer_question(context, question)
            print(f"➜ {result['answer']} ({result['score']:.2%})")
        elif choice == "3":
            text = input("Add meg a szöveget (hosszabb): ")
            summary = ai.summarize_text(text)
            print(f"➜ {summary}")
        elif choice == "4":
            path = input("Add meg a kép URL-jét vagy útvonalát: ")
            results = ai.classify_image(path)
            print("➜ Top 3:")
            for i, r in enumerate(results[:3], 1):
                print(f"   {i}. {r['label']}: {r['score']:.2%}")
        else:
            print("Érvénytelen választás!")


def main():
    """Főprogram"""
    print("="*60)
    print("🚀 HUGGING FACE AI ALKALMAZÁS")
    print("="*60)
    print("\nMultimodális AI alkalmazás szöveg- és képfeldolgozáshoz")
    print("Modell forrás: https://huggingface.co/models\n")
    
    ai = HuggingFaceAI()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode(ai)
    else:
        # Demo módban fut
        print("\n💡 Demo mód - különböző AI képességek bemutatása")
        print("   (Használd --interactive kapcsolót az interaktív módhoz)\n")
        
        try:
            demo_sentiment_analysis(ai)
            demo_question_answering(ai)
            demo_summarization(ai)
            demo_image_classification(ai)
            
            print("\n" + "="*60)
            print("✨ DEMO BEFEJEZVE")
            print("="*60)
            print("\nTovábbi lehetőségek:")
            print("- Futtasd újra --interactive kapcsolóval az interaktív módhoz")
            print("- Nézd meg a kódot további testreszabáshoz")
            
        except KeyboardInterrupt:
            print("\n\n⏸️  Program megszakítva")
        except Exception as e:
            print(f"\n❌ Hiba történt: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
