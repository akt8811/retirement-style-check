from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    answers = [request.form.get(f'q{i}') for i in range(1, 11)]

    count_a = answers.count('A')
    count_b = answers.count('B')
    count_c = answers.count('C')

    # 判定ロジック
    if count_c >= 4 and answers[1] == 'C' and answers[4] == 'C':
        result_type = '現役ビジネスマンタイプ'
        description = '「定年って何のこと？」退職後も週3でコンサル、Zoom会議、後輩指導。周囲からは「休んだら？」と言われるが、楽しそうなのでOK。'
        tweet = '定年後も現役ビジネスマンタイプらしいです💼'
    elif count_c >= 4:
        result_type = '旅に生きる自由人タイプ'
        description = '「今日どこ泊まろうか」が口ぐせの自由人。地酒、温泉、朝市…。全国津々浦々をマイペースに旅する暮らし。'
        tweet = '定年後は旅に生きる自由人タイプらしいです🧳'
    elif count_b > count_a:
        result_type = '地域デビュー職人タイプ'
        description = '町内会、NPO、子ども食堂…。気づけば地域の顔に。「元会社員・現なんでも屋」と名乗ってそう。'
        tweet = '定年後は地域デビュー職人タイプらしいです🛠'
    else:
        result_type = 'おうち満喫のんびりタイプ'
        description = '家庭菜園・ラジオ体操・猫とのあいさつ。こういう毎日が一番幸せ、という人。'
        tweet = '定年後はおうち満喫タイプらしいです🪴'

    twitter_url = f"https://twitter.com/intent/tweet?text={tweet}%0A%23定年後スタイル診断"

    return render_template('result.html', result_type=result_type, description=description, twitter_url=twitter_url)

if __name__ == '__main__':
     import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
