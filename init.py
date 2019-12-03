#!/usr/bin/python3.6
#日本語を処理するのに必要
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#デバッグ機能を有効にする
cgitb.enable()

def html_head():
  print("Content-type: text/html;\n\n")
  print("<html><body><h1>test cgi</h1>\n")

def html_end():
  print("</body></html>\n")

