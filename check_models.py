from groq import Groq

client = Groq(api_key="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")

models = client.models.list()

print("Available Models:\n")

for m in models.data:
    print(m.id)