

#Used to scan down the file "rankings_response.html" for uique links to players profile
#Got 50 links to 50 Unique players hence links to top 50 midfielders and saved in "world_cup_50_players.csv"
#I verified whether the links where of correct players



from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin

html = Path("rankings_response.html").read_text(
    encoding="utf-8",
    errors="replace"
)

soup = BeautifulSoup(html, "html.parser")

players = {}

for link in soup.select('a[href*="/rankings/player/"]'):
    href = link.get("href", "")

    # Find the player's name from the link or its surrounding HTML
    name = link.get_text(" ", strip=True)

    if not name:
        image = link.find("img")
        if image:
            name = image.get("alt", "").strip()

    if not name:
        parent = link.parent
        for _ in range(4):
            if parent is None:
                break

            image = parent.find("img")
            if image and image.get("alt", "").strip():
                name = image["alt"].strip()
                break

            parent = parent.parent

    if name and href:
        full_url = urljoin("https://fc.gradientsports.com", href)
        players[full_url] = name

print("Unique player URLs:", len(players))

for url, name in list(players.items())[:20]:
    print(f"{name} -> {url}")

import pandas as pd

df = pd.DataFrame(
    [
        {"Player": name, "URL": url}
        for url, name in players.items()
    ]
)

df.to_csv("world_cup_50_players.csv", index=False)

print("\nSaved 50 players to world_cup_50_players.csv")
print(df.head())

