# 使用するPythonのバージョンを指定
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

COPY requirements.txt /bot/
RUN pip install -r requirements.txt

# アプリケーションのソースコードをコンテナにコピー
COPY . /app/

# アプリケーションを実行
CMD ["python", "app.py"]
