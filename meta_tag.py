_author__ = 'nishank'

from bs4 import BeautifulSoup
import urllib2
import sys
website = sys.argv[1]
soup = BeautifulSoup(urllib2.urlopen(website))
if soup('meta'):
	for meta_tag in soup('meta'):
		try:
			print meta_tag['name']+' ===>',
			print meta_tag['content']
		except:
			pass
else:
	print 'NO METADATA FOUND'
