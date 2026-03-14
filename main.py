from transformers import pipeline
from scipy.io.wavfile import write

# Salesforce/blip-image-captioning-base hasznalata a kep szovegge alakitashoz
def imgToText(path):
    
    img_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    
    text = img_to_text(path)[0]['generated_text']

    print("")
    print(text)
    print("")

    return text

scenario = imgToText("assets/test.png")

# Nyelvi modell hasznalata a tortenet generalasahoz
def generateStory(scenario):
    template = f"Once upon a time, there was {scenario}. "
    
    story_generator = pipeline("text-generation", model="roneneldan/TinyStories-33M")
    
    story = story_generator(template, max_length=200, num_return_sequences=1)[0]['generated_text']

    print("")
    print(story)
    print("")

    return story

# Fordito modell hasznalata a tortenet magyarra forditasahoz
def translateStory(story):
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hu")
    
    translated_story = translator(story)[0]['translation_text']

    print("")
    print(translated_story)
    print("")

    return translated_story

# TTS modell hasznalata a tortenet fajlba mentesehez
def textToSpeech(story):
    tts = pipeline("text-to-speech", model="facebook/mms-tts-hun")
    
    audio = tts(story)
    
    write("assets/story.wav", audio["sampling_rate"], audio["audio"].T)

    print("Audio file 'story.wav' has been created.")

    return audio

story = generateStory(scenario)
translatedStory = translateStory(story)
textToSpeech(translatedStory) # Magyar tortenet lementese fajlba.