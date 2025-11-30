from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
from scipy.io.wavfile import write

load_dotenv(find_dotenv())

# Salesforce/blip-image-captioning-base hasznalata a kep szovegge alakitashoz
def imgToText(url):
    
    img_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    
    text = img_to_text(url)[0]['generated_text'] # Az elso talalat kinyerese, kivagjuk a szoveget (ne keruljon bele felesleges adat)

    print("")
    print(text)
    print("")

    return text

scenario = imgToText("assets/test.png")

# LLM hasznalata a tortenet generalasahoz
def generateStory(scenario):
    template = f"Once upon a time, there was {scenario}. "
    
    story_generator = pipeline("text-generation", model="roneneldan/TinyStories-33M")
    
    story = story_generator(template, max_length=200, num_return_sequences=1)[0]['generated_text']

    print("")
    print(story)
    print("")

    return story

# Fordito modell hasznalata (Angol -> Magyar)
def translateStory(story):
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hu")
    
    translated_story = translator(story)[0]['translation_text']

    print("")
    print(translated_story)
    print("")

    return translated_story

# TTS modell hasznalata a tortenet felolvasasahoz
def textToSpeech(story):
    tts = pipeline("text-to-speech", model="facebook/mms-tts-eng")
    
    audio = tts(story)
    
    write("assets/story.wav", audio["sampling_rate"], audio["audio"].T)

    print("Audio file 'story.wav' has been created.")

    return audio

story = generateStory(scenario)
translated_story = translateStory(story)
textToSpeech(story) # Angol tortenet felolvasasa, mert a TTS modell csak angolul tud normalisan.