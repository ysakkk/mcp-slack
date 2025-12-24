# mcp-slack

Slack MCP（制御中枢） - Socket Mode を使った MCP 実装

## 概要

Slack Socket Mode を使った MCP を Python で実装しています。
slack-bolt を利用し、Slack からの `app_mention` を受信して即座に ACK（返信）します。

## セットアップ

### 1. 依存関係のインストール

```bash
pip install -e .
```

### 2. 環境変数の設定

`.env` ファイルを作成し、以下の環境変数を設定してください：

```bash
cp .env.example .env
# .env を編集してトークンを設定
```

- `SLACK_APP_TOKEN`: Socket Mode の App-Level Token
- `SLACK_BOT_TOKEN`: Bot User OAuth Token

## 使い方

```bash
mcp-slack
```

Slack でボットにメンション（`@bot`）すると、即座に「受信しました」と返信します。

## プロジェクト構造

```
src/
└── mcp_slack/
    ├── __init__.py
    ├── config.py          # 環境変数読み込み
    ├── main.py            # CLI エントリポイント
    └── slack/
        ├── __init__.py
        ├── app.py         # slack-bolt App 生成
        └── events.py      # イベントハンドラ
```

## 開発方針

- **受信・判断・委譲**: MCP の役割は受信と判断のみ。実処理は外部に委譲
- **構造の分離**: Slack / MCP / 実行系を分離
- **軽量な handler**: handler 内に重い処理を書かない

