from flask import Flask, request, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

# 復習日を計算する関数
def calculate_review_dates(start_date):
    review_days = [1, 7, 14, 30]  # 復習のタイミング（1日後、7日後、14日後、30日後）
    review_dates = [(start_date + timedelta(days=days)).strftime("%Y-%m-%d") for days in review_days]
    return review_dates

# トップページのルート
@app.route('/')
def index():
    return render_template('index.html')

# 復習日を計算するルート
@app.route('/calculate', methods=['POST'])
def calculate():
    start_date_str = request.form['start_date']  # フォームから取得した日付を文字列として取得
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")  # 日付の文字列を datetime形式に変換
    review_dates = calculate_review_dates(start_date)  # 復習日を計算
    return render_template('result.html', review_dates=review_dates)  # 結果を表示

# アプリケーションの実行
if __name__ == '__main__':
    app.run(debug=True)
