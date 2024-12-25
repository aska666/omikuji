# 使用するPythonのバージョンを指定
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# ローカルの requirements.txt をコンテナ内にコピー
COPY requirements.txt /app/

# 必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコンテナにコピー
COPY . /app/

# アプリケーションを実行
CMD ["python", "app.py"]
