from gpt import get_data
from anki_utils import create_note
import random

UNSEEN_WORDS_PATH = "data/unseen_words.txt"
SEEN_WORDS_PATH = "data/seen_words.txt"


def get_random_word(path):
    with open(path, "r") as f:
        words = [line.strip() for line in f if line.strip()]

    if not words:
        return None

    word = random.choice(words)
    words.remove(word)

    with open(path, "w") as f:
        for w in words:
            f.write(w + "\n")

    with open(SEEN_WORDS_PATH, "a") as f:
        f.write(word + "\n")

    return word


def generate_card(word):
    word_data = get_data(word)
    front = word
    back = ", ".join(word_data['translations'])
    sentence = word_data['example_sentence_spanish']
    english_sentence = word_data['example_sentence_english']
    pos = word_data['part_of_speech']
    important_info = word_data['important_info']
    important_info_html = "<ul>" + "".join(
        f"<li>{p}</li>" for p in important_info
    ) + "</ul>"

    create_note(front, back, sentence, english_sentence, pos, important_info_html)

def main(n=1):
    for i in range(n):
        word = get_random_word(UNSEEN_WORDS_PATH)
        generate_card(word)

if __name__ == "__main__":
    n = int(input("How many words would you like to do?: "))
    main(n)

