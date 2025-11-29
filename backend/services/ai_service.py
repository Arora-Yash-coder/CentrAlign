import json
from services.memory_service import retrieve_relevant_forms
from config.settings import settings
import requests

"""
This service is written to support flexible LLM providers.
Default: Gemini 1.5 Flash (via REST).
You can plug Groq / OpenRouter by changing `call_llm_api`.
"""


def call_llm_api(messages: list):
    """
    Raw REST call to Gemini-style chat completion.
    Expected output: JSON string representing the form schema.
    """
    url = "https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent".format(
        settings.AI_MODEL
    )

    payload = {
        "contents": [
            {"role": msg["role"], "parts": [{"text": msg["content"]}]}
            for msg in messages
        ]
    }

    params = {"key": settings.AI_API_KEY}

    res = requests.post(url, json=payload, params=params)

    if res.status_code != 200:
        raise Exception(f"AI API Error: {res.text}")

    output = res.json()
    text = output["candidates"][0]["content"]["parts"][0]["text"]

    return text


def generate_schema_with_context(prompt: str, context: list):
    """
    Builds the final LLM instruction based on:
    - relevant past forms
    - user's new prompt
    """

    system_prompt = """
    You are an intelligent form schema generator.
    You convert natural language instructions into JSON form schemas.
    Return ONLY valid JSON — no markdown, no explanation, no comments.
    """

    user_payload = f"""
    Here is relevant user form history for reference:
    {json.dumps(context, indent=2)}

    Now generate a new form schema for this request:
    "{prompt}"
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_payload}
    ]

    result = call_llm_api(messages)

    try:
        return json.loads(result)
    except:
        raise Exception("AI returned invalid JSON. Validate your prompt formatting.")


def generate_form_schema(prompt: str, user_id: str):
    """
    Main public function used by form_service.
    """
    relevant = retrieve_relevant_forms(prompt, user_id)
    schema = generate_schema_with_context(prompt, relevant)
    return schema
