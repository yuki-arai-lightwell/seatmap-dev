#!/usr/bin/python3.6
################################################
# (sample) Seatmap 更新処理
# Lw NewTech ARA/MIYA
# Last Update 2019/12/13 
################################################

#モジュールの読み込み
import datetime
import cgi
import cgitb
import csv
from http import cookies
#日本語を処理するのに必要
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='shift_jis')

#デバッグ機能を有効にする
cgitb.enable()

#フォームの情報取得
form = cgi.FieldStorage()

#エラー処理：イベントのチェック、イベント指定がない場合はエラー表示
if "event" not in form:
  print("Content-type: text/html;\n\n")
  print("<html><body><h1>更新処理ERROR-1</h1>\n")
  print("<META http-equiv=Refresh content='5;URL=./index.cgi'>")
  print("<hr>")
  print("イベントが不正です。トップ画面から操作してください。")
  print("<hr>")
  print("<a href=./index.cgi>TOP</a>")
  print("</body></html>\n")
  sys.exit(0)

#エラー処理：イ席番号のチェック、席番号がない場合はエラー表示
if "num" not in form:
  print("Content-type: text/html;\n\n")
  print("<html><body><h1>更新処理ERROR-2</h1>\n")
  print("<META http-equiv=Refresh content='5;URL=./index.cgi'>")
  print("<hr>")
  print("席番号不明。トップ画面から操作してください。")
  print("<hr>")
  print("<a href=./index.cgi>TOP</a>")
  print("</body></html>\n")
  sys.exit(0)

#席番号を変数へロードおよび数値型へ変換
SeatNum = form["num"].value
intSeatNum = int(SeatNum)

#エラー処理：席番号に範囲がの番号が指定された場合はエラー表示
if intSeatNum < 1 or intSeatNum > 24 :
  print("Content-type: text/html;\n\n")
  print("<html><body><h1>更新処理ERROR-3</h1>\n")
  print("<META http-equiv=Refresh content='5;URL=./index.cgi'>")
  print("<hr>")
  print("席番号",SeatNum,"は範囲外です。トップ画面から操作してください。")
  print("<hr>")
  print("<a href=./index.cgi>TOP</a>")
  print("</body></html>\n")
  sys.exit(0)


#メイン処理

#画面表示モード（event=form)
if form["event"].value == "form":
  # 座席表テキストファイルの読み込み、リストへ格納
  # with open('/var/www/cgi-bin/seatmap.txt')as f:
  with open('/var/www/cgi-bin/seatmap.txt',encoding='utf-8')as f:
    reader = csv.reader(f)
    data = [row for row in reader]

  #リストから指定の席番号の情報を取得(現使用者と最終更新)
  SeatMember = data[int(SeatNum)-1][1]
  RegiDate = data[int(SeatNum)-1][2]

  #画面出力
  print("Content-type: text/html;\n\n")
  print("<html><body><h1>座席の更新</h1>\n")
  print("<hr>")

  #更新モード
  if "forcemod" not in form:
    if SeatMember == "":
      #通常モード：利用者なし
      print("<META http-equiv=Refresh content='5;URL=./index.cgi'>")
      print("席番号 ",SeatNum," は現在利用されていません。トップ画面に戻り、登録画面で登録してください。")
      print("<br><hr><a href=./index.cgi>TOP</a><br>")
      print("</body></html>\n")
      sys.exit(0)
    else:
      #通常モード：利用者あり
      print("座席",SeatNum,"の現在利用者は、",SeatMember,"です。<br>")
      print("LastUpdate:",RegiDate)
  elif "forcemod" in form:
    #強制更新モード
    print("強制更新モードです。座席番号:",SeatNum)

  # 更新画面表示
  print("<hr>")
  print("更新するには名前を入力し【更新】ボタンを押してください。席を空席にする場合は、【空席にする】を押してください。<br>")
  print("<form id=\"form1\" name=\"form1\" method=\"post\" action=mod.cgi>")

  print("名前：<input type=\"text\" name=\"name\" value=\"",SeatMember,"\">",sep='')
  print("""
<input type=\"submit\" name=\"submod\" value=\"更新\">
<input type=\"submit\" name=\"subclear\" value=\"空席にする\">
<input type=\"hidden\" name=\"event\" value=\"mod\">
  """)
  print("<input type=\"hidden\" name=\"num\" value=\"",SeatNum,"\">",sep='')
  print("</form>")

  print("<a href=./index.cgi>TOP</a>")
  print("</body></html>\n")
  #更新画面表示終了（event=form終了)
  sys.exit(0)

#更新モード（event=mod)
if form["event"].value == "mod":
  #フォームの名前欄入力チェック
  if "name" not in form:
    print("Content-type: text/html;\n\n")
    print("<html><body><h1>更新処理ERROR-5</h1>\n")
    print("<META http-equiv=Refresh content='5;URL=./mod.cgi?&event=form&num=",intSeatNum,"'>",sep='')
    print("<hr>")
    print("名前を入力してください。")
    print("<hr>")
    print("<a href=\"./mod.cgi?&event=form&num=",intSeatNum,"\">戻る</a>",sep='')
    print("</body></html>\n")
    sys.exit(0)

  #更新処理画面表示開始
  SeatMemberMod = form["name"].value
  print("Content-type: text/html;\n\n")
  print("<html><body><h1>座席の更新</h1>\n")
  print("<META http-equiv=Refresh content='5;URL=./index.cgi'>")
  print("<hr>")

  #リストから指定の席番号の情報を取得(現使用者と最終更新)
  #ファイルを読み込みリストへ
  # with open('/var/www/cgi-bin/seatmap.txt')as f:
  with open('/var/www/cgi-bin/seatmap.txt',encoding='utf-8')as f:
    reader = csv.reader(f)
    data = [row for row in reader]

  # 書き換え
  for i in range(len(data)):
    if int(data[i][0]) == intSeatNum :
      if "subclear" not in form:
        # 名前更新
        data[i][1] = SeatMemberMod
        #現在時刻を取得し更新
        nowDate = datetime.datetime.now()
        data[i][2] = nowDate.strftime("%Y/%m/%d %H:%M:%S")
        print("座席",SeatNum,"の利用者は、「",SeatMemberMod,"」に更新しました。")
      if "submod" not in form:
        data[i][1] = ""
        data[i][2] = ""
        print("座席",SeatNum,"を開放しました。"
)
  #リストの内容をCSVファイルへ吐き出す
  # with open('/var/www/cgi-bin/seatmap.txt','w')as f:
  with open('/var/www/cgi-bin/seatmap.txt','w',encoding='utf-8')as f:
    writer = csv.writer(f)
    writer.writerows(data)

  #更新処理画面表示
  print("<hr>")
  print("<a href=\"./mod.cgi?&event=form&num=",intSeatNum,"\">戻る</a>",sep='')
  print("<a href=./index.cgi>TOP</a>")
  print("</body></html>\n")
  #更新画面表示終了（event=mod終了)
  sys.exit(0)

#エラー処理：イベント不正時の画面表示(eventが空以外で何かしら指定している場合)
print("Content-type: text/html;\n\n")
print("<html><body><h1>更新処理ERROR-9</h1>\n")
print("<META http-equiv=Refresh content='5;URL=./index.cgi'>")
print("<hr>")
print("イベントが不正です。トップ画面から操作してください。")
print("<hr>")
print("<a href=./index.cgi>TOP</a>")
print("</body></html>\n")
sys.exit(0)
