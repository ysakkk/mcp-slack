"""Slack イベントハンドラ"""

import logging
import os
import requests

from slack_bolt import App

logger = logging.getLogger(__name__)

N8N_WEBHOOK_URL = os.environ["N8N_WEBHOOK_URL"]

def register_handlers(app: App) -> None:
    """イベントハンドラを登録"""
    
    @app.event("app_mention")
    def handle_app_mention(event, say, client):
        """app_mention イベントを処理"""
        logger.info(f"app_mention を受信: {event}")
        payload = {
            "user": event["user"],
            "text": event["text"],
            "channel": event["channel"],
            "ts": event["ts"],
        }
       
        requests.post(N8N_WEBHOOK_URL, json=payload)
       
        say("受け取った。処理中。")
        logger.info(f"ACK を送信しました (channel: {channel}, thread_ts: {thread_ts})")

