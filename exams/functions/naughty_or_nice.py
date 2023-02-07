def naughty_or_nice_list(kids_list, *args, **kwargs):
    kids = {
        "Nice": [],
        "Naughty": [],
        "Not found": [],
    }
    kids_by_id = {}
    for kid_id, name in kids_list:
        if kid_id not in kids_by_id:
            kids_by_id[kid_id] = []
        kids_by_id[kid_id].append(name)
    for command in args:
        counting_number, nice_naughty = [int(x) if x.isdigit() else x for x in command.split('-')]
        if counting_number in kids_by_id:
            if nice_naughty == 'Naughty' and len(kids_by_id[counting_number]) == 1:
                kids["Naughty"].extend(kids_by_id[counting_number])
                del kids_by_id[counting_number]
            elif nice_naughty == 'Nice' and len(kids_by_id[counting_number]) == 1:
                kids["Nice"].extend(kids_by_id[counting_number])
                del kids_by_id[counting_number]
    for name, good_or_not in kwargs.items():
        count = 0
        for number, values in kids_by_id.items():
            if name in values:
                count += 1
        if count == 1:
            kids[good_or_not].append(name)
            for number, values in kids_by_id.items():
                if name in values:
                    values.remove(name)
    for value in kids_by_id.values():
        if value:
            kids["Not found"].extend(value)
    result = []
    for key, value in kids.items():
        if value:
            result.append(f"{key}: " + ', '.join(map(str,value)))
    return "\n".join(result)
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))


