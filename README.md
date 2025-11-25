# ml-practice-research

Practice project for an ML-based university project.

## 🤖 Hugging Face AI Application

This is a multimodal AI application that uses models from [Hugging Face](https://huggingface.co/models).

### ✨ Features

The application supports six main AI capabilities:

1. **Sentiment Analysis** - Analyze the emotional tone of text
2. **Question Answering** - Answer questions based on text context
3. **Text Summarization** - Automatically summarize long texts
4. **Image Classification** - Recognize objects in images
5. **Image Captioning (BLIP)** - Generate kid-friendly descriptions of images
6. **Story Generation** - Create short children's stories from images

### 🎯 Image to Story Generator (New Feature!)

This application includes a special feature for children: it can take any image and generate a cute children's story based on it!

**How it works:**
1. Upload or provide an image URL (e.g., forest, animal, playground, fairy tale illustration)
2. **Model 1 - Image Captioning**: Uses BLIP model to create a detailed, kid-friendly description
3. **Model 2 - Story Generation**: Uses GPT-2 to generate a short (6-8 sentences) children's story based on the description

### 📋 Installation

#### Requirements
- Python 3.8 or newer
- pip package manager

#### Steps

1. **Clone the repository**
```bash
git clone https://github.com/zsoltfrks/ml-practice-research.git
cd ml-practice-research
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### 🚀 Usage

#### Demo Mode

Demo mode automatically showcases all AI features:

```bash
python ai_app.py
```

#### Interactive Mode

Interactive mode allows you to try your own texts and images:

```bash
python ai_app.py --interactive
```

### 📚 Examples

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
long_text = "..." # long text
summary = ai.summarize_text(long_text)
print(summary)
```

#### Image Classification
```python
ai = HuggingFaceAI()
results = ai.classify_image("path/to/image.jpg")
# or URL:
results = ai.classify_image("https://example.com/image.jpg")
print(results)
```

#### Image Captioning (BLIP)
```python
ai = HuggingFaceAI()
caption = ai.caption_image("path/to/image.jpg")
print(caption)
# Example output: "a happy girl walking in a forest with a friendly dog"
```

#### Image to Story (for children)
```python
ai = HuggingFaceAI()
result = ai.image_to_story("path/to/image.jpg")
print(f"Caption: {result['caption']}")
print(f"Story: {result['story']}")
# Example output:
# Caption: "a happy girl walking in a forest with a friendly dog"
# Story: "Once upon a time, a happy girl named Emma went for a walk..."
```

### 🔧 Models Used

The application uses the following Hugging Face models:

- **Sentiment Analysis**: distilbert-base-uncased-finetuned-sst-2-english
- **Question Answering**: distilbert-base-cased-distilled-squad
- **Summarization**: facebook/bart-large-cnn
- **Image Classification**: google/vit-base-patch16-224
- **Image Captioning**: Salesforce/blip-image-captioning-base
- **Story Generation**: gpt2

### 📖 Additional Resources

- [Hugging Face Models](https://huggingface.co/models)
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [Pipeline API](https://huggingface.co/docs/transformers/main_classes/pipelines)

### 🤝 Contributing

This is a university practice project. Suggestions and improvements are welcome!

### 📝 License

MIT License
