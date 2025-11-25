from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GPT_MODEL = "gpt-5-mini"
client = OpenAI(api_key=OPENAI_API_KEY)

result = client.responses.create(
    model="gpt-5.1",
    input="What is the english translation for the spanish word 'peluche'?",
)

def get_data(word):
    prompt = f"""
    You are an assistant that returns information in clean, valid JSON only.

    TASK:
    Given the Spanish word "{word}", provide:

    - "translations": A list of English translation(s)
    - "part_of_speech": The grammatical part of speech
    - "example_sentence_spanish": One natural Spanish sentence using the word
    - "example_sentence_english": That same sentence translated to English
    - "important_info": A SHORT list (3 to 5 items) of the most useful notes about the word:
    * nuances / register
    * common collocations or patterns
    * one key pitfall or contrast with a similar word
    Each item must be at most 25 words.

    RESPONSE FORMAT (STRICT):
    Return ONLY a JSON object in this exact structure:

    {{
    "translations": [],
      "part_of_speech": "",
      "example_sentence_spanish": "",
      "example_sentence_english": "",
      "important_info": []
    }}

    Do not include anything outside of the JSON. No markdown.
    """
    result = client.responses.create(
        model=GPT_MODEL,
        input=prompt,
    )

    return json.loads(result.output_text)
