#!/usr/bin/env python3
# language_loader.py

import json

def load_language(language):
    with open(f'languages/{language}.json', 'r') as file:
        return json.load(file)
