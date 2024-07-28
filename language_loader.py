import json

def load_language(language):
    try:
        with open(f'languages/{language}.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Language file for '{language}' not found. Defaulting to English.")
        with open('languages/english.json', 'r') as file:
            return json.load(file)
