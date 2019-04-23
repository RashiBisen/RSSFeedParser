import feedparser
from unidecode import unidecode

class RssParser:
	def __init__(self, url):
		self.url = url

	def parse(self):
		feed = feedparser.parse(self.url)
		return self.parseHeader(feed["feed"]),self.parseItems(feed["entries"])

	def parseItems(self,feed):
		dictlist = []
		for key in feed:
			dict = {} 				
			dict['title']= unidecode(key["title"])
			dict['link']= key["link"]
			dict['description']= unidecode(key["description"])
			if 'media_thumbnail' in key:
				dict['image']= key["media_thumbnail"][0]["url"]
			dictlist.append(dict)
		return dictlist

	def parseHeader(self,feed):
		header={}
		if('image' in feed):
			header['imageUrl']=feed['image']['href']
		if('title' in feed):
			header['title'] = feed['title']
		return header