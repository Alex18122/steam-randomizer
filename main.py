import requests

API_KEY = "E5A8D84A5EC9F9BC368FC36DC6365CAF"
steam_id = input("ingrese su ide de steam")

url = (f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={steam_id}&include_appinfo=1&format=json")