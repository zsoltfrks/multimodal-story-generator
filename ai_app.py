"""
AI Application using Hugging Face Models
A multimodal AI application for text and image processing.
"""

from transformers import pipeline
from PIL import Image
import requests
from io import BytesIO
import sys


class HuggingFaceAI:
    """
    AI application using Hugging Face models.
    Capabilities: text processing, image processing, image captioning, story generation.
    """
    
    def __init__(self):
        self.sentiment_analyzer = None
        self.qa_model = None
        self.image_classifier = None
        self.summarizer = None
        self.image_captioner = None
        self.story_generator = None
        
    def load_sentiment_analyzer(self):
        """Load sentiment analysis model"""
        print("📊 Loading Sentiment Analysis model...")
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        print("✅ Sentiment Analysis model loaded!")
        
    def load_qa_model(self):
        """Load Question Answering model"""
        print("❓ Loading Question Answering model...")
        self.qa_model = pipeline("question-answering")
        print("✅ Question Answering model loaded!")
        
    def load_summarizer(self):
        """Load text summarization model"""
        print("📝 Loading Summarization model...")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        print("✅ Summarization model loaded!")
        
    def load_image_classifier(self):
        """Load image classification model"""
        print("🖼️  Loading Image Classification model...")
        self.image_classifier = pipeline("image-classification")
        print("✅ Image Classification model loaded!")
    
    def load_image_captioner(self):
        """Load image captioning model (BLIP)"""
        print("📷 Loading Image Captioning model (BLIP)...")
        self.image_captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
        print("✅ Image Captioning model loaded!")
    
    def load_story_generator(self):
        """Load story generation model"""
        print("📖 Loading Story Generation model...")
        self.story_generator = pipeline("text-generation", model="gpt2")
        print("✅ Story Generation model loaded!")
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of text.
        
        Args:
            text: The text to analyze
            
        Returns:
            Sentiment analysis result
        """
        if not self.sentiment_analyzer:
            self.load_sentiment_analyzer()
        
        result = self.sentiment_analyzer(text)[0]
        return result
    
    def answer_question(self, context, question):
        """
        Answer question based on text context.
        
        Args:
            context: The context text
            question: The question
            
        Returns:
            The answer
        """
        if not self.qa_model:
            self.load_qa_model()
        
        result = self.qa_model(question=question, context=context)
        return result
    
    def summarize_text(self, text, max_length=130, min_length=30):
        """
        Summarize text.
        
        Args:
            text: The text to summarize
            max_length: Maximum summary length
            min_length: Minimum summary length
            
        Returns:
            The summary
        """
        if not self.summarizer:
            self.load_summarizer()
        
        result = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return result[0]['summary_text']
    
    def classify_image(self, image_path_or_url):
        """
        Classify image / object recognition.
        
        Args:
            image_path_or_url: Image file path or URL
            
        Returns:
            Classification results
        """
        if not self.image_classifier:
            self.load_image_classifier()
        
        # Handle URL or local file
        if image_path_or_url.startswith('http'):
            try:
                response = requests.get(image_path_or_url, timeout=10)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
            except requests.exceptions.RequestException as e:
                raise ValueError(f"Error downloading image: {e}")
        else:
            image = Image.open(image_path_or_url)
        
        results = self.image_classifier(image)
        return results
    
    def caption_image(self, image_path_or_url):
        """
        Generate a kid-friendly description of an image using BLIP.
        
        Args:
            image_path_or_url: Image file path or URL
            
        Returns:
            Image caption/description
        """
        if not self.image_captioner:
            self.load_image_captioner()
        
        # Handle URL or local file
        if image_path_or_url.startswith('http'):
            try:
                response = requests.get(image_path_or_url, timeout=10)
                response.raise_for_status()
                image = Image.open(BytesIO(response.content))
            except requests.exceptions.RequestException as e:
                raise ValueError(f"Error downloading image: {e}")
        else:
            image = Image.open(image_path_or_url)
        
        result = self.image_captioner(image)
        return result[0]['generated_text']
    
    def generate_story(self, image_description, max_length=200):
        """
        Generate a short children's story based on an image description.
        
        Args:
            image_description: Description of the image (from caption_image)
            max_length: Maximum story length in tokens
            
        Returns:
            Generated children's story
        """
        if not self.story_generator:
            self.load_story_generator()
        
        prompt = f"Write a short, cute children's story in 6-8 sentences based on this description: {image_description}\n\nOnce upon a time,"
        
        result = self.story_generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            do_sample=True,
            temperature=0.8,
            top_p=0.9
        )
        
        generated_text = result[0]['generated_text']
        # Extract just the story part (after the prompt)
        story_start = generated_text.find("Once upon a time,")
        if story_start != -1:
            return generated_text[story_start:]
        return generated_text
    
    def image_to_story(self, image_path_or_url, max_story_length=200):
        """
        Generate a children's story from an image (combines captioning and story generation).
        
        Args:
            image_path_or_url: Image file path or URL
            max_story_length: Maximum story length in tokens
            
        Returns:
            Dictionary with caption and story
        """
        # Step 1: Generate image caption
        caption = self.caption_image(image_path_or_url)
        
        # Step 2: Generate story from caption
        story = self.generate_story(caption, max_length=max_story_length)
        
        return {
            'caption': caption,
            'story': story
        }


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
        print(f"\nText: {text}")
        result = ai.analyze_sentiment(text)
        print(f"➜ Result: {result['label']} (Confidence: {result['score']:.2%})")


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
    
    print(f"\nContext: {context[:100]}...")
    
    for question in questions:
        print(f"\nQuestion: {question}")
        result = ai.answer_question(context, question)
        print(f"➜ Answer: {result['answer']} (Confidence: {result['score']:.2%})")


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
    
    print(f"\nOriginal text ({len(text)} characters):")
    print(text)
    
    summary = ai.summarize_text(text)
    print(f"\nSummary ({len(summary)} characters):")
    print(f"➜ {summary}")


def demo_image_classification(ai):
    """Image classification demo"""
    print("\n" + "="*60)
    print("🖼️  IMAGE CLASSIFICATION DEMO")
    print("="*60)
    
    # Example image URLs
    image_urls = [
        "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
    ]
    
    for url in image_urls:
        print(f"\nAnalyzing image: {url}")
        try:
            results = ai.classify_image(url)
            print("➜ Top 3 results:")
            for i, result in enumerate(results[:3], 1):
                print(f"   {i}. {result['label']}: {result['score']:.2%}")
        except Exception as e:
            print(f"   ⚠️  Error: {e}")


def demo_image_captioning(ai):
    """Image captioning demo"""
    print("\n" + "="*60)
    print("📷 IMAGE CAPTIONING DEMO")
    print("="*60)
    
    # Example image URLs
    image_urls = [
        "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg",
    ]
    
    for url in image_urls:
        print(f"\nGenerating caption for: {url}")
        try:
            caption = ai.caption_image(url)
            print(f"➜ Caption: {caption}")
        except Exception as e:
            print(f"   ⚠️  Error: {e}")


def demo_image_to_story(ai):
    """Image to children's story demo"""
    print("\n" + "="*60)
    print("📖 IMAGE TO CHILDREN'S STORY DEMO")
    print("="*60)
    
    # Example image URL
    image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"
    
    print(f"\nGenerating story from image: {image_url}")
    try:
        result = ai.image_to_story(image_url)
        print(f"\n📷 Image Caption: {result['caption']}")
        print(f"\n📖 Generated Story:\n{result['story']}")
    except Exception as e:
        print(f"   ⚠️  Error: {e}")


def interactive_mode(ai):
    """Interactive mode with user input"""
    print("\n" + "="*60)
    print("🤖 INTERACTIVE MODE")
    print("="*60)
    print("\nChoose a feature:")
    print("1. Sentiment Analysis")
    print("2. Question Answering")
    print("3. Text Summarization")
    print("4. Image Classification")
    print("5. Image Captioning (BLIP)")
    print("6. Image to Story (for children)")
    print("0. Exit")
    
    while True:
        choice = input("\nChoice (0-6): ").strip()
        
        if choice == "0":
            print("Goodbye! 👋")
            break
        elif choice == "1":
            text = input("Enter the text: ")
            result = ai.analyze_sentiment(text)
            print(f"➜ {result['label']} ({result['score']:.2%})")
        elif choice == "2":
            context = input("Enter the context: ")
            question = input("Enter the question: ")
            result = ai.answer_question(context, question)
            print(f"➜ {result['answer']} ({result['score']:.2%})")
        elif choice == "3":
            text = input("Enter the text (longer): ")
            summary = ai.summarize_text(text)
            print(f"➜ {summary}")
        elif choice == "4":
            path = input("Enter the image URL or path: ")
            results = ai.classify_image(path)
            print("➜ Top 3:")
            for i, r in enumerate(results[:3], 1):
                print(f"   {i}. {r['label']}: {r['score']:.2%}")
        elif choice == "5":
            path = input("Enter the image URL or path: ")
            caption = ai.caption_image(path)
            print(f"➜ Caption: {caption}")
        elif choice == "6":
            path = input("Enter the image URL or path: ")
            result = ai.image_to_story(path)
            print(f"\n📷 Caption: {result['caption']}")
            print(f"\n📖 Story:\n{result['story']}")
        else:
            print("Invalid choice!")


def main():
    """Main program"""
    print("="*60)
    print("🚀 HUGGING FACE AI APPLICATION")
    print("="*60)
    print("\nMultimodal AI application for text and image processing")
    print("Model source: https://huggingface.co/models\n")
    
    ai = HuggingFaceAI()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode(ai)
    else:
        # Running in demo mode
        print("\n💡 Demo mode - showcasing different AI capabilities")
        print("   (Use --interactive flag for interactive mode)\n")
        
        try:
            demo_sentiment_analysis(ai)
            demo_question_answering(ai)
            demo_summarization(ai)
            demo_image_classification(ai)
            demo_image_captioning(ai)
            demo_image_to_story(ai)
            
            print("\n" + "="*60)
            print("✨ DEMO COMPLETE")
            print("="*60)
            print("\nMore options:")
            print("- Run again with --interactive flag for interactive mode")
            print("- Check the code for further customization")
            
        except KeyboardInterrupt:
            print("\n\n⏸️  Program interrupted")
        except Exception as e:
            print(f"\n❌ Error occurred: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
