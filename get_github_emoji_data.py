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
        emoji_data = {
                        'emoji': emoji['emoji'],
                        'unicode': hex_data,
                        'aliases': emoji['aliases'],
                        'tags': emoji['tags'],
                        'description': emoji['description']
                     }
        emoji_list.append(emoji_data)

with open('emoji.json', 'w') as f:
    json.dump(emoji_list, f, ensure_ascii=False, indent=4, separators=(',', ': '))

