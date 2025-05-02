from SimplerLLM.language.llm import LLM, LLMProvider

llm_instance = LLM.create(provider=LLMProvider.GEMINI, model_name="gemini-1.5-flash")

generated_text = llm_instance.generate_response(prompt="generate a sentence of 5 words")

print(generated_text)
