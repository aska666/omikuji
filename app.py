from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# おみくじの結果リスト
RESULTS = [
    # 動物
    "いぬ", "ねこ", "かんがるー", "さる", "ぞう", "きりん", "くま", "うさぎ", "らいおん", "ぺんぎん",

    # 乗り物
    "くるま", "じてんしゃ", "ばす", "ひこうき", "へりこぷたー", "ろけっと",

    # 食べ物
    "ばなな", "りんご", "すし", "おにぎり",

    # 日常の動作
    "はしる", "あるく", "のむ", "たべる", "うたう", "ねむる", "てをふる", "わらう", "なく", "じゃんぷ",

    # スポーツ
    "さっかー", "ばすけっとぼーる", "やきゅう", "すいえい", "ばどみんとん", "てにす", "ばれーぼーる", "ごるふ",

    # 職業
    "おいしゃさん(お医者さん)", "けいさつかん(警察官)", "しょうぼうし(消防士)",

    # 自然
    "あめ(雨)", "かぜ(風)", "き(木)", "はな(花)", "やま(山)"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw', methods=['GET'])
def draw():
    result = random.choice(RESULTS)
    # 結果をランダムに選び、残りの結果リストの長さを一緒に返す
    return jsonify({"result": result, "remaining": RESULTS})

@app.route('/reset', methods=['POST'])
def reset():
    global RESULTS
    if len(RESULTS) > 0:
        removed_result = RESULTS.pop()  # 末尾の結果を削除
        return jsonify({"result": None, "remaining": RESULTS})
    else:
        return jsonify({"result": None, "remaining": RESULTS})

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
