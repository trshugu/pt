# -*- coding: shift_jis -*-

import os.path
import http.client
import urllib.request

#���������O�̃e�L�X�g��Ǎ���
file = open(os.path.basename(__file__).replace("py", "txt"), 'r')

#���ԋp�R�[�h�̏����o��
result = open("result_" + os.path.basename(__file__).replace("py", "txt"), 'w')

for line in file:
	if line.startswith("http"):
		try:
			#��URL�̎擾
			if http.client.OK == urllib.request.urlopen(line).status:
				#print("ok")
				continue
			else:
				#print("ng")
				#print(line)
				#print(urllib.request.urlopen(line).status)
				result.write(line)
				result.write(urllib.request.urlopen(line).status)
		except:
			#print("ng")
			#print(line)
			result.write(line)


