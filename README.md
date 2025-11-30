# Történet generátor

Ez a projekt egy mesterséges intelligencia alapú alkalmazás, amely képekből generál rövid történeteket gyerekeknek. A program először szöveges leírást készít egy képről, majd ebből a leírásból egy mesét ír.

## Követelmények
- Python 3.x telepítve
- Visual Studio Code (ajánlott)

## Projekt megnyitása VS Code-ban

1.  Indítsd el a **Visual Studio Code**-ot.
2.  Kattints a bal felső sarokban a **File** (Fájl) menüre, majd válaszd az **Open Folder...** (Mappa megnyitása) lehetőséget.
3.  Keresd meg és válaszd ki a `multimodal-story-generator` mappát.

## Telepítés és Futtatás

1.  **Terminál megnyitása:**
    A VS Code-ban kattints a **Terminal** -> **New Terminal** menüpontra.

2.  **Csomagok telepítése:**
    Másold be és futtasd az alábbi parancsot a függőségek telepítéséhez:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Program indítása:**
    A futtatáshoz írd be:
    ```bash
    python main.py
    ```

## Működés
A `main.py` fájlban található kód:
1.  Letölt egy képet az internetről.
2.  A `Salesforce/blip-image-captioning-base` modell segítségével leírja, mi van a képen.
3.  A `roneneldan/TinyStories-33M` modell segítségével generál egy rövid mesét a leírás alapján.
