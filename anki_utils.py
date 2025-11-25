import json
import requests

ANKI_CONNECT_URL = "http://localhost:8765"

def invoke(action, params=None):
    payload = {
        "action": action,
        "version": 6,
        "params": params or {}
    }
    resp = requests.post(ANKI_CONNECT_URL, json=payload)
    print("Status code:", resp.status_code)
    print("Raw response:", resp.text)
    return resp.json()

def create_note(front, back, sentence, sentence_english, pos, important_info):
    deck = "Languages::Spanish"
    note = {
        "deckName": deck,
        "modelName": "Basic",
        "fields": {
            "Front": front,
            "Back": back,
            "Sentence": sentence,
            "Part of Speech": pos,
            "Sentence English": sentence_english,
            "Important Info": important_info
        },
        "options": {
            "allowDuplicate": False
        },
        "tags": []
    }

    return invoke("addNote", {"note": note})
