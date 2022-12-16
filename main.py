from requests import get

# response = get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# print(response)

# latitude = response.json()["iss_position"]["latitude"]
# longitude = response.json()["iss_position"]["longitude"]
# iss_position = (latitude, longitude)
# # print(response.json())

# print(iss_position)


parameters = {
    "lat": 42.43,
    "lng": -87.9
}

response = get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

print(response.json())
