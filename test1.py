#!/usr/bin/python3.6

#モジュールの読み込み
import cgi
import cgitb
import csv
from http import cookies
#日本語を処理するのに必要
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#デバッグ機能を有効にする
cgitb.enable()


#席番号を変数へロードおよび数値型へ変換
SeatNum = "12"
intSeatNum = int(SeatNum)

mode = "mod"

#メイン処理

#画面表示モード（event=form)
if mode == "form":
  # 座席表テキストファイルの読み込み、リストへ格納
  with open('/var/www/cgi-bin/seatmap.txt')as f:
    reader = csv.reader(f)
    data = [row for row in reader]

  #リストから指定の席番号の情報を取得(現使用者と最終更新)
  SeatMember = data[int(SeatNum)-1][1]
  RegiDate = data[int(SeatNum)-1][2]
  
  #画面出力
  print("Content-type: text/html;\n\n")
  print("<html><body><h1>座席の更新</h1>\n")  
  print("<hr>")
  if SeatMember == "":
    print("席番号 ",SeatNum," は現在利用されていません。トップ画面に戻り、登録画面で登録してください。")
    print("<br><hr><a href=./index.cgi>TOP</a><br>")
    print("</body></html>\n")
    sys.exit(0)

  else:
    print("席番号",SeatNum,"の現在利用者は、",SeatMember,"です。<br>")
    print("LastUpdate:",RegiDate)

  print("<hr>")
  print("更新するには名前を入力し【更新】ボタンを押してください。")
  print("<form id=\"form1\" name=\"form1\" method=\"post\" action=mod.cgi>")
 
  print("名前：<input type=\"text\" name=\"name\" value=\"\">")
  print("""
<input type=\"submit\" value=\"更新\">
<input type=\"hidden\" name=\"event\" value=\"mod\">
  """)
  print("<input type=\"hidden\" name=\"num\" value=\"",SeatNum,"\">")
  print("</form>")

  print("<a href=./index.cgi>TOP</a>")
  print("</body></html>\n")
  sys.exit(0)  


#更新モード（event=mod)
if mode == "mod":
  #リストから指定の席番号の情報を取得(現使用者と最終更新)
  SeatMemberMod = "fuga"
  
  #ファイルを読み込み
  with open('/var/www/cgi-bin/seatmap.txt')as f:
    reader = csv.reader(f)
    data = [row for row in reader]
    
  for i in range(len(data)):
    if data[i][0] == SeatNum:
      data[i][1] = SeatMemberMod
      data[i][2] = "2019/12/10 11:00" 
  
  with open('/var/www/cgi-bin/seatmap.txt','w')as f:
    writer = csv.writer(f)
    writer.writerows(data)
     
    
  print("Content-type: text/html;\n\n")
  print("<html><body><h1>座席の更新</h1>\n")
  print("<hr>")
  print("更新しました。（テスト表示）")
  print("<hr>")
  print("<a href=./index.cgi>TOP</a>")
  print("</body></html>\n")
  sys.exit(0)




