from datetime import datetime, timezone
from smtplib import SMTP
from requests import get

MY_LATITUDE = 42.43
MY_LONGITUDE = -87.9

EMAIL = "ntouchtongarbage@yahoo.com"

# This section is to check if the ISS is overhead

response = get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def between_two_numbers(num, low, high):
    """Function to determaine if num is in between a and b."""
    if low < num and num < high:
        return True
    else:
        return False

LONG_CHECK = between_two_numbers(iss_longitude, MY_LONGITUDE - 5, MY_LONGITUDE + 5)
LAT_CHECK = between_two_numbers(iss_latitude, MY_LATITUDE - 5, MY_LATITUDE + 5)

if LONG_CHECK is True and LAT_CHECK is True:
    IS_OVERHEAD = True
else:
    IS_OVERHEAD = False

# This section is for the time of day check

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

response = get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc)
# print(IS_OVERHEAD)

#If the ISS is close to my current position
# and it is currently dark

if IS_OVERHEAD:
    if time_now.hour < sunrise or time_now.hour > sunset:
        with SMTP("smtp.mail.yahoo.com", port=587) as connection:
            connection.starttls()
            connection.login(
                user=EMAIL,
                password="insert password here",
            )
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="ntouchton@protonmail.com",
                msg="Subject:Look up.\n\nLook up.",
            )

# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
