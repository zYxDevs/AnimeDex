
import random
import requests
from string import digits


def get_names(li):
    x = ''.join(f'{i}, ' for i in li)
    return x[:-2]


def get_title(tit):
    if tit.endswith('-dub'):
        tit = tit[:-4]
    if tit.endswith('-sub'):
        tit = tit[:-4]
    x = tit.replace('-', ' ').title().strip()

    if x[-1] not in digits:
        x += ' 1'

    return x


z1 = ['goload', 'ssbstream', 'dood', 'fembed', 'mixdrop']
z2 = ['gogo', 'goload', 'ssbstream', 'dood', 'fembed', 'mixdrop']


def sort_list(list1, list2):
    x1 = ['1', '2', '3', '4', '5']
    x2 = ['1', '2', '3', '4', '5']

    for i in z1:
        for m in list1:
            if i in m:
                n = z1.index(i)
                x2[n] = m

    for a in x2:
        for b in x1:
            if b == a:
                n = x2.index(b)
                x2[n] = '#watch'

    y1 = ['1', '2', '3', '4', '5', '6']
    y2 = ['1', '2', '3', '4', '5', '6']

    for i in z2:
        for m in list2:
            if i in m:
                n = z2.index(i)
                y2[n] = m

    for a in y2:
        for b in y1:
            if b == a:
                n = y2.index(b)
                y2[n] = '#download'

    return x2, y2


def get_targets(list):
    final = []

    for i in list:
        if '#' in i:
            final.append('')
        else:
            final.append('target="_blank"')
    return final


def get_atitle(title):
    return (
        title.get('english') or title.get('romaji') or title.get('native')
        if title
        else 'Unknown'
    )


def get_other_title(title):
    if not title:
        return 'Unknown'
    other = ''
    tit = title.get('english')
    if tit:
        other += f'{tit}, '
    tit = title.get('romaji')
    if tit:
        other += f'{tit}, '
    tit = title.get('native')
    if tit:
        other += f'{tit}, '
    return tit[:-2]


def get_studios(stud):
    tit = ''.join(i.get('name') + ', ' for i in stud)
    return tit[:-2]


def get_genre(genres):
    return '' if not genres or len(genres) == 0 else random.choice(genres)


def get_urls(title):
    return f'/anime/{str(requests.utils.quote(title))}'


def get_t_from_u(url):
    return str(requests.utils.unquote(url)).replace('/anime/', '')
