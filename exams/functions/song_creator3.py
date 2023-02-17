def add_songs(*args):
    song_dict = {}
    result = []
    for song, lyrics in args:
        if not song in song_dict:
            song_dict[song] = []
        song_dict[song].extend(lyrics)
    for key, value in song_dict.items():
        result.append(f"- {key}")
        result.extend(value)
    return '\n'.join(result)

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))


