open(filename [,mode [,buffsize]])
filename：ファイル名
mode：'r', 'w','a','b' # read, write, append, binary +もつけられる
buffsize：ファイルオブジェクトのバッファサイズ。
0：バッファリングなし
1：ラインバッファ
その他の正数：実際のバッファサイズ
負数：システムデフォルト値
