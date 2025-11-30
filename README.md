# Történet generátor

Ez a projekt egy mesterséges intelligencia alapú alkalmazás, amely képekből generál rövid történeteket gyerekeknek, lefordítja őket magyarra, és fel is olvassa az angol verziót.

## Funkciók és Működés

A program egy AI pipeline-t használ, amely a következő lépésekből áll:

1.  **Képfelismerés (Image-to-Text):**
    -   A program elemzi a megadott képet.
    -   **Modell:** `Salesforce/blip-image-captioning-base`
    -   Kimenet: Egy rövid angol leírás a képről (pl. "a river with a mountain in the background").

2.  **Történetgenerálás (Story Generation):**
    -   A képleírás alapján generál egy rövid, gyerekeknek szóló mesét angolul.
    -   **Modell:** `roneneldan/TinyStories-33M`
    -   Ez a modell kifejezetten egyszerű, gyerekek számára érthető nyelvezetre van tanítva.

3.  **Fordítás (Translation):**
    -   A generált angol történetet lefordítja magyar nyelvre.
    -   **Modell:** `Helsinki-NLP/opus-mt-en-hu`

4.  **Szövegfelolvasás (Text-to-Speech):**
    -   Az eredeti angol történetet hangfájllá alakítja.
    -   **Modell:** `facebook/mms-tts-eng`
    -   Kimenet: Egy `story.wav` hangfájl.

## Előfeltételek

-   **Python 3.x** telepítve legyen a gépeden.
-   Ajánlott fejlesztőkörnyezet: **Visual Studio Code**.

## Telepítés

1.  **Klónozd le a repót** vagy töltsd le a fájlokat.
2.  Nyisd meg a projekt mappáját VS Code-ban.
3.  Nyiss egy terminált (Terminal -> New Terminal).
4.  Telepítsd a szükséges Python csomagokat az alábbi paranccsal:

    ```bash
    pip install -r requirements.txt
    ```

    *Ez telepíti a `transformers`, `torch`, `pillow`, `scipy`, `sentencepiece` és `sacremoses` csomagokat.*

## Használat

1.  Győződj meg róla, hogy van internetkapcsolatod (a modellek letöltéséhez).
2.  Futtasd a fő programot:

    ```bash
    python main.py
    ```

3.  A program:
    -   Kiírja a konzolra a kép leírását.
    -   Kiírja a generált angol mesét.
    -   Kiírja a magyar fordítást.
    -   Létrehoz egy `story.wav` fájlt a mappában az angol mese hanganyagával.

## Fájlok szerkezete

-   `main.py`: A fő programkód.
-   `requirements.txt`: A szükséges Python csomagok listája.
