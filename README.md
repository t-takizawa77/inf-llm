# inf-llm

## バージョン管理

backend: Poetry

frontend: yarn

## 事前にインストール

python: 3.12.8

node:v14.8.0

## セットアップ

```
# backend
python manage.py startapp backend
poetry run python manage.py migrate

# frontend
poetry install

# .env
# トップのディレクトリにおく。openai apiキーを記載。
OPENAI_API_KEY=""

# llama_backend/data
# 参照したいデータ（PDF・wordなど）をおいておく
```

## 開発用サーバー

```
poetry run python manage.py runserver 0.0.0.0:3000
yarn dev
poetry run python manage.py process_tasks
```

## ディレクトリ
backend_llama : django project
backend : django app
frontend : yarn

## 参照
django
https://qiita.com/pythonista/items/19613663ef7bb3c57d4f#%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%AE%E4%BD%9C%E6%88%90

https://qiita.com/YoshitakaOkada/items/570c025cf235062649c8

https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8

next.js
https://zenn.dev/akgcog/articles/1f25938ada06c5
