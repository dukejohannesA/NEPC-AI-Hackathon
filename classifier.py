from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

headlines = [
    "President signs new education bill",
    "Local football team wins championship",
    "New restaurant opens in Windhoek",
    "Tech startup raises N$2 million",
    "Heavy rains cause flooding in northern Namibia"
]

categories = ["politics", "sports", "lifestyle", "business", "weather"]

print("Classifying headlines...\n")
for headline in headlines:
    result = classifier(headline, candidate_labels=categories)
    top_category = result["labels"][0]
    confidence = round(result["scores"][0] * 100, 1)
    print(f"Headline: {headline}")
    print(f"Category: {top_category} ({confidence}% confidence)\n")