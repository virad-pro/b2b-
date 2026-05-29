from ollama_client import ask_llm
import json

import re


def detect_niche(company):

    prompt = f"""
Analyze this company.

Company Name:
{company.get('name')}

Description:
{company.get('description')}

Specialities:
{company.get('specialities')}

Return ONLY valid JSON.

Example:

{{
    "industry": "...",
    "niche": "...",
    "sub_niche": "..."
}}
"""



    response = ask_llm(prompt)

    match = re.search(
    r"\{.*\}",
    response,
    re.DOTALL
)

    if match:

       return json.loads(
        match.group()
    )

    return {
    "industry": "Unknown",
    "niche": "Unknown",
    "sub_niche": "Unknown"
}