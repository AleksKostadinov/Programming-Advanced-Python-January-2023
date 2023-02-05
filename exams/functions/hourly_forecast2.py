def forecast(*args):
    result = ''
    weather_dict = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': [],
    }
    for location, weather in sorted(args):
        weather_dict[weather].append(location)

    for key in weather_dict:
        for value in weather_dict[key]:
            result += f"{value} - {key}\n"
    return result

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
