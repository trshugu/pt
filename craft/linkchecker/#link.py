# -*- coding: shift_jis -*-

import os
import httplib
import urllib2

#＊同じ名前のテキストを読込み
file = open(os.path.basename(__file__).replace("py", "txt"), 'r')

#＊返却コードの書き出し
result = open("result_" + os.path.basename(__file__).replace("py", "txt"), 'w')

for line in file:
  if line.startswith("http"):
    try:
      #＊URLの取得
      if httplib.OK == urllib2.urlopen(line).code:
        print("ok")
        continue
      else:
        print("ng")
        print(line)
        #print(urllib.request.urlopen(line).status)
        result.write(line)
        result.write(urllib2.urlopen(line).code)
    except:
      #print("ng")
      print(line)
      result.write(line)

