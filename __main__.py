import os
from datetime import datetime

import requests

SATURDAY = 5


def post_attend():
    today = datetime.today()
    if today.weekday() != SATURDAY:
        print('Not saturday')
        return

    host = 'sm-members.fcfc-1.com'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; SM-N950N Build/PPR1.180610.011)',
        'Host': host,
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }
    data = {
        'ver': 338,
        'os': 'a1',
        'pw': os.getenv('pw'),
        'n': '최종원',
        'gid': os.getenv('gid'),
        'it': '0600000',
        'bid': os.getenv('bid'),
        'bt': 'Y',
        'edid': int(today.strftime('%Y%m%d')),
        'etid': 1500,
        'g_t': 517902720,
    }
    resp = requests.post(
        f'http://{host}/group_members/set_offmoim/{os.getenv("bid")}.json',
        headers=headers,
        json=data
    )
    print(resp.content)
    return resp


if __name__ == '__main__':
    post_attend()
