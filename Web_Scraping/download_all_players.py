
import pandas as pd
import requests
from pathlib import Path

# 1. Read the list of 50 players
players = pd.read_csv("world_cup_50_players.csv")

# 2. Create a folder to store the downloaded pages
output_folder = Path("player_html")
output_folder.mkdir(exist_ok=True)

# 3. Download each player's metrics page
for index, player in players.iterrows():
    name = player["Player"]
    profile_url = player["URL"]

    # Change the profile URL to the metrics URL
    metrics_url = profile_url.replace(
        "?competition=world-cup",
        "/metrics?competition=world-cup"
    )

    try:
        response = requests.get(metrics_url, timeout=20)
        response.raise_for_status()

        # Make a safe filename from the player ID
        player_id = metrics_url.split("/player/")[1].split("/")[0]
        file_path = output_folder / f"{player_id}.html"

        file_path.write_text(response.text, encoding="utf-8")

        print(f"SUCCESS: {name} | {response.status_code}")

    except requests.RequestException as error:
        print(f"FAILED: {name} | {error}")

print("Download process finished.")
