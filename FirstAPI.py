import requests
import pandas as pd

# 5 sample cities in Virginia with lat/lon
cities_va = {
    "Williamsburg": (37.2707, -76.7075),
    "Richmond": (37.5407, -77.4360),
    "Virginia Beach": (36.8529, -75.9780),
    "Roanoke": (37.27097, -79.94143),
    "Charlottesville": (38.0293, -78.4767)
}

url = "https://api.open-meteo.com/v1/forecast"

results = []

for city, (lat, lon) in cities_va.items():
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if "current_weather" in data:
        weather = data["current_weather"]
        results.append({
            "City": city,
            "Temperature (°C)": weather["temperature"],
            "Wind Speed (m/s)": weather["windspeed"],
            "Time": weather["time"]
        })
    else:
        results.append({"City": city, "Temperature (°C)": None, 
                        "Wind Speed (m/s)": None, "Time": None})

# Display as table
df = pd.DataFrame(results)
print(df)
