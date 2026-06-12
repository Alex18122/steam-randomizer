import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

steam_id = "76561198867346433"

url = (f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={steam_id}&include_appinfo=1&format=json")

response = requests.get(url)
data = response.json()

games = data["response"]["games"]

for game in sorted(games, key=lambda g: g["name"]):
    print(f"{game["name"]} appId: {game["appid"]} playtime : {game["playtime_forever"]}")