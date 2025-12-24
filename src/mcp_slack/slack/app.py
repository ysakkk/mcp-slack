"""Slack App 生成モジュール"""

import logging

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from mcp_slack.config import get_slack_app_token, get_slack_bot_token

logger = logging.getLogger(__name__)


def create_app() -> App:
    """slack-bolt App を生成"""
    bot_token = get_slack_bot_token()
    app = App(token=bot_token)
    logger.info("Slack App を生成しました")
    return app


def create_handler(app: App) -> SocketModeHandler:
    """SocketModeHandler を生成"""
    app_token = get_slack_app_token()
    handler = SocketModeHandler(app, app_token)
    logger.info("SocketModeHandler を生成しました")
    return handler

