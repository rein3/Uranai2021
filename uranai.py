import time
import random
import IPython
from google.colab import output

# アイコンの指定
BOT_ICON = 'https://2.bp.blogspot.com/-mRJKwyORJkQ/Wn1ZTOBrszI/AAAAAAABKKs/Bg5yjLL9RYwmfUM0pEkBA3Ky3ui0IOZWQCLcBGAs/s800/animal_smile_inu.png'
YOUR_ICON = 'https://4.bp.blogspot.com/-SC6_6x7MQnc/Wn1ZUkdcPxI/AAAAAAABKK8/qqHVlc8E7lEGsEwJ_J8H6Gp9RvfhTX67wCLcBGAs/s800/animal_smile_neko.png'

n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n

def run_chat(chat = chat, start='今日の運勢とおすすめのお菓子を紹介するね‼返事をしてくれたら始まるよ', **kw):
  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', 'ボット')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #fff;
            font-size: 10px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 6px;
            background: #eee;
            color: #333;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #66d;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)


#１つにまとめた
import requests
import re
import datetime
dt_now = datetime.datetime.now()
Ty = dt_now.year
while Ty >= 10:
  y = str(Ty)
  Ty = int(y[-1]) + int(y[-2]) + int(y[-3]) + int(y[-4])
Tm = dt_now.month
while Tm >= 10:
  m = str(Tm)
  Tm = int(m[-1]) + int(m[-2])
Td = dt_now.day
while Td >= 10:
  d = str(Td)
  Td = int(d[-1]) + int(d[-2])

def snack(num):
  url = "https://sysbird.jp/toriko/api/"
  param = {"apikey": "guest", "format": "json", "id" : num}
  data = requests.get(url, param).json()
  return data["item"]["name"] , data["item"]["url"]

# フレーム 状態をもつ辞書
frame = {}
def uranai(input_text):
  global frame # 外部の状態を参照する
  if 'asking' in frame:  # asking から更新する
    frame[frame['asking']] = input_text
    del frame['asking']

  if 'name' not in frame:
    frame['asking'] = 'name' # 名前をたずねる  
    return 'あなたの名前は？'

  if 'name' in frame and 'Byear' not in frame:
    frame['asking'] = 'Byear' # 誕生年をたずねる 
    return 'あなたの誕生年は西暦何年？（半角数字4桁）'
  pattern = r'\d\d\d\d'
  Byear = int(frame['Byear'])
  content = str(Byear)
  result = re.match(pattern, content)
  Tyear = int(dt_now.year)
  if result == None:   
    frame['asking'] = 'Byear'
    return "半角数字4桁で入力してね"
  elif Byear > Tyear:
    frame['asking'] = 'Byear'
    return "未来から来たのかな?もう一度入力してね"
  elif Byear < (Tyear - 118):
    frame['asking'] = 'Byear'
    return "ずいぶん長生きだね...もう一度入力してね"


  if 'name' in frame and 'Bmonth' not in frame:
    frame['asking'] = 'Bmonth' # 誕生日をたずねる    
    return 'あなたの誕生月は？数字だけを入力してね'
  Bmonth = int(frame['Bmonth'])
  if Bmonth > 12:
    frame['asking'] = 'Bmonth' # 誕生日をたずねる 
    return 'そんな月はないよ！もう一度入力してね'

  if 'name' in frame and 'Bday' not in frame:
    frame['asking'] = 'Bday' # 誕生日をたずねる    
    return 'あなたの誕生日は？数字だけを入力してね'

  Bday = int(frame['Bday'])
  if Bmonth == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if Bday > 31:
      frame['asking'] = 'Bday' # 誕生日をたずねる    
      return 'そんな日はないよ!もう一度入力してね'
  elif Bmonth == 4 or 6 or 9 or 11:
    if Bday > 30:
      frame['asking'] = 'Bday' # 誕生日をたずねる    
      return 'そんな日はないよ!もう一度入力してね'
  elif Bmonth == 2:
    if Bday > 29:
      frame['asking'] = 'Bday' # 誕生日をたずねる    
      return 'そんな日はないよ!もう一度入力してね'


  if ('name' in frame) and ('Byear' in frame) and ('Bmonth' in frame) and ('Bday' in frame):
    if not ('ura' in frame):
      # 占います
      By = int(frame['Byear'])
      while By >= 10:
        y = str(By)
        By = int(y[-1]) + int(y[-2]) + int(y[-3]) + int(y[-4])
      Bm = int(frame['Bmonth'])
      while Bm >= 10:
        m = str(Bm)
        Bm = int(m[-1]) + int(m[-2])
      Bd = int(frame['Bday'])
      while Bd >= 10:
        d = str(Bd)
        Bd = int(d[-1]) + int(d[-2])

      year = Ty + By
      while year >= 10:
        y = str(year)
        year = int(y[-1]) + int(y[-2])
      month = Tm + Bm
      while month >= 10:
        m = str(month)
        month = int(m[-1]) + int(m[-2])
      day = Td + Bd
      while day >= 10:
        d = str(day)
        day = int(d[-1]) + int(d[-2])
    
      unsei = int(year) + int(month) + int(day)
      okashi = str(year) + str(month) + str(day)
      while unsei >= 10:
        u = str(unsei)
        unsei = int(u[-1]) + int(u[-2])
      if unsei == 0 or 1:
        print(frame['name'] ,'におすすめのお菓子は.....' , snack(okashi))
        return '今日の運勢は小吉です☆!!'
      elif unsei == 2 or 3 or 4:
        return '今日の運勢は中吉です☆☆!!'
      elif unsei == 5 or 6 or 7:
        return '今日の運勢は吉です☆☆☆!!'
      elif unsei == 8 or 9:
        return '今日の運勢は大吉です☆☆☆☆!!'
    
  return output_text
  
def start():
  run_chat(chat=uranai)
