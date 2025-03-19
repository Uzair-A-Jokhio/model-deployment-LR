import requests

url = "http://127.0.0.1:8080/predict"
data = {"input": [5.1, 3.5, 1.4, 0.2]}

response = requests.post(url, json=data)
print(response.json())