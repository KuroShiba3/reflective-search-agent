# Reflective Search Agent

LangGraphとGoogle Geminiを使用した、自己反省機能を持つ検索エージェントです。Web検索の必要性を判断し、検索クエリを生成し、結果を評価して改善を繰り返します。

## 機能

- 質問に対してWeb検索が必要かを自動判断
- 複数の検索クエリを並列実行
- 検索結果の評価と自動改善（最大3回まで）

## 必要な環境変数

以下の環境変数が必要です：

| 環境変数名 | 説明 | 取得方法 |
|-----------|------|---------|
| `GOOGLE_API_KEY` | Google Gemini APIキー | [Google AI Studio](https://aistudio.google.com/app/apikey)で取得 |
| `GOOGLE_CSE_ID` | Google Custom Search Engine ID | [Programmable Search Engine](https://programmablesearchengine.google.com/)で作成 |

### 環境変数の設定方法

1. `.env.sample`をコピーして`.env`を作成

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

## プロジェクト構造

```
reflective-search-agent/
├── src/
│   ├── __init__.py
│   ├── graph.py          # LangGraphの定義
│   ├── nodes.py          # 各ノードの実装
│   └── state.py          # グラフの状態管理
├── config/
│   └── config.py         # 環境変数の読み込み
├── main.py               # エントリーポイント
├── pyproject.toml        # プロジェクト設定
├── Dockerfile            # Docker設定
├── .env.sample           # 環境変数のサンプル
└── README.md
```