import json
import sys


def suggest(token):
    emoji_data = []
    with open('emoji.json') as f:
        emoji_data = json.load(f)

    match_data = [emoji for emoji in emoji_data for alias in emoji['aliases'] if token in alias]

    data = [tuple(d.items()) for d in match_data]
    data = set([(i[0], i[1], (i[2][0], tuple(i[2][1])), i[3]) for i in data])
    match_data = [dict(t) for t in data]
    for data in match_data:
        emoji = data['emoji']
        for alias in data['aliases']:
            print(f'{emoji} :{alias}:')


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        suggest(args[1])
    else:
        exit()
