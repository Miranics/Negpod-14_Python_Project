#!/usr/bin/python3
import json

def load_language(language):
    with open(f'languages/{language}.json', 'r') as file:
        lang = json.load(file)
    return lang
