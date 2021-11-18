pupils = [{
    'firstname': 'Masha',
    'Group': 42,
    'physics': 7,
    'informatics': 6,
    'history': 8,
}, {'firstname': 'Misha',
    'Group': 42,
    'physics': 6,
    'informatics': 7,
    'history': 9, },
    {'firstname': 'Vova',
     'Group': 42,
     'physics': 3,
     'informatics': 2,
     'history': 2, }]
c = 0
c1 = 0
for i in pupils:
    for j in i.values():
        if isinstance(j, int) and 0 < j <= 10:
            c += j
            c1 += 1

    if (c / c1) > 4:
        print(i['firstname'])
    c = 0
    c1 = 0
