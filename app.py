from bs4 import BeautifulSoup
from urllib import request
import requests
from flask import Flask, render_template

app = Flask(__name__)

def line_send(message):
	token = "token_address"
	url = 'https://notify-api.line.me/api/notify'
	headers = {"Authorization": "Bearer " + token}
	payload = {"message": message}
	r = requests.post(url, headers=headers, params=payload)
	return r

def sumo():
    url = "https://www.nikkansports.com/battle/sumo/"
    html = request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("section", {"id": "topNewsArea"})
    sub = main.find("ul", {"class": "newslist"})
    return line_send(sub)

@app.route("/")
def hello():
    print(sumo())
    return render_template("index.html", name="lineに表示！")

if __name__== "__main__":
	app.run(host='0.0.0.0', port=5000)
    # app.run()
