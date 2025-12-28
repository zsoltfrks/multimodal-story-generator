# Multimodal Story Generator


This project is an AI-based application that generates short stories for children from images, translates them into Hungarian, and reads aloud the English version since the Hungarian TTS is a bit rough.

## Features and How it Works

The program uses an AI pipeline consisting of the following steps:

1.  **Image Recognition (Image-to-Text):**
    -   The program analyzes the provided image.
    -   **Model:** `Salesforce/blip-image-captioning-base`
    -   Output: A short English description of the image (e.g., "a river with a mountain in the background").

2.  **Story Generation:**
    -   Generates a short story for children in English based on the image description.
    -   **Model:** `roneneldan/TinyStories-33M`
    -   This model is specifically trained on simple language understandable by children.

3.  **Translation:**
    -   Translates the generated English story into Hungarian.
    -   **Model:** `Helsinki-NLP/opus-mt-en-hu`

4.  **Text-to-Speech:**
    -   Converts the original English story into an audio file.
    -   **Model:** `facebook/mms-tts-eng`
    -   Output: A `story.wav` audio file.

## Prerequisites

-   **Python 3.x** installed on your machine.
-   Recommended IDE: **Visual Studio Code**.

## Installation

1.  **Clone the repo** or download the files.
2.  Open the project folder in VS Code.
3.  Open a terminal (Terminal -> New Terminal).
4.  Install the required Python packages with the following command:

    ```bash
    pip install -r requirements.txt
    ```

    *This installs `transformers`, `torch`, `pillow`, `scipy`, `sentencepiece`, and `sacremoses`.*

## Usage

1.  Ensure you have an internet connection (to download the models).
2.  Run the main program:

    ```bash
    python main.py
    ```

3.  The program will:
    -   Print the image description to the console.
    -   Print the generated English story.
    -   Print the Hungarian translation.
    -   Create a `story.wav` file in the folder with the audio of the English story.

## File Structure

-   `main.py`: The main program code.
-   `requirements.txt`: List of required Python packages.
