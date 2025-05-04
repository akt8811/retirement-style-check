from flask import Flask, render_template, request
import os

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
        description = (
            "「定年って何のこと？」と言わんばかりに、退職後もコンサルやオンライン会議で多忙な日々。"
            "週に3日とは言いつつ、気づけば毎日誰かと打ち合わせ。後輩の相談にも頼られっぱなしです。"
            "周囲からは『少し休んだら？』と言われつつも、ご本人は充実感いっぱい。"
            "好きなことを仕事にしている、まさに“現役”の名にふさわしいライフスタイルですね。"
        )
        tweet = '定年後も現役ビジネスマンタイプらしいです💼'
        image = '/static/images/genneki.jpg'

    elif count_c >= 4:
        result_type = '旅に生きる自由人タイプ'
        description = (
            "「今日どこ泊まろうか？」が口ぐせ。地酒に温泉、朝市に出会い…。"
            "日本中をマイペースに巡る旅の暮らしがあなたの理想。"
            "計画に縛られず、ふと思い立って出発する自由さは、定年後の特権かもしれません。"
            "新しい景色や人との出会いが、あなたの生きがいになっていきそうです。"
        )
        tweet = '定年後は旅に生きる自由人タイプらしいです🧳'
        image = '/static/images/tabi.jpg'

    elif count_b > count_a:
        result_type = '地域デビュー職人タイプ'
        description = (
            "町内会やNPO、子ども食堂など、地域での活動に積極的に関わるあなた。"
            "最初はお手伝いだったのに、いつの間にか中心人物に。"
            "『元会社員・現なんでも屋』なんて肩書きも似合う、地域の頼れる存在になりそう。"
            "人とのつながりが、これからの暮らしを豊かにしてくれるタイプです。"
        )
        tweet = '定年後は地域デビュー職人タイプらしいです🛠'
        image = '/static/images/tiiki.jpg'

    else:
        result_type = 'おうち満喫のんびりタイプ'
        description = (
            "家庭菜園、ラジオ体操、猫とのあいさつ──そんなゆるやかな毎日が、あなたにとっての幸せ。"
            "定年後は、無理せずのんびり、自分のペースで過ごしたい気持ちが強そうです。"
            "読書や趣味に打ち込んだり、家族と穏やかに過ごす時間が、心を満たしてくれるはず。"
            "“ゆるく、心地よく”が、これからのキーワードです。"
        )
        tweet = '定年後はおうち満喫タイプらしいです🪴'
        image = '/static/images/outi.jpg'

    twitter_url = f"https://twitter.com/intent/tweet?text={tweet}%0A%23定年後スタイル診断"

    return render_template(
        'result.html',
        result_type=result_type,
        description=description,
        twitter_url=twitter_url,
        image=image
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

