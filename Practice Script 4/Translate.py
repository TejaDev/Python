def translate(x):
    List = []
    d = {"merry": "god",
         "christmas": "jul",
         "and": "och",
         "happy": "gott",
         "new": "nytt",
         "year": "ar"}
    y = x.split(' ')
    for i in y:
        List.append(d[i])

    return (' '.join(List))


print(translate('merry christmas and happy new year'))