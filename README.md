# inf-llm

## クイックスタート(windows)

### 1. パッケージ管理ツール Scoop経由で必要なパッケージをインストール
左下の検索🔍画面で"Powershell"と検索し、Powershellアプリを管理者権限で実行を選択したあと、以下のコマンドを一行ずつ入力する。

``` powershell
# scoopのインストール
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop bucket add extras
scoop bucket add versions

# でgitをインストールしていない人はインストール
scoop install git

# nodeをインストールする
scoop install nvm yarn
nvm install 20.11.0
nvm use 20.11.0
node -v
yarn -v

# Poetry環境をインストールする
scoop install poetry
```

### 2. フロントエンドとバックエンドの環境準備

```
# pythonのインストール
# https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe

# backendのディレクトリに移動して実行
cd llama_backend
poetry install
poetry run python manage.py startapp backend
poetry run python manage.py migrate

# frontendのディレクトリに移動して実行
cd llama_frontend
poetry install
```

### 3. 必要なファイルの準備
#### .envファイルの設定

トップのディレクトリに.envと名前の付いたファイルをおく。openai apiキーを記載。
```OPENAI_API_KEY=""```

#### llama_backend/dataにllmで参照したいファイルを置く

参照したいデータ（PDF・wordなど）をこのディレクトリに置いておくと、参照してくれます。

## 開発用サーバーの設定
環境設定が完了したら、以下のコマンドを実行することで

```
# backendのディレクトリで実行
poetry run python manage.py runserver 0.0.0.0:3000
poetry run python manage.py process_tasks

# frontendのディレクトリで実行
yarn dev
```

### 参照
- https://scoop.sh/


## バージョン管理

backend: Poetry

frontend: yarn

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
