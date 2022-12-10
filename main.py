from requests import get

response = get(url="http://api.open-notify.org/iss-now.json")
print(response)

if response.status_code == 404:
    raise Exception("This resource is not available.")
if response.status_code == 401:
    raise Exception("You are not authorized to access this data.")
