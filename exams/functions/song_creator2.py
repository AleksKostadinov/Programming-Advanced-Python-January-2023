def add_songs(*args):
    result_dict = {}
    result = ''
    for title, lyrics in args:
        if title not in result_dict:
            result_dict[title] = []
        result_dict[title].extend(lyrics)

    for key, value in result_dict.items():
        result += f"- {key}\n"
        for lyric in value:
            result += f"{lyric}\n"
    return result

print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
