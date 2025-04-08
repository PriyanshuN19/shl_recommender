import requests

response = requests.post(
    "https://shl-recommender-pefm.onrender.com/recommend",
    json={"query": "problem solving"}
)

print(response.json())
