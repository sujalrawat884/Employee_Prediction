import requests

url = "http://127.0.0.1:5000/predict"
test_data = {
    "team": 5, "month": 3, "targeted_productivity": 0.80, "smv": 10.5,
    "wip": 20, "over_time": 1000, "incentive": 500, "idle_time": 5,
    "idle_men": 2, "no_of_style_change": 1, "no_of_workers": 50
}

response = requests.post(url, data=test_data)
print(response.text)
