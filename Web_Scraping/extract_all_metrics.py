
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd

# Folder containing the downloaded HTML files
folder = Path("player_html")

# Store the metrics for every player
all_players = []

# Read each HTML file
for file in folder.glob("*.html"):
    html = file.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    player_metrics = {"Player ID": file.stem}

    # Extract each metric's name and displayed value
    for item in soup.select("li"):
        label = item.select_one("div.truncate")
        value = item.select_one('[data-slot="badge"]')

        if label and value:
            name = label.get_text(" ", strip=True)
            number = value.get_text(" ", strip=True)

            player_metrics[name] = number

    all_players.append(player_metrics)

# Combine the players into one table
df = pd.DataFrame(all_players)

# Save the extracted data separately
df.to_csv("all_players_metrics.csv", index=False)

print("Players extracted:", len(df))
print("Columns created:", len(df.columns))
print("\nFirst five rows:")
print(df.head().to_string(index=False))

print("\nSaved to all_players_metrics.csv")
