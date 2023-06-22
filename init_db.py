import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

def insert_all():
    db.myclothes.drop() #myclothes 콜렉션을 모두 지워줌

    data1 = {
        'min': 28, 'max': " ",
        'clothes': [
            {
                'type': "민소매",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "반바지",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "반팔티",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data1)

    data2 = {
        'min': 23, 'max': 27,
        'clothes': [
            {
                'type': "반팔티",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "반바지",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "치마",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data2)


    data3 = {
        'min': 20, 'max': 22,
        'clothes': [
            {
                'type': "원피스",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "블라우스",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "긴팔티",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data3)

    data4 = {
        'min': 17, 'max': 19,
        'clothes': [
            {
                'type': "가디건",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "긴바지",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "얇은니트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data4)

    data5 = {
        'min': 12, 'max': 16,
        'clothes': [
            {
                'type': "자켓",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "니트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "기모치마",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data5)

    data6 = {
        'min': 9, 'max': 11,
        'clothes': [
            {
                'type': "트렌치코트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "야상",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "기모바지",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data6)

    data7 = {
        'min': 5, 'max': 8,
        'clothes': [
            {
                'type': "울코트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "히트텍",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "가죽옷",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data7)

    data8 = {
        'min': " ", 'max': 4,
        'clothes': [
            {
                'type': "패딩",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "코트",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            },
            {
                'type': "목도리/장갑",
                'links': [
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'},
                    {'name': '...', 'mall': '...', 'img': '...', 'url': '...'}
                ]
            }
        ]
    }
    db.myclothes.insert_one(data8)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Retrieve the selected temperature from the form
    temperature = int(request.form['temperature'])

    # Perform clothing recommendation based on temperature
    if temperature > 28:
        recommendation = "Recommended outfit: Sleeveless, shorts, short-sleeved T-shirt"
    elif 23 <= temperature <= 27:
        recommendation = "Recommended outfit: Short sleeves, shorts, skirts"
    elif 20 <= temperature <= 22:
        recommendation = "Recommended outfit: One-piece, blouse, long-sleeved tee"
    elif 17 <= temperature <= 19:
        recommendation = "Recommended outfit: Cardigans, long pants, thin knits"
    elif 12 <= temperature <= 16:
        recommendation = "Recommended outfit: Jacket, knit, brushed skirt"
    elif 9 <= temperature <= 11:
        recommendation = "Recommended outfit: Trench coat, field jacket, brushed pants"
    elif 5 <= temperature <= 8:
        recommendation = "Recommended outfit: Wool coat, heat tech, leather jacket"
    else:
        recommendation = "Recommended outfit: Padding, coat, scarf, gloves"

    return render_template('recommend.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
