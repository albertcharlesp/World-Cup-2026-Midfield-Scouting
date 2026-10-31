
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd

folder = Path("player_html")
files = list(folder.glob("*.html"))

results = []

for file in files:
    html = file.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    metrics = [
        item
        for item in soup.select("li")
        if item.select_one("div.truncate")
        and item.select_one('[data-slot="badge"]')
    ]

    results.append({
        "Player ID": file.stem,
        "Metric Count": len(metrics)
    })

df = pd.DataFrame(results)

print("Files checked:", len(df))
print("\nMetric count summary:")
print(df["Metric Count"].value_counts().sort_index())

print("\nFiles that do not contain 55 metrics:")
print(df[df["Metric Count"] != 55].to_string(index=False))

df.to_csv("metric_count_check.csv", index=False)
print("\nSaved report: metric_count_check.csv")

