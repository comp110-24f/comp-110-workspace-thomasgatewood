"""Weather report question in class."""


def get_weather_report() -> str:
    weather: str = input("What is the weather")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("keep cool out there")
    else:
        print("I don't recgonize this weather")
    return weather
