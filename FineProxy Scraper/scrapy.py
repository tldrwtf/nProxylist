import json

data_file = "load.txt"

try:
  with open(data_file, "r") as file:
    data = file.read()
except FileNotFoundError:
  print(f"Error: File '{data_file}' not found!")
  exit()

proxies = json.loads(data)

with open("scraped.txt", "a") as file:

  for proxy in proxies:
    ip = proxy["ip"]
    port = proxy["port"]
    file.write(f"{ip}:{port}\n")

print("Saved to scraped.txt. Join https://t.me/Finnessable")