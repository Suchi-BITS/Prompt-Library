import json
import os

PROMPT_DIR = os.path.join(os.path.dirname(__file__), 'prompts')

def load_prompt(name: str) -> dict:
    """Load a prompt JSON by name."""
    path = os.path.join(PROMPT_DIR, f"{name}.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt '{name}' not found.")
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
