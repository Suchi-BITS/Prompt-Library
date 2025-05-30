from finops_prompts.prompt_loader import load_prompt

def test_load_prompt():
    prompt = load_prompt("intent_classification")
    assert "prompt" in prompt
    assert isinstance(prompt["prompt"], list)
