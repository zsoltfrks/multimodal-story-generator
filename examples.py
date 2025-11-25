"""
Hugging Face AI Application - Example Usage

This file demonstrates how to use ai_app.py for different AI tasks.
Contents: code examples and expected results documentation.
"""

# ============================================================================
# 1. SENTIMENT ANALYSIS - Emotional Tone Analysis
# ============================================================================

"""
Example usage:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

# Analyzing positive text
result = ai.analyze_sentiment("I love this amazing technology!")
print(result)
# Expected output:
# {'label': 'POSITIVE', 'score': 0.9998}

# Analyzing negative text
result = ai.analyze_sentiment("This is terrible and disappointing.")
print(result)
# Expected output:
# {'label': 'NEGATIVE', 'score': 0.9997}

# Analyzing neutral text
result = ai.analyze_sentiment("The weather is normal today.")
print(result)
# Expected output:
# {'label': 'NEUTRAL', 'score': 0.8523}
"""


# ============================================================================
# 2. QUESTION ANSWERING - Question-Answer System
# ============================================================================

"""
Example usage:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

context = '''
Hugging Face is a company that develops tools for building applications using 
machine learning. It is most notable for its Transformers library built for 
natural language processing applications and its platform that allows users 
to share machine learning models and datasets. The company was founded in 2016 
in New York City and is now based in Paris, France.
'''

# Question 1: Year of founding
question = "When was Hugging Face founded?"
answer = ai.answer_question(context, question)
print(f"Question: {question}")
print(f"Answer: {answer['answer']}")
print(f"Confidence: {answer['score']:.2%}")
# Expected output:
# Question: When was Hugging Face founded?
# Answer: 2016
# Confidence: 99.87%

# Question 2: Location
question = "Where is Hugging Face based?"
answer = ai.answer_question(context, question)
print(f"Question: {question}")
print(f"Answer: {answer['answer']}")
# Expected output:
# Answer: Paris, France

# Question 3: Product information
question = "What is Transformers library used for?"
answer = ai.answer_question(context, question)
print(f"Answer: {answer['answer']}")
# Expected output:
# Answer: natural language processing applications
"""


# ============================================================================
# 3. TEXT SUMMARIZATION - Text Summary
# ============================================================================

"""
Example usage:

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
print(f"Original text length: {len(long_text)} characters")
print(f"Summary length: {len(summary)} characters")
print(f"Summary: {summary}")

# Expected output:
# Original text length: 869 characters
# Summary length: 145 characters
# Summary: Artificial intelligence (AI) is intelligence demonstrated by 
# machines. AI research has been defined as the field of study of intelligent 
# agents. AI applications include advanced web search engines, recommendation 
# systems, self-driving cars and more.
"""


# ============================================================================
# 4. IMAGE CLASSIFICATION - Image Classification
# ============================================================================

"""
Example usage:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

# Analyzing a local image file
results = ai.classify_image("path/to/cat.jpg")
print("Top 3 results:")
for i, result in enumerate(results[:3], 1):
    print(f"{i}. {result['label']}: {result['score']:.2%}")

# Expected output (for a cat image):
# Top 3 results:
# 1. tabby cat: 45.32%
# 2. Egyptian cat: 32.18%
# 3. tiger cat: 12.45%

# Analyzing an image from URL
image_url = "https://example.com/dog.jpg"
results = ai.classify_image(image_url)
print("Top 5 results:")
for i, result in enumerate(results[:5], 1):
    print(f"{i}. {result['label']}: {result['score']:.2%}")

# Expected output (for a dog image):
# Top 5 results:
# 1. golden retriever: 67.89%
# 2. Labrador retriever: 18.23%
# 3. cocker spaniel: 5.67%
# 4. Irish setter: 3.45%
# 5. dog: 2.34%
"""


# ============================================================================
# 5. IMAGE CAPTIONING - Generate Image Descriptions (BLIP)
# ============================================================================

"""
Example usage:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

# Generate caption for a local image
caption = ai.caption_image("path/to/forest.jpg")
print(f"Caption: {caption}")

# Expected output:
# Caption: a beautiful forest with sunlight filtering through the trees

# Generate caption from URL
image_url = "https://example.com/playground.jpg"
caption = ai.caption_image(image_url)
print(f"Caption: {caption}")

# Expected output:
# Caption: children playing on a colorful playground
"""


# ============================================================================
# 6. IMAGE TO STORY - Generate Children's Stories from Images
# ============================================================================

"""
Example usage:

from ai_app import HuggingFaceAI

ai = HuggingFaceAI()

# Generate a story from an image
result = ai.image_to_story("path/to/kids_forest.jpg")
print(f"Caption: {result['caption']}")
print(f"Story: {result['story']}")

# Expected output:
# Caption: a happy girl walking in a forest with a friendly dog
# Story: Once upon a time, there was a happy girl named Emma who loved 
# exploring the forest near her home. One sunny morning, she took her 
# best friend, a fluffy golden dog named Max, on an adventure. They 
# walked through tall trees, listening to birds singing sweet songs.
# Emma found beautiful flowers and shared them with Max. Together they 
# discovered a sparkling stream where fish swam playfully. As the sun 
# began to set, they headed home, tired but happy from their wonderful day.

# You can also provide a URL
result = ai.image_to_story("https://example.com/animal.jpg", max_story_length=250)
print(f"Caption: {result['caption']}")
print(f"Story: {result['story']}")
"""


# ============================================================================
# 7. INTERACTIVE USAGE - From Command Line
# ============================================================================

"""
The application can run in two modes:

1. DEMO MODE (default):
   python ai_app.py
   
   This automatically runs through all demo features and shows
   the results.

2. INTERACTIVE MODE:
   python ai_app.py --interactive
   
   This starts an interactive menu where you can manually select
   which feature you want to use and enter your own data.
   
   Menu options:
   1. Sentiment Analysis - Analyze your own text sentiment
   2. Question Answering - Answer questions based on context
   3. Text Summarization - Summarize long text
   4. Image Classification - Object recognition in images
   5. Image Captioning (BLIP) - Generate image descriptions
   6. Image to Story - Generate children's stories from images
   0. Exit
"""


# ============================================================================
# 8. USING FROM PYTHON CODE
# ============================================================================

"""
Complete example program:

#!/usr/bin/env python3
from ai_app import HuggingFaceAI

def main():
    # Create AI object
    ai = HuggingFaceAI()
    
    # 1. Analyzing customer reviews
    reviews = [
        "This product is amazing! Best purchase ever!",
        "Terrible quality, broke after one day.",
        "It's okay, nothing special."
    ]
    
    print("Customer review analysis:")
    for review in reviews:
        result = ai.analyze_sentiment(review)
        print(f"  '{review[:30]}...' -> {result['label']}")
    
    # 2. FAQ system
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
    
    print("\nFAQ answers:")
    for q in questions:
        answer = ai.answer_question(faq_context, q)
        print(f"  Q: {q}")
        print(f"  A: {answer['answer']}")
    
    # 3. Product description summarization
    product_desc = '''
    [Long product description text...]
    '''
    summary = ai.summarize_text(product_desc)
    print(f"\nProduct summary: {summary}")
    
    # 4. Automatic product image tagging
    images = ["product1.jpg", "product2.jpg", "product3.jpg"]
    print("\nProduct image analysis:")
    for img in images:
        try:
            results = ai.classify_image(img)
            print(f"  {img}: {results[0]['label']}")
        except Exception as e:
            print(f"  {img}: Error - {e}")
    
    # 5. Generate children's story from image
    print("\nChildren's story generation:")
    try:
        result = ai.image_to_story("kids_playing.jpg")
        print(f"  Caption: {result['caption']}")
        print(f"  Story: {result['story'][:200]}...")
    except Exception as e:
        print(f"  Error: {e}")

if __name__ == "__main__":
    main()
"""


# ============================================================================
# 9. USEFUL TIPS AND NOTES
# ============================================================================

"""
MODEL DOWNLOADS:
- On the first run, models are automatically downloaded from Hugging Face
- Models are saved to ~/.cache/huggingface/ directory
- Larger models may take several minutes to download
- Internet connection is required for the first run

PERFORMANCE:
- GPU usage significantly speeds up processing
- Works on CPU too, but slower
- The pipeline() automatically detects and uses GPU if available

CUSTOMIZATION:
- Different models can be used with the pipeline() function
- Example: pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
- There are models for many languages available on Hugging Face

TROUBLESHOOTING:
- If models don't download, check your internet connection
- For OutOfMemory errors, use smaller models
- For CUDA errors, check PyTorch and CUDA compatibility

ADDITIONAL FEATURES:
- Translation: pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
- Named Entity Recognition: pipeline("ner")
- Text Generation: pipeline("text-generation")
- Zero-shot Classification: pipeline("zero-shot-classification")

IMAGE TO STORY FEATURE:
- Uses BLIP (Salesforce/blip-image-captioning-base) for image captioning
- Uses GPT-2 for story generation
- Generates kid-friendly 6-8 sentence stories
- Works with both local files and URLs
"""
