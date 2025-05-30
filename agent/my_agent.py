# my_agent/agent.py

from finops_prompts import get_prompt

query = "Give me EC2 cost trend for last month"
prompt_template = get_prompt("cot_structuring")
prompt = prompt_template.format(query=query)

# Use this prompt in your LLM chain
print(prompt)
