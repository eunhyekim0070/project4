from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.musinsa.com/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()

soup = BeautifulSoup(html, 'html.parser')
info = soup.find("div", class_="keyImg")
if info is not None:
    imgUrl = info.find("img")['src']
    img = info.find("img")['alt']
    print(imgUrl, img)

client = MongoClient('localhost', 27017)
db = client.dbsparta

def start_server():
    server = Flask("옷 저장소")

    @server.route('/')
    def home():
        return render_template('storage.html')

    @server.route('/clothes', methods=['POST'])
    def add_clothes():
        max_val = request.form['max']
        min_val = request.form['min']
        type_val = request.form['type']
        mall_val = request.form['mall']
        url_val = request.form['url']

        html = urlopen(url_val).read()
        soup = BeautifulSoup(html, 'html.parser')
        info = soup.find("div", class_="keyImg")
        if info is not None:
            imgUrl = info.find("img")['src']
            img = info.find("img")['alt']
        else:
            imgUrl = ""
            img = ""

        cloth = {
            'max': max_val,
            'min': min_val,
            'type': type_val,
            'mall': mall_val,
            'url': url_val,
            'imgUrl': imgUrl,
            'img': img
        }
        db.clothes.insert_one(cloth)
        return jsonify({'result':'success', 'msg': '옷 저장 성공!'})

    @server.route('/clothes', methods=['GET'])
    def read_clothes_list():
        clothes = list(db.clothes.find({}, {'_id': 0}))
        return jsonify({'result': 'success', 'clothes': clothes})

    server.run('0.0.0.0', port=5000, debug=True)

start_server()
