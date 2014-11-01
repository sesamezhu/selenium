# -*- coding: utf-8 -*-
import etaoCheckin
import sys

def checkByCode():
	with open('etao.code.txt') as codeTxt:
	    for line in codeTxt:
	    	if line.startswith('#'):
	    		continue
	        nos = line.rstrip().split(' ')
	        account, pwd = nos[0], nos[1]
	        etaoCheckin.checkIn(account, pwd)

reload(sys) 
sys.setdefaultencoding('utf8')
checkByCode()
