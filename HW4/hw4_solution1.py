def percentage(text, abw='qwertyuiopasdfghjklzxcvbnm'):
    List1 = [f for f in this_text.lower() if f in abw]
    List = {}
    for f in List1:
        if f in List:
            List[f] += f
        else:
            List[f] = f
    for f in List:
        List[f] = round((len(List[f]) / len(List1) * 100), 1)
    return List


this_text = 'AsBCda'

print(percentage(this_text))
