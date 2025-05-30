# my_agent/agent.py

from finops_prompts.prompt_loader import load_prompt

query = "Give me EC2 cost trend for last month"
prompt_template = load_prompt("cot_structuring")
prompt = prompt_template["prompt"]
formatted_prompt = "\n".join(prompt).format(query=query)
print(formatted_prompt)
