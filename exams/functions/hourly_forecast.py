def forecast(*args):
    data = {}
    result = ''
    weather_rank = {
        'Sunny': 1,
        'Cloudy': 2,
        'Rainy': 3,
    }
    for city, weather in args:
        data[city] = {weather: weather_rank[weather]}

    for key, value in sorted(data.items(), key=lambda x: (list(x[1].values())[0], x[0])):
        result += f'{key} - {"".join(value)}\n'
    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

