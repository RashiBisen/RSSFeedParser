from flask import Flask, render_template, request
from RssReader import RssParser
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		url=result.get("url")
		objRssParser = RssParser(url)
		header,feedItems= objRssParser.parse()
		return render_template("feed.html", feedItems = feedItems,header=header)

if __name__ == '__main__':
   app.run()