# -*- coding: shift_jis -*-

#���v����
#�������`�F�b�N
#���d���`�F�b�N
#���t�B���^�����O
#���\�[�g
#���폜�A�ǉ��Ȃǂ̕ҏW

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
				pass
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



#
#
#
#
#


#import urllib.request
#print(urllib.request.urlopen("http://cruel.org/jindex.html").status)

#import http.client
#h = http.client.HTTPConnection('www.aoky.net')
#h.request('GET', 'articles/paul_graham/startupmistakes.htm')
#r = h.getresponse()
#print(r.status)
#print(http.client.OK)

#root, ext = os.path.splitext(__file__)
#print(root)
#print(ext)
#print(os.path.basename(__file__).replace("py", "txt"))

#for line in open(os.path.basename(__file__).replace("py", "txt"), 'r'):
#	print(line)

		#print(line.replace("http://", "").replace("\n","").split("/",1))
		#domain, url = line.replace("http://", "").split("/",1)
		#print(domain)
		#print(url)
		#h = http.client.HTTPConnection(str(domain))
		#h.request('GET', "/" + str(url))
		#r = h.getresponse()
		#print(r.status)
