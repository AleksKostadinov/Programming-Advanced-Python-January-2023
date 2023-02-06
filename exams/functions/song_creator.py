def add_songs(*args):
    result_dict = {}
    result = []
    for title, lyrics in args:
        if title not in result_dict:
            result_dict[title] = []
        result_dict[title] += lyrics

    for key, value in result_dict.items():
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






