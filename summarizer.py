from transformers import pipeline

summarizer = pipeline("text-generation", model="gpt2")

text = """The Namibian government has announced a new digital transformation strategy 
aimed at modernising public services. The plan includes investment in broadband 
infrastructure, e-government platforms, and digital literacy programmes."""

prompt = f"Summarize this news article in one sentence:\n{text}\nSummary:"

result = summarizer(prompt, max_new_tokens=60, do_sample=False)
print("Summary:", result[0]['generated_text'])