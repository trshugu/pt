#exec文
import os
e = "x=2\nprint `x+1`"
exec e # 3
f = open("18Tst.py") # 18Tst.pyの内容(print 'exec文から実行')
exec f # exec文から実行
