"""設定管理モジュール"""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# .env ファイルを読み込む
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)


def get_slack_app_token() -> str:
    """SLACK_APP_TOKEN を取得"""
    token = os.getenv("SLACK_APP_TOKEN")
    if not token:
        raise ValueError("SLACK_APP_TOKEN 環境変数が設定されていません")
    return token


def get_slack_bot_token() -> str:
    """SLACK_BOT_TOKEN を取得"""
    token = os.getenv("SLACK_BOT_TOKEN")
    if not token:
        raise ValueError("SLACK_BOT_TOKEN 環境変数が設定されていません")
    return token

