import requests

endpoint = f"http://127.0.0.1:5000/recommendations/OK Computer"
text = requests.get(endpoint)
print(text.text)