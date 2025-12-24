"""Slack イベントハンドラ"""

import logging

from slack_bolt import App

logger = logging.getLogger(__name__)


def register_handlers(app: App) -> None:
    """イベントハンドラを登録"""
    
    @app.event("app_mention")
    def handle_app_mention(event, say, client):
        """app_mention イベントを処理"""
        logger.info(f"app_mention を受信: {event}")
        
        # 即座に ACK を返す
        channel = event["channel"]
        thread_ts = event.get("ts")
        
        say(
            text="受信しました",
            thread_ts=thread_ts,
        )
        
        logger.info(f"ACK を送信しました (channel: {channel}, thread_ts: {thread_ts})")

