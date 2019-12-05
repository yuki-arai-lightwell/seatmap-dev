#!/usr/bin/python3.6
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

with open('/var/www/cgi-bin/seatmap.txt')as f:
  reader = csv.reader(f)
  data = [row for row in reader]
  
print([0][1])


