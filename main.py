from dotenv import load_dotenv, find_dotenv
from transformers import pipeline

load_dotenv(find_dotenv())

# Salesforce/blip-image-captioning-base hasznalata a kep szovegge alakitashoz
def img2text(url):
    
    img_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    
    text = img_to_text(url)[0]['generated_text'] # Az elso talalat kinyerese, kivagjuk a szoveget (ne keruljon bele felesleges adat)

    print("")
    print(text)
    print("")
    return text

scenario = img2text("https://images.unsplash.com/photo-1506744038136-46273834b3fb")

# LLM hasznalata a tortenet generalasahoz
def generate_story(scenario):
    template = f"Once upon a time, there was {scenario}. "
    
    # Using a model specifically trained for children's stories
    story_generator = pipeline("text-generation", model="roneneldan/TinyStories-33M")
    
    story = story_generator(template, max_length=200, num_return_sequences=1)[0]['generated_text']

    print("")
    print(story)
    print("")
    return story

generate_story(scenario)