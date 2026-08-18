import requests 
import pandas as pd
import os 
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("api_key")
cities = ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]

url = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_list):
    all_weather_data = []

    for city in city_list:
        params = {
            'q' : city,
            'appid' : api_key,
            'units' : 'metric'
        }

        try:
            response = requests.get(url, params=params)

            if response.status_code != 200:
                print(f"Error fetching data for {city}:")
                continue

            data = response.json()
            all_weather_data.append(data)
            print(f"Successfully fetched data for {city}")

        except Exception as e:
            print(f"An error occurred while fetching data for {city}: {e}")

    return all_weather_data

data = weather_data(cities)
df = pd.DataFrame(data)

print(df)
timestamp = datetime.now().strftime("%d-%m-%Y")
filename = f"weather_report_{timestamp}.csv"

df.to_csv(filename, index=False)
print(f"Weather report saved as {filename}")

