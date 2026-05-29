from ollama_client import ask_llm
import json


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

    try:
        return json.loads(response)
    except:
        return {
            "industry": "Unknown",
            "niche": "Unknown",
            "sub_niche": "Unknown"
        }