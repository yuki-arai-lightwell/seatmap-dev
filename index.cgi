#!/usr/bin/python3.6
import init
import cgi
import cgitb
#from http import cookies

#日本語を処理するのに必要
#import sys
#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#デバッグ機能を有効にする
#cgitb.enable()


#フォーム情報の取り込み
form = cgi.FieldStorage()

if len(form) == 0:
    CC=""
    C=""
else:
    CC=form["name"].value
    event=form["event"].value
#    print("Set-Cookie: NAME="+CC)
    C = cookies.SimpleCookie()
    C["name"] = CC

#サンプル
print("Content-type: text/html;\n\n")
print("<html><body><h1>test cgi</h1>\n")
print("""
<br>
AAA<br>
BBB<br>
<hr>
CCC<br>
テスト表示<br>
<form id="form1" name="form1" method="post" action=test.py>
<br>
名前：<input type="text" name=name value="名前">
<input type="submit" value="更新">
<input type="hidden" name="event" value="mod">
<input type="hidden" name="num" value="24">
</form>
""")
print("<hr>入力内容<br>")
#フォームの内容を表示
print(f'名前：<b>',CC,"</b><br>")
print(C)
print("</body></html>\n")
