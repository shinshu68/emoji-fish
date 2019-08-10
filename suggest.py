import json
import sys


def suggest(token):
    emoji_data = []
    with open('emoji.json') as f:
        emoji_data = json.load(f)

    match_data = [emoji for emoji in emoji_data for alias in emoji['aliases'] if token in alias]

    print(match_data)


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        suggest(args[1])
    else:
        exit()
