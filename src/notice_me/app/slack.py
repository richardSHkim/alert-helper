import os
import requests


def call_slack(text: str):
    url = os.environ.get("SLACK_ALARM_URL", None)
    requests.post(url, json={"text": text})
