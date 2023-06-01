import requests

url = "https://api.greynoise.io/v3/community/142.251.33.110"

headers = {
    "accept": "application/json",
    "key": "Ol4GL8sBpIHmU4Ha2e6RAdZFON0fqEmrLKR5H4QoY7J6tZwgPM2g61eOzyHSX66O"
}

response = requests.get(url, headers=headers)

print(response.text)