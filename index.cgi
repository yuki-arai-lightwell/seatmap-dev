#!/usr/bin/python3.6
#import init
import cgi
import cgitb
import csv
import datetime
import pathlib
import shutil
from http import cookies

#日本語を処理するのに必要
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#デバッグ機能を有効にする
cgitb.enable()

#HTML Header
print("Content-type: text/html;\n\n")

#フォーム情報の取り込み
form = cgi.FieldStorage()

#dataファイルの初期化
now = datetime.datetime.now()
month = '{0:%d}'.format(now)
p = pathlib.Path('/var/www/cgi-bin/seatmap.txt')
ff=datetime.datetime.fromtimestamp(p.stat().st_ctime)
fileday = '{0:%d}'.format(ff)
if month != fileday:
   src = '/var/www/cgi-bin/seatmap.org'
   copy = '/var/www/cgi-bin/seatmap.txt'
   shutil.copyfile(src,copy)

#データファイルを変数に置き換え
with open('/var/www/cgi-bin/seatmap.txt', encoding='utf-8') as f:
   reader = csv.reader(f)
   data = [row for row in reader]

if len(form) == 0:
    CC=""
    C=""
else:
    CC=form["name"].value
    event=form["event"].value
    C = cookies.SimpleCookie()
    C["name"] = CC

#データ判定および必要変数追加
cnt=0
for line in data:
   if len(line[1]) == 0:
      CGI="add.cgi"
      FORM="登録"
      COLOR="#FFFFFF"
      NAME="　"
      data[cnt]=data[cnt][0],data[cnt][1],data[cnt][2],CGI,FORM,COLOR,NAME
      cnt=cnt + 1
   else:
      CGI="mod.cgi"
      FORM="更新"
      COLOR="#BAF1FC"
      NAME=line[1]
      data[cnt]=data[cnt][0],data[cnt][1],data[cnt][2],CGI,FORM,COLOR,NAME
      cnt=cnt + 1

#サンプル
print("<html><body><TITLE>ITSS座席表</TITLE>\n")
print("""
<table width="200" border="0">
  <tbody>
    <tr>
      <td valign="bottom"><table width="200" border="1">
        <tbody>
          <tr>
            <td colspan=2 bgcolor=#BAF1FC><center><b>杉崎</b></center>03-5828-XXXX(xxxx)</td>
          </tr>
          <tr>
""")

print("<td bgcolor=",data[0][5]," valign=top><form id=form1 name=form1 method=post action=",data[0][3],">")
print("<input type=submit value=",data[0][4],"><input type=hidden name=event value=form><input type=hidden name=num value=1>")
print("<center><b>",data[0][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[1][5]," valign=top><form id=form1 name=form1 method=post action=",data[1][3],">")
print("<input type=submit value=",data[1][4],"><input type=hidden name=event value=form><input type=hidden name=num value=2>")
print("<center><b>",data[1][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[2][5]," valign=top><form id=form1 name=form1 method=post action=",data[2][3],">")
print("<input type=submit value=",data[2][4],"><input type=hidden name=event value=form><input type=hidden name=num value=3>")
print("<center><b>",data[2][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[3][5]," valign=top><form id=form1 name=form1 method=post action=",data[3][3],">")
print("<input type=submit value=",data[3][4],"><input type=hidden name=event value=form><input type=hidden name=num value=4>")
print("<center><b>",data[3][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[4][5]," valign=top><form id=form1 name=form1 method=post action=",data[4][3],">")
print("<input type=submit value=",data[4][4],"><input type=hidden name=event value=form><input type=hidden name=num value=5>")
print("<center><b>",data[4][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[5][5]," valign=top><form id=form1 name=form1 method=post action=",data[5][3],">")
print("<input type=submit value=",data[5][4],"><input type=hidden name=event value=form><input type=hidden name=num value=6>")
print("<center><b>",data[5][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[6][5]," valign=top><form id=form1 name=form1 method=post action=",data[6][3],">")
print("<input type=submit value=",data[6][4],"><input type=hidden name=event value=form><input type=hidden name=num value=7>")
print("<center><b>",data[6][6],"</b></center>9174(2364)</form></td>")

print("<td bgcolor=",data[7][5]," valign=top><form id=form1 name=form1 method=post action=",data[7][3],">")
print("<input type=submit value=",data[7][4],"><input type=hidden name=event value=form><input type=hidden name=num value=8>")
print("<center><b>",data[7][6],"</b></center>9174(2365)</form></td>")

print("""
          </tr>
        </tbody>
      </table>
      </td>
      <td valign="bottom"><table width="200" border="1">
        <tbody>
          <tr>
            <td colspan=2 bgcolor=#BAF1FC><center><b>星野</b></center>03-5828-XXXX(xxxx)</td>

          </tr>
          <tr>
          <tr>
""")

print("<td bgcolor=",data[8][5]," valign=top><form id=form1 name=form1 method=post action=",data[8][3],">")
print("<input type=submit value=",data[8][4],"><input type=hidden name=event value=form><input type=hidden name=num value=9>")
print("<center><b>",data[8][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[9][5]," valign=top><form id=form1 name=form1 method=post action=",data[9][3],">")
print("<input type=submit value=",data[9][4],"><input type=hidden name=event value=form><input type=hidden name=num value=10>")
print("<center><b>",data[9][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[10][5]," valign=top><form id=form1 name=form1 method=post action=",data[10][3],">")
print("<input type=submit value=",data[10][4],"><input type=hidden name=event value=form><input type=hidden name=num value=11>")
print("<center><b>",data[10][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[11][5]," valign=top><form id=form1 name=form1 method=post action=",data[11][3],">")
print("<input type=submit value=",data[11][4],"><input type=hidden name=event value=form><input type=hidden name=num value=12>")
print("<center><b>",data[11][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[12][5]," valign=top><form id=form1 name=form1 method=post action=",data[12][3],">")
print("<input type=submit value=",data[12][4],"><input type=hidden name=event value=form><input type=hidden name=num value=13>")
print("<center><b>",data[12][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[13][5]," valign=top><form id=form1 name=form1 method=post action=",data[13][3],">")
print("<input type=submit value=",data[13][4],"><input type=hidden name=event value=form><input type=hidden name=num value=14>")
print("<center><b>",data[13][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[14][5]," valign=top><form id=form1 name=form1 method=post action=",data[14][3],">")
print("<input type=submit value=",data[14][4],"><input type=hidden name=event value=form><input type=hidden name=num value=15>")
print("<center><b>",data[14][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[15][5]," valign=top><form id=form1 name=form1 method=post action=",data[15][3],">")
print("<input type=submit value=",data[15][4],"><input type=hidden name=event value=form><input type=hidden name=num value=16>")
print("<center><b>",data[15][6],"</b></center>XXXX(xxxx)</form></td>")

print("""
</tr>
        </tbody>
      </table></td>
      <td valign="bottom"><table width="200" border="1">
        <tbody>
          <tr>
""")
print("<td bgcolor=",data[16][5]," valign=top><form id=form1 name=form1 method=post action=",data[16][3],">")
print("<input type=submit value=",data[16][4],"><input type=hidden name=event value=form><input type=hidden name=num value=17>")
print("<center><b>",data[16][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[17][5]," valign=top><form id=form1 name=form1 method=post action=",data[17][3],">")
print("<input type=submit value=",data[17][4],"><input type=hidden name=event value=form><input type=hidden name=num value=18>")
print("<center><b>",data[17][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[18][5]," valign=top><form id=form1 name=form1 method=post action=",data[18][3],">")
print("<input type=submit value=",data[18][4],"><input type=hidden name=event value=form><input type=hidden name=num value=19>")
print("<center><b>",data[18][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[19][5]," valign=top><form id=form1 name=form1 method=post action=",data[19][3],">")
print("<input type=submit value=",data[19][4],"><input type=hidden name=event value=form><input type=hidden name=num value=20>")
print("<center><b>",data[19][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[20][5]," valign=top><form id=form1 name=form1 method=post action=",data[20][3],">")
print("<input type=submit value=",data[20][4],"><input type=hidden name=event value=form><input type=hidden name=num value=21>")
print("<center><b>",data[20][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[21][5]," valign=top><form id=form1 name=form1 method=post action=",data[21][3],">")
print("<input type=submit value=",data[21][4],"><input type=hidden name=event value=form><input type=hidden name=num value=22>")
print("<center><b>",data[21][6],"</b></center>XXXX(xxxx)</form></td></tr><tr>")

print("<td bgcolor=",data[22][5]," valign=top><form id=form1 name=form1 method=post action=",data[22][3],">")
print("<input type=submit value=",data[22][4],"><input type=hidden name=event value=form><input type=hidden name=num value=23>")
print("<center><b>",data[22][6],"</b></center>XXXX(xxxx)</form></td>")

print("<td bgcolor=",data[23][5]," valign=top><form id=form1 name=form1 method=post action=",data[23][3],">")
print("<input type=submit value=",data[23][4],"><input type=hidden name=event value=form><input type=hidden name=num value=24>")
print("<center><b>",data[23][6],"</b></center>XXXX(xxxx)</form></td>")

print("""
          </tr>
        </tbody>
      </table></td>
    </tr>
  </tbody>
</table>
""")
#print(data)
print("</body></html>\n")
