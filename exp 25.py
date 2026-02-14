from transformers import pipeline

# Load GPT-2 text generation model
generator = pipeline("text-generation", model="gpt2")

prompt = "Explain Natural Language Processing in simple terms."

result = generator(prompt, max_length=100, num_return_sequences=1)

print("Generated Text:\n")
print(result[0]['generated_text'])
