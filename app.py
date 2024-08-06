from flask import Flask, request, render_template
from dotenv import load_dotenv
import requests
import os

load_dotenv()

KEY = os.getenv("Key")

app = Flask(__name__,template_folder="templates")

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/")
def weather_info():
    city = request.form.get("city")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        wind = data["wind"]
        wind_speed = wind["speed"]
        weather = data["weather"]
        description = weather[0]["description"]
        return render_template("weather.html",city = city,temperature=temperature,feels_like=feels_like,wind_speed=wind_speed,description=description)
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    app.run(debug=True)