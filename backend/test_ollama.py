from ollama_client import ask_llm

response = ask_llm(
    "What industry is OpenAI in?"
)

print(response)