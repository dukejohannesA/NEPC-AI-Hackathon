import pandas as pd

data = {
    "headline": [
        "President signs new education bill",
        "Local football team wins championship",
        "New restaurant opens in Windhoek",
        "Tech startup raises N$2 million",
        "Heavy rains cause flooding in northern Namibia",
        "Parliament debates new land reform policy",
        "Namibia national team qualifies for AFCON",
        "New shopping mall opens in Katutura",
        "Mining company announces 500 new jobs",
        "Drought declared in Kunene region",
        "Government launches free wifi in schools",
        "Windhoek FC signs new striker",
        "Local chef wins African cooking award",
        "Namibia stock exchange hits record high",
        "Flash floods destroy homes in Oshakati"
    ],
    "category": [
        "politics", "sports", "lifestyle", "business", "weather",
        "politics", "sports", "lifestyle", "business", "weather",
        "politics", "sports", "lifestyle", "business", "weather"
    ],
    "online_views": [
        4200, 8900, 3100, 5600, 7800,
        3900, 9200, 2800, 4700, 6500,
        5100, 7600, 2300, 4100, 8200
    ]
}

df = pd.DataFrame(data)
df.to_csv("news_data.csv", index=False)
print("Dataset saved to news_data.csv")
print(df)