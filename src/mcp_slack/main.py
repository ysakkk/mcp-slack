"""CLI エントリポイント"""

import logging
import sys

from mcp_slack.slack.app import create_app, create_handler
from mcp_slack.slack.events import register_handlers

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)


def main():
    """メインエントリポイント"""
    try:
        logger.info("MCP Slack を起動します...")
        
        # App を生成
        app = create_app()
        
        # イベントハンドラを登録
        register_handlers(app)
        
        # SocketModeHandler を生成して起動
        handler = create_handler(app)
        logger.info("Socket Mode で接続を開始します...")
        handler.start()
        
    except KeyboardInterrupt:
        logger.info("終了シグナルを受信しました")
        sys.exit(0)
    except Exception as e:
        logger.error(f"エラーが発生しました: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

