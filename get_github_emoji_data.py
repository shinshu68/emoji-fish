import urllib.request
import json


def emoji_to_hex(emoji):
    hex_data = ''
    for char in emoji:
        hex_data += hex(ord(char)).replace('0x', '\\U')
    return hex_data


GITHUB_EMOJI_URL = 'https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json'
emoji_list = []
with urllib.request.urlopen(GITHUB_EMOJI_URL) as req:
    emoji_json = json.loads(req.read().decode('utf-8'))
    for emoji in emoji_json:
        hex_data = emoji_to_hex(emoji['emoji'])
        for alias in emoji['aliases']:
            emoji_list.append(f'":{alias}:"={hex_data}')

emoji_list.sort()
for emoji in emoji_list:
    print(emoji)
