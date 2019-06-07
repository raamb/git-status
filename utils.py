import json
import requests
from constant import SLACK_HOOK


def report_slack(slack_msg):
    url = SLACK_HOOK['url']
    print(url)
    payload = {"channel": SLACK_HOOK['channel'],
               "username": "webhookbot",
               "text": slack_msg,
               "icon_emoji": ":ghost:"
               }

    resp = requests.post(url=url, data=json.dumps(payload))
    print(resp.status_code, resp.text)