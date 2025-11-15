# Reflective Search Agent

LangGraphとGoogle Geminiを使用した、自己反省機能を持つWeb検索エージェント。

ユーザーの質問に対して検索の必要性を自動判断し、最適な検索クエリを生成・実行し、回答の品質を評価して自動改善する。

## 機能

- ユーザーの質問に対してWeb検索が必要かを自動判断
- 最適な検索クエリを自動生成（1-2個）
- 複数の検索クエリを並列実行
- 検索結果のWebページから情報を自動取得
- 検索結果を統合して自然な日本語回答を生成
- 回答品質を自動評価し、必要に応じて検索または回答を改善（最大3回まで）
- 会話コンテキストを保持した応答生成

## プロジェクト構造

```
reflective-search-agent/
├── src/
│   ├── __init__.py
│   ├── graph.py          # LangGraphの定義
│   ├── nodes.py          # 検索判定・クエリ生成・検索実行・回答生成・評価ノード
│   ├── state.py          # グラフの状態管理
│   └── logger.py         # ロガー設定
├── config/
│   └── config.py         # 環境変数の読み込み
├── main.py               # エントリーポイント
├── pyproject.toml        # プロジェクト設定
├── Dockerfile            # Docker設定
├── .env.sample           # 環境変数のサンプル
└── README.md
```

## 技術スタック

- **LLM**: Google Gemini (gemini-2.0-flash)
- **フレームワーク**: LangGraph 0.2.0+
- **検索**: Google Custom Search API
- **Webスクレイピング**: WebBaseLoader (BeautifulSoup)
- **言語**: Python 3.12+
- **パッケージ管理**: uv

## 必要な環境変数

以下の環境変数が必要：

| 環境変数名 | 説明 | 取得方法 |
|-----------|------|---------|
| `GOOGLE_API_KEY` | Google Gemini APIキー | [Google AI Studio](https://aistudio.google.com/app/apikey)で取得 |
| `GOOGLE_CSE_ID` | Google Custom Search Engine ID | [Programmable Search Engine](https://programmablesearchengine.google.com/)で作成 |

### 環境変数の設定方法

1. `.env.sample`をコピーして`.env`を作成

```bash
cp .env.sample .env
```

2. `.env`ファイルを編集して、実際のAPIキーとCSE IDを設定

## セットアップ

### 1. ローカル環境で実行

#### 前提条件
- Python 3.12以上
- [uv](https://github.com/astral-sh/uv)がインストールされていること

#### インストールと実行

```bash
# 依存関係のインストール
uv sync

# アプリケーションの実行
uv run main.py
```

### 2. Dockerで実行

#### イメージのビルド

```bash
docker build -t reflective-search-agent .
```

#### コンテナの実行

```bash
docker run reflective-search-agent
```