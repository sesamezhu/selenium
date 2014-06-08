import sys
print sys.getdefaultencoding()
reload(sys) 
sys.setdefaultencoding('utf8')